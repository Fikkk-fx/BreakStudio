import aiosqlite
import json
import datetime
from contextlib import asynccontextmanager
from .config import settings

@asynccontextmanager
async def get_db():
    async with aiosqlite.connect(settings.DATABASE_PATH) as db:
        db.row_factory = aiosqlite.Row
        yield db

async def init_db():
    async with get_db() as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS jobs (
                id TEXT PRIMARY KEY,
                type TEXT,
                model TEXT,
                prompt TEXT,
                status TEXT,
                params TEXT,
                input_files TEXT,
                prediction_id TEXT,
                output_url TEXT,
                output_path TEXT,
                error TEXT,
                created_at TEXT,
                updated_at TEXT,
                elapsed_seconds REAL
            )
        ''')
        await db.commit()

async def create_job(job_data: dict) -> dict:
    now = datetime.datetime.utcnow().isoformat()
    job_data['created_at'] = now
    job_data['updated_at'] = now
    async with get_db() as db:
        keys = list(job_data.keys())
        values = list(job_data.values())
        placeholders = ','.join(['?'] * len(keys))
        await db.execute(f"INSERT INTO jobs ({','.join(keys)}) VALUES ({placeholders})", values)
        await db.commit()
    return await get_job(job_data['id'])

async def get_job(job_id: str) -> dict:
    async with get_db() as db:
        async with db.execute("SELECT * FROM jobs WHERE id = ?", (job_id,)) as cursor:
            row = await cursor.fetchone()
            if row:
                return dict(row)
            return None

async def list_jobs(type_filter: str = None, status_filter: str = None, limit: int = 20, offset: int = 0) -> list:
    query = "SELECT * FROM jobs WHERE 1=1"
    params = []
    if type_filter:
        query += " AND type = ?"
        params.append(type_filter)
    if status_filter:
        query += " AND status = ?"
        params.append(status_filter)
    query += " ORDER BY created_at DESC LIMIT ? OFFSET ?"
    params.extend([limit, offset])
    
    async with get_db() as db:
        async with db.execute(query, params) as cursor:
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]

async def update_job(job_id: str, updates: dict) -> dict:
    updates['updated_at'] = datetime.datetime.utcnow().isoformat()
    async with get_db() as db:
        set_clauses = [f"{k} = ?" for k in updates.keys()]
        values = list(updates.values())
        values.append(job_id)
        
        await db.execute(f"UPDATE jobs SET {', '.join(set_clauses)} WHERE id = ?", values)
        await db.commit()
    return await get_job(job_id)

async def delete_job(job_id: str):
    async with get_db() as db:
        await db.execute("DELETE FROM jobs WHERE id = ?", (job_id,))
        await db.commit()

async def get_gallery(type_filter: str = None, limit: int = 20, offset: int = 0) -> list:
    query = "SELECT * FROM jobs WHERE status = 'succeeded'"
    params = []
    if type_filter:
        query += " AND type = ?"
        params.append(type_filter)
    query += " ORDER BY created_at DESC LIMIT ? OFFSET ?"
    params.extend([limit, offset])
    
    async with get_db() as db:
        async with db.execute(query, params) as cursor:
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]

async def count_jobs(type_filter: str = None, status_filter: str = None) -> int:
    query = "SELECT COUNT(*) FROM jobs WHERE 1=1"
    params = []
    if type_filter:
        query += " AND type = ?"
        params.append(type_filter)
    if status_filter:
        query += " AND status = ?"
        params.append(status_filter)
    
    async with get_db() as db:
        async with db.execute(query, params) as cursor:
            row = await cursor.fetchone()
            return row[0]
