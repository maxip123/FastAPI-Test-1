from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.middleware.custom_headers import add_custom_headers
from app.routes import items, websocket

# Punto de entrada — equivalente al index.js de Node/Express
app = FastAPI()

# --- Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(add_custom_headers)

# --- Eventos del ciclo de vida ---
@app.on_event("startup")
async def startup_event():
    print("Application startup")

@app.on_event("shutdown")
async def shutdown_event():
    print("Application shutdown")

# --- Rutas (equivalente a app.use() en Express) ---
app.include_router(items.router)
app.include_router(websocket.router)