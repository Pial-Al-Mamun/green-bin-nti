import asyncio
from fastapi import FastAPI
import uvicorn
from app.routes import router
from app.camera import camera
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        yield
    finally:
        camera.release()
        print("Camera resource released.")


app = FastAPI(lifespan=lifespan)
app.include_router(router)


async def main():
    config = uvicorn.Config(app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped by user.")
