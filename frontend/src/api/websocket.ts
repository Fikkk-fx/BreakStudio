import { useState, useEffect, useRef, useCallback } from 'react';

export function useJobStatus(jobId: string | null) {
  const [status, setStatus] = useState<string | null>(null);
  const [elapsedSeconds, setElapsedSeconds] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [outputUrl, setOutputUrl] = useState<string | null>(null);
  const [outputPath, setOutputPath] = useState<string | null>(null);
  const [isConnected, setIsConnected] = useState<boolean>(false);

  const ws = useRef<WebSocket | null>(null);
  const retries = useRef(0);
  const maxRetries = 5;
  const isTerminal = useRef(false);

  const connect = useCallback(() => {
    if (!jobId || isTerminal.current) return;

    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    // Support external backend via VITE_API_BASE_URL
    const apiBase = import.meta.env.VITE_API_BASE_URL || '';
    const wsBase = apiBase
      ? apiBase.replace(/^https?/, protocol.replace(':', ''))
      : `${protocol}//${window.location.host}`;
    const wsUrl = `${wsBase}/ws/jobs/${jobId}`;

    ws.current = new WebSocket(wsUrl);

    ws.current.onopen = () => {
      setIsConnected(true);
      retries.current = 0;
    };

    ws.current.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        if (data.status) setStatus(data.status);
        if (data.elapsed_seconds !== undefined) setElapsedSeconds(data.elapsed_seconds);
        if (data.error) setError(data.error);
        if (data.output_url) setOutputUrl(data.output_url);
        if (data.output_path) setOutputPath(data.output_path);

        if (['succeeded', 'failed', 'deleted'].includes(data.status)) {
          isTerminal.current = true;
          ws.current?.close();
        }
      } catch (err) {
        console.error('Error parsing WS message', err);
      }
    };

    ws.current.onclose = () => {
      setIsConnected(false);
      // Reconnect if not terminal and within retry limit
      if (!isTerminal.current && retries.current < maxRetries) {
        retries.current += 1;
        setTimeout(connect, 2000 * retries.current);
      }
    };

    ws.current.onerror = (err) => {
      console.error('WebSocket error:', err);
    };
  }, [jobId]);

  useEffect(() => {
    if (!jobId) return;
    isTerminal.current = false;
    retries.current = 0;
    connect();

    return () => {
      isTerminal.current = true;
      ws.current?.close();
    };
  }, [jobId, connect]);

  return { status, elapsedSeconds, error, outputUrl, outputPath, isConnected };
}
