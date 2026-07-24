from typing import Callable
from fastapi import Request

# Equivalente a un middleware de Express: (req, res, next) => { ... }
async def add_custom_headers(request: Request, call_next: Callable):
    response = await call_next(request)
    response.headers["X-Custom-Header"] = "My-Value"
    return response
