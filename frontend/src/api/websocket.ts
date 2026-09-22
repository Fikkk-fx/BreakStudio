import { useState, useEffect, useRef } from 'react';

export function useJobStatus(jobId: string | null) {
  const [status, setStatus] = useState<string | null>(null);
  const [elapsedSeconds, setElapsedSeconds] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [outputUrl, setOutputUrl] = useState<string | null>(null);
  const [outputPath, setOutputPath] = useState<string | null>(null);
  const [isConnected, setIsConnected] = useState<boolean>(false);

  const ws = useRef<WebSocket | null>(null);
  const retries = useRef(0);
  const maxRetries = 3;

  useEffect(() => {
    if (!jobId) return;

    let isMounted = true;

    const connect = () => {
      const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
      const wsUrl = `${protocol}//${window.location.host}/ws/jobs/${jobId}`;
      
      ws.current = new WebSocket(wsUrl);

      ws.current.onopen = () => {
        if (isMounted) {
          setIsConnected(true);
          retries.current = 0;
        }
      };

      ws.current.onmessage = (event) => {
        if (!isMounted) return;
        try {
          const data = JSON.parse(event.data);
          if (data.status) setStatus(data.status);
          if (data.elapsed_seconds !== undefined) setElapsedSeconds(data.elapsed_seconds);
          if (data.error) setError(data.error);
          if (data.output_url) setOutputUrl(data.output_url);
          if (data.output_path) setOutputPath(data.output_path);

          if (['succeeded', 'failed'].includes(data.status)) {
            ws.current?.close();
          }
        } catch (err) {
          console.error('Error parsing WS message', err);
        }
      };

      ws.current.onclose = () => {
        if (!isMounted) return;
        setIsConnected(false);
        if (status && !['succeeded', 'failed'].includes(status) && retries.current < maxRetries) {
          retries.current += 1;
          setTimeout(connect, 2000);
        }
      };

      ws.current.onerror = (err) => {
        console.error('WebSocket error:', err);
      };
    };

    connect();

    return () => {
      isMounted = false;
      if (ws.current) {
        ws.current.close();
      }
    };
  }, [jobId, status]);

  return { status, elapsedSeconds, error, outputUrl, outputPath, isConnected };
}
