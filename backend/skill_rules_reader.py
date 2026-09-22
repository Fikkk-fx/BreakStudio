"""
BreakStudio — Skill & Rules Reader (Raw UGC Studio Edition)
========================================================================================================
File Python khusus untuk membaca, mem-parse, dan mengekstrak:
  1. SKILL.md — Master Skill (18 Ironclad Mandates, 6-Step Flow, Canonical UGC Architecture)
  2. rules/*.md — Seluruh 44 Modul Specialist Engines UGC

Mengekstrak secara otomatis:
  • Aturan MUTLAK / WAJIB / STRICT / ZERO TOLERANCE
  • 18 Ironclad Production Mandates V20.5 (UGC Edition)
  • Larangan (BANNED / FORBIDDEN / PROHIBITIONS / ❌)
  • Lock Declarations (LOCK / MUST / SHALL / MANDATORY)
  • Negative Prompts & Hardware Locks

Output: Structured JSON report atau formatted terminal display.
========================================================================================================
"""

import re
import os
import sys
import json
import argparse
import glob
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass, field, asdict

# Ensure safe UTF-8 output on Windows consoles
if sys.platform.startswith("win"):
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        if hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


# =============================================================================
# 1. DATA STRUCTURES
# =============================================================================

@dataclass
class ExtractedRule:
    """Represents a single extracted absolute rule."""
    rule_id: str                  # e.g. "MANDAT-01", "LOCK-CAMERA-03", "BAN-SLUGGISH-07"
    category: str                 # MANDAT | LOCK | BAN | MUTLAK | WAJIB | ZERO_TOLERANCE | PROHIBITION
    severity: str                 # FATAL | CRITICAL | WARNING
    source_file: str              # Relative path to source file
    source_line: int              # Approximate line number
    title: str                    # Short title / header
    content: str                  # Full rule text
    keywords: List[str] = field(default_factory=list)  # Matching trigger keywords


@dataclass
class SkillMetadata:
    """Metadata parsed from SKILL.md YAML frontmatter."""
    name: str = ""
    description: str = ""
    version: str = ""


@dataclass
class RulesReport:
    """Complete report of all extracted rules."""
    skill_metadata: SkillMetadata = field(default_factory=SkillMetadata)
    total_files_scanned: int = 0
    total_rules_extracted: int = 0
    rules_by_category: Dict[str, int] = field(default_factory=dict)
    rules: List[ExtractedRule] = field(default_factory=list)
    source_files: List[Dict[str, Any]] = field(default_factory=list)


# =============================================================================
# 2. PATTERN DEFINITIONS — Triggers for Absolute Rules
# =============================================================================

# Regex patterns that signal an absolute/mandatory rule
ABSOLUTE_RULE_TRIGGERS = {
    "MUTLAK": [
        r"(?i)\bMUTLAK\b",
        r"(?i)\bWAJIB\b",
        r"(?i)\bHARUS\b",
        r"(?i)\bDILARANG\b",
    ],
    "MANDATE": [
        r"(?i)\bMandat\s+\d+",
        r"(?i)\bMandate\b",
        r"(?i)\bIronclad\b",
        r"(?i)\bMandatory\b",
        r"(?i)\bMUST\b",
        r"(?i)\bSHALL\b",
        r"(?i)\bREQUIRED\b",
    ],
    "LOCK": [
        r"(?i)\bLOCK(?:ED|S)?\b",
        r"(?i)\bHARD[- ]?LOCK\b",
        r"(?i)\bGLOBAL\s+LOCK\b",
        r"(?i)\bCHARACTER\s+LOCK\b",
        r"(?i)\bCAMERA\s+LOCK\b",
        r"(?i)\bHARDWARE\s+LOCK\b",
        r"(?i)\bBIOMETRIC\s+LOCK\b",
    ],
    "BAN": [
        r"(?i)\bBANNED?\b",
        r"(?i)\bFORBIDDEN\b",
        r"(?i)\bPROHIBIT(?:ED|ION|IONS)?\b",
        r"(?i)\bPURGE[D]?\b",
        r"(?i)\bBLACKLIST(?:ED)?\b",
    ],
    "ZERO_TOLERANCE": [
        r"(?i)\bZERO\s+TOLERANCE\b",
        r"(?i)\bSTRICTLY?\s+(?:0%|ZERO)\b",
        r"(?i)\b100%\s+(?:PURGE|BAN|FORBIDDEN)\b",
        r"(?i)\bABSOLUTE(?:LY)?\s+(?:ZERO|0%|NO|NEVER)\b",
        r"(?i)\bFATAL\b",
        r"(?i)\bNON[- ]NEGOTIABLE\b",
    ],
    "PROHIBITION": [
        r"(?i)❌\s*(?:Do\s+NOT|NEVER|JANGAN|DILARANG)",
        r"(?i)\bDo\s+NOT\s+use\b",
        r"(?i)\bNEVER\s+(?:use|allow|permit|leave|place)\b",
        r"(?i)\bSTRICTLY\s+(?:NO|ZERO|0%)\b",
        r"(?i)\b0%\s+\w+",
    ],
    "STRICT": [
        r"(?i)\bSTRICT(?:LY)?\b",
        r"(?i)\bINVARIANT\b",
        r"(?i)\bIMMUTABLE\b",
        r"(?i)\bSSOT\b",
        r"(?i)\bCANONICAL\b",
    ],
}

