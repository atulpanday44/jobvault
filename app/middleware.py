from fastapi import FastAPI, Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.errors import ServerErrorMiddleware
import time

class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI, max_requests: int, time_window: int):
        super().__init__(app)
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = {}

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        current_time = time.time()
        if client_ip not in self.requests:
            self.requests[client_ip] = []

        # Remove outdated requests
        self.requests[client_ip] = [timestamp for timestamp in self.requests[client_ip] if timestamp > current_time - self.time_window]

        if len(self.requests[client_ip]) >= self.max_requests:
            raise HTTPException(status_code=429, detail="Rate limit exceeded")

        # Log the request time
        self.requests[client_ip].append(current_time)

        response = await call_next(request)
        return response

app = FastAPI()

# Enable error handling middleware
app.add_middleware(ServerErrorMiddleware)

# Add rate limiting middleware (e.g., 5 requests per 60 seconds)
app.add_middleware(RateLimitMiddleware, max_requests=5, time_window=60)