# Severity mapping
SEVERITY_MAP = {
    "MUTLAK": "FATAL",
    "ZERO_TOLERANCE": "FATAL",
    "BAN": "FATAL",
    "PROHIBITION": "FATAL",
    "MANDATE": "CRITICAL",
    "LOCK": "CRITICAL",
    "STRICT": "WARNING",
}


# =============================================================================
# 3. PARSING FUNCTIONS
# =============================================================================

def parse_yaml_frontmatter(content: str) -> SkillMetadata:
    """Extract YAML frontmatter from SKILL.md."""
    meta = SkillMetadata()
    fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if fm_match:
        fm_text = fm_match.group(1)
        name_m = re.search(r"^name:\s*(.+)$", fm_text, re.MULTILINE)
        desc_m = re.search(r"^description:\s*>-\s*\n((?:\s{2,}.+\n?)+)", fm_text, re.MULTILINE)
        if not desc_m:
            desc_m = re.search(r"^description:\s*(.+)$", fm_text, re.MULTILINE)
        if name_m:
            meta.name = name_m.group(1).strip()
        if desc_m:
            meta.description = " ".join(desc_m.group(1).strip().split())
        # Try to extract version from name or content
        ver_m = re.search(r"V(\d+\.\d+)", content[:500])
        if ver_m:
            meta.version = ver_m.group(1)
    return meta


def extract_section_context(lines: List[str], line_idx: int, context_radius: int = 5) -> Tuple[str, str]:
    """
    Extract the nearest heading (title) and a context block around the matched line.
    Returns (section_title, context_text).
    """
    # Walk backwards to find nearest heading
    title = ""
    for i in range(line_idx, max(line_idx - 30, -1), -1):
        if i < 0:
            break
        line = lines[i].strip()
        # Match markdown headings or numbered mandate headers
        if re.match(r"^#{1,6}\s+", line):
            title = re.sub(r"^#{1,6}\s+", "", line).strip()
            break
        mandat_m = re.match(r"^\d+\.\s+\*\*Mandat\s+\d+.*?\*\*", line, re.IGNORECASE)
        if mandat_m:
            title = re.sub(r"\*\*", "", mandat_m.group(0)).strip()
            break

    # Gather context lines
    start = max(0, line_idx - context_radius)
    end = min(len(lines), line_idx + context_radius + 1)
    context_lines = lines[start:end]
    context_text = "\n".join(l.rstrip() for l in context_lines)

    return title, context_text


def scan_file_for_rules(
    filepath: str,
    base_dir: str,
    rule_counter: Dict[str, int]
) -> List[ExtractedRule]:
    """Scan a single markdown file for absolute rules."""
    rules = []
    rel_path = os.path.relpath(filepath, base_dir)

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"  [!] Error reading {rel_path}: {e}", file=sys.stderr)
        return rules

    lines = content.split("\n")

    # Track already-captured line ranges to avoid duplicates
    captured_ranges = set()

    for category, patterns in ABSOLUTE_RULE_TRIGGERS.items():
        for pattern in patterns:
            for match in re.finditer(pattern, content):
                # Find line number
                line_start = content[:match.start()].count("\n")

                # Check if this line was already captured (within ±2 lines)
                range_key = (category, line_start // 3)  # group nearby lines
                if range_key in captured_ranges:
                    continue
                captured_ranges.add(range_key)

                # Extract context
                title, context_text = extract_section_context(lines, line_start)
                if not title:
                    title = lines[line_start].strip()[:120]

                # Clean title from markdown formatting
                title = re.sub(r"[\*\_\[\]`#]", "", title).strip()
                title = re.sub(r"\s+", " ", title)
                if len(title) > 150:
                    title = title[:147] + "..."

                # Generate rule ID
                rule_counter[category] = rule_counter.get(category, 0) + 1
                rule_id = f"{category}-{rule_counter[category]:03d}"

                # Detect matched keywords
                matched_keywords = []
                for kw_pattern in patterns:
                    kw_matches = re.findall(kw_pattern, lines[line_start] if line_start < len(lines) else "")
                    matched_keywords.extend(kw_matches)
                matched_keywords = list(set(matched_keywords))[:5]

                rule = ExtractedRule(
                    rule_id=rule_id,
                    category=category,
                    severity=SEVERITY_MAP.get(category, "WARNING"),
                    source_file=rel_path.replace("\\", "/"),
                    source_line=line_start + 1,
                    title=title,
                    content=context_text.strip(),
                    keywords=matched_keywords,
                )
                rules.append(rule)

    return rules


def extract_ironclad_mandates(skill_content: str) -> List[Dict[str, str]]:
    """Extract the 18 Ironclad Production Mandates specifically from SKILL.md."""
    mandates = []
    # Match numbered mandates: "1. **Mandat 1: Title:**"
    pattern = r"(\d+)\.\s+\*\*Mandat\s+(\d+):\s*(.*?)\*\*\s*\n((?:.*?\n)*?)(?=\n\d+\.\s+\*\*Mandat|\n---|\n##|\Z)"
    for m in re.finditer(pattern, skill_content, re.MULTILINE):
        num = m.group(2)
        title = m.group(3).strip().rstrip(":")
        body = m.group(4).strip()
        # Clean markdown
        body = re.sub(r"\s+", " ", body)
        body = re.sub(r"[\*`]", "", body)
        mandates.append({
            "mandat_number": int(num),
            "title": title,
            "full_text": body,
        })
    return mandates


def extract_prohibitions(content: str) -> List[str]:
    """Extract explicit prohibition lines (❌ / Do NOT / NEVER / DILARANG)."""
    prohibitions = []
    lines = content.split("\n")
    for line in lines:
        stripped = line.strip()
        if re.match(r"❌|^\*?\s*❌", stripped):
            prohibitions.append(re.sub(r"^[\*\s]*❌\s*", "", stripped).strip())
        elif re.match(r"(?i)^\s*(?:\*\s+)?(?:Do NOT|NEVER|STRICTLY NO|DILARANG|JANGAN)", stripped):
            prohibitions.append(stripped.lstrip("* ").strip())
    return list(dict.fromkeys(prohibitions))  # deduplicate while preserving order


def extract_negative_prompt(content: str) -> Optional[str]:
    """Extract the master negative prompt block from SKILL.md."""
    # Look for the negative prompt code block
    neg_match = re.search(
        r"(?:NEGATIVE PROMPT|HARDWARE LOCK|NEGATIVE FILTER).*?```(?:text)?\s*\n(.*?)```",
        content, re.DOTALL | re.IGNORECASE
    )
    if neg_match:
        return neg_match.group(1).strip()
    return None


# =============================================================================
# 4. MAIN READER ENGINE
# =============================================================================

def read_skills_and_rules(
    base_dir: str,
    categories: Optional[List[str]] = None,
    search_query: Optional[str] = None,
    severity_filter: Optional[str] = None,
) -> RulesReport:
    """
    Main engine: reads SKILL.md + all rules/*.md and builds a complete report.

    Args:
        base_dir: Root directory containing SKILL.md and rules/
        categories: Filter by categories (e.g., ["MUTLAK", "BAN", "MANDATE"])
        search_query: Free-text search within rule titles and content
        severity_filter: Filter by severity ("FATAL", "CRITICAL", "WARNING")
    """
    report = RulesReport()

    skill_path = os.path.join(base_dir, "SKILL.md")
    rules_dir = os.path.join(base_dir, "rules")

    # --- 1. Parse SKILL.md ---
    if os.path.isfile(skill_path):
        with open(skill_path, "r", encoding="utf-8") as f:
            skill_content = f.read()
        report.skill_metadata = parse_yaml_frontmatter(skill_content)
        report.source_files.append({
            "file": "SKILL.md",
            "size_bytes": os.path.getsize(skill_path),
            "type": "master_skill",
        })
    else:
        print(f"[!] SKILL.md not found in {base_dir}", file=sys.stderr)
        skill_content = ""

    # --- 2. Discover all rules/*.md ---
    rule_files = []
    if os.path.isdir(rules_dir):
        rule_files = sorted(glob.glob(os.path.join(rules_dir, "*.md")))
        for rf in rule_files:
            report.source_files.append({
                "file": os.path.relpath(rf, base_dir).replace("\\", "/"),
                "size_bytes": os.path.getsize(rf),
                "type": "rule_module",
            })

    all_files = []
    if os.path.isfile(skill_path):
        all_files.append(skill_path)
    all_files.extend(rule_files)

    report.total_files_scanned = len(all_files)

    # --- 3. Scan all files for absolute rules ---
    rule_counter: Dict[str, int] = {}
    all_rules: List[ExtractedRule] = []

    for filepath in all_files:
        file_rules = scan_file_for_rules(filepath, base_dir, rule_counter)
        all_rules.extend(file_rules)

    # --- 4. Apply filters ---
    if categories:
        cats_upper = [c.upper() for c in categories]
        all_rules = [r for r in all_rules if r.category in cats_upper]

    if severity_filter:
        sev = severity_filter.upper()
        all_rules = [r for r in all_rules if r.severity == sev]

    if search_query:
        q = search_query.lower()
        all_rules = [
            r for r in all_rules
            if q in r.title.lower() or q in r.content.lower()
        ]

    # --- 5. Deduplicate by content similarity ---
    seen_hashes = set()
    deduped_rules = []
    for rule in all_rules:
        # Use first 80 chars of content + source file as dedup key
        content_key = (rule.source_file, rule.content[:80].strip().lower())
        if content_key not in seen_hashes:
            seen_hashes.add(content_key)
            deduped_rules.append(rule)
    all_rules = deduped_rules

    # --- 6. Build report ---
    report.rules = all_rules
    report.total_rules_extracted = len(all_rules)

    cat_counts: Dict[str, int] = {}
    for r in all_rules:
        cat_counts[r.category] = cat_counts.get(r.category, 0) + 1
    report.rules_by_category = cat_counts

    return report


# =============================================================================
# 5. DISPLAY FORMATTERS
# =============================================================================

SEVERITY_COLORS = {
    "FATAL":    "\033[91m",   # Red
    "CRITICAL": "\033[93m",   # Yellow
    "WARNING":  "\033[96m",   # Cyan
}
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"


def print_terminal_report(report: RulesReport, verbose: bool = False):
    """Pretty-print the report to terminal with colors."""

    print()
    print(f"{BOLD}{'='*90}{RESET}")
    print(f"{BOLD}  🎬 BREAKSTUDIO V{report.skill_metadata.version} — SKILL & ATURAN MUTLAK READER{RESET}")
    print(f"{BOLD}{'='*90}{RESET}")
    print(f"  Skill Name     : {report.skill_metadata.name}")
    print(f"  Files Scanned  : {report.total_files_scanned}")
    print(f"  Rules Extracted : {report.total_rules_extracted}")
    print()

    # Category breakdown
    print(f"  {BOLD}📊 BREAKDOWN PER KATEGORI:{RESET}")
    for cat, count in sorted(report.rules_by_category.items(), key=lambda x: -x[1]):
        sev = SEVERITY_MAP.get(cat, "WARNING")
        color = SEVERITY_COLORS.get(sev, "")
        print(f"    {color}■ {cat:<20} : {count:>4} aturan  [{sev}]{RESET}")
    print()

    # Rules grouped by source file
    print(f"  {BOLD}📋 DAFTAR ATURAN MUTLAK:{RESET}")
    print(f"  {'─'*86}")

    current_file = ""
    for i, rule in enumerate(report.rules, 1):
        if rule.source_file != current_file:
            current_file = rule.source_file
            print(f"\n  {BOLD}📄 {current_file}{RESET}")
            print(f"  {'─'*86}")

        sev = rule.severity
        color = SEVERITY_COLORS.get(sev, "")

        print(f"  {color}[{rule.rule_id}] [{sev}]{RESET} {rule.title[:80]}")
        print(f"  {DIM}   Line {rule.source_line} | Keywords: {', '.join(rule.keywords[:3]) or '-'}{RESET}")

        if verbose:
            # Show truncated content
            content_preview = rule.content.replace("\n", " ")[:200]
            print(f"  {DIM}   → {content_preview}...{RESET}")

    print(f"\n  {'='*90}")
    print(f"  {BOLD}✅ Total: {report.total_rules_extracted} aturan mutlak diekstrak dari {report.total_files_scanned} file{RESET}")
    print(f"  {'='*90}\n")


def print_mandates_summary(base_dir: str):
    """Print a focused summary of just the 18 Ironclad Mandates."""
    skill_path = os.path.join(base_dir, "SKILL.md")
    if not os.path.isfile(skill_path):
        print("[!] SKILL.md not found.", file=sys.stderr)
        return

    with open(skill_path, "r", encoding="utf-8") as f:
        content = f.read()

    mandates = extract_ironclad_mandates(content)

    print()
    print(f"{BOLD}{'='*90}{RESET}")
    print(f"{BOLD}  🛡️  THE 18 IRONCLAD PRODUCTION MANDATES V20.5{RESET}")
    print(f"{BOLD}{'='*90}{RESET}")

    for m in mandates:
        print(f"\n  {BOLD}Mandat {m['mandat_number']:>2}:{RESET} {m['title']}")
        # Wrap text at ~85 chars
        text = m["full_text"]
        words = text.split()
        line = "    "
        for w in words:
            if len(line) + len(w) + 1 > 88:
                print(f"  {DIM}{line}{RESET}")
                line = "    "
            line += w + " "
        if line.strip():
            print(f"  {DIM}{line}{RESET}")

    print(f"\n  {'='*90}")
    print(f"  {BOLD}Total: {len(mandates)} Ironclad Mandates{RESET}")
    print(f"  {'='*90}\n")


def print_prohibitions_summary(base_dir: str):
    """Print all explicit prohibitions across SKILL.md and rules."""
    all_prohibitions = []

    # Scan SKILL.md
    skill_path = os.path.join(base_dir, "SKILL.md")
    if os.path.isfile(skill_path):
        with open(skill_path, "r", encoding="utf-8") as f:
            content = f.read()
        proh = extract_prohibitions(content)
        for p in proh:
            all_prohibitions.append(("SKILL.md", p))

        # Also extract negative prompt
        neg = extract_negative_prompt(content)
        if neg:
            for token in neg.split(","):
                token = token.strip()
                if token:
                    all_prohibitions.append(("SKILL.md [NEGATIVE PROMPT]", token))

    # Scan rules
    rules_dir = os.path.join(base_dir, "rules")
    if os.path.isdir(rules_dir):
        for rf in sorted(glob.glob(os.path.join(rules_dir, "*.md"))):
            rel = os.path.relpath(rf, base_dir).replace("\\", "/")
            with open(rf, "r", encoding="utf-8") as f:
                content = f.read()
            proh = extract_prohibitions(content)
            for p in proh:
                all_prohibitions.append((rel, p))

    print()
    print(f"{BOLD}{'='*90}{RESET}")
    print(f"{BOLD}  🚫 DAFTAR LENGKAP LARANGAN & PROHIBITIONS{RESET}")
    print(f"{BOLD}{'='*90}{RESET}")

    current_file = ""
    for source, text in all_prohibitions:
        if source != current_file:
            current_file = source
            print(f"\n  {BOLD}📄 {source}{RESET}")
        print(f"    {SEVERITY_COLORS['FATAL']}❌{RESET} {text[:120]}")

    print(f"\n  {'='*90}")
    print(f"  {BOLD}Total: {len(all_prohibitions)} larangan eksplisit{RESET}")
    print(f"  {'='*90}\n")


# =============================================================================
# 6. JSON EXPORT
# =============================================================================

def export_to_json(report: RulesReport) -> str:
    """Export the full report as JSON."""
    data = {
        "skill_metadata": asdict(report.skill_metadata),
        "summary": {
            "total_files_scanned": report.total_files_scanned,
            "total_rules_extracted": report.total_rules_extracted,
            "rules_by_category": report.rules_by_category,
        },
        "source_files": report.source_files,
        "rules": [asdict(r) for r in report.rules],
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


# =============================================================================
# 7. CLI INTERFACE
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="BreakStudio — Pembaca Skills & Aturan Mutlak",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Contoh Penggunaan:
  python skill_rules_reader.py                          # Baca semua aturan mutlak
  python skill_rules_reader.py --mandates               # Tampilkan 18 Ironclad Mandates saja
  python skill_rules_reader.py --prohibitions           # Tampilkan semua larangan
  python skill_rules_reader.py --category MUTLAK BAN    # Filter kategori tertentu
  python skill_rules_reader.py --severity FATAL          # Hanya aturan FATAL
  python skill_rules_reader.py --search "camera"         # Cari kata kunci
  python skill_rules_reader.py --json                    # Output JSON
  python skill_rules_reader.py --json --output report.json  # Export ke file JSON
  python skill_rules_reader.py --verbose                 # Tampilkan konten detail
        """
    )
    parser.add_argument("--dir", type=str, default=None,
                        help="Root directory (default: directory containing this script)")
    parser.add_argument("--mandates", action="store_true",
                        help="Tampilkan 18 Ironclad Production Mandates saja")
    parser.add_argument("--prohibitions", action="store_true",
                        help="Tampilkan semua larangan eksplisit (❌ / Do NOT / BANNED)")
    parser.add_argument("--category", nargs="+", type=str, default=None,
                        help="Filter kategori: MUTLAK, MANDATE, LOCK, BAN, ZERO_TOLERANCE, PROHIBITION, STRICT")
    parser.add_argument("--severity", type=str, default=None,
                        help="Filter severity: FATAL, CRITICAL, WARNING")
    parser.add_argument("--search", type=str, default=None,
                        help="Cari kata kunci di dalam title/content aturan")
    parser.add_argument("--json", action="store_true",
                        help="Output hasil sebagai JSON")
    parser.add_argument("--output", type=str, default=None,
                        help="Path file output untuk export JSON (gunakan bersama --json)")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Tampilkan preview konten setiap aturan")
    parser.add_argument("--stats", action="store_true",
                        help="Tampilkan statistik file rules saja")

    args = parser.parse_args()

    # Determine base directory
    if args.dir:
        base_dir = os.path.abspath(args.dir)
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))

    if not os.path.isdir(base_dir):
        print(f"[!] Directory not found: {base_dir}", file=sys.stderr)
        sys.exit(1)

    # --- Stats mode ---
    if args.stats:
        print(f"\n{BOLD}📁 FILE STATISTICS — {base_dir}{RESET}\n")
        skill_path = os.path.join(base_dir, "SKILL.md")
        if os.path.isfile(skill_path):
            size = os.path.getsize(skill_path)
            with open(skill_path, "r", encoding="utf-8") as f:
                lines = len(f.readlines())
            print(f"  SKILL.md : {size:>8,} bytes | {lines:>5,} lines")

        rules_dir = os.path.join(base_dir, "rules")
        total_size = 0
        total_lines = 0
        if os.path.isdir(rules_dir):
            rule_files = sorted(glob.glob(os.path.join(rules_dir, "*.md")))
            for rf in rule_files:
                size = os.path.getsize(rf)
                with open(rf, "r", encoding="utf-8") as f:
                    lines = len(f.readlines())
                total_size += size
                total_lines += lines
                rel = os.path.relpath(rf, base_dir).replace("\\", "/")
                print(f"  {rel:<65} : {size:>8,} bytes | {lines:>5,} lines")
            print(f"\n  {'─'*90}")
            print(f"  {BOLD}TOTAL rules/ : {total_size:>10,} bytes | {total_lines:>6,} lines | {len(rule_files)} files{RESET}")
        print()
        sys.exit(0)

    # --- Mandates mode ---
    if args.mandates:
        print_mandates_summary(base_dir)
        sys.exit(0)

    # --- Prohibitions mode ---
    if args.prohibitions:
        print_prohibitions_summary(base_dir)
        sys.exit(0)

    # --- Full scan ---
    print(f"\n{DIM}[*] Scanning {base_dir} ...{RESET}")
    report = read_skills_and_rules(
        base_dir=base_dir,
        categories=args.category,
        search_query=args.search,
        severity_filter=args.severity,
    )

    if args.json:
        json_output = export_to_json(report)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(json_output)
            print(f"[+] JSON report exported to: {args.output}")
        else:
            print(json_output)
    else:
        print_terminal_report(report, verbose=args.verbose)


if __name__ == "__main__":
    main()
