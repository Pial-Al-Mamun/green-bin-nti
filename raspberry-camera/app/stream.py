import asyncio
from typing import AsyncGenerator
from app.camera import camera


async def gen_frames() -> AsyncGenerator[bytes, None]:
    """
    Asynchronous generator for camera frames.
    """
    try:
        while True:
            frame = camera.get_frame()
            if frame:
                yield (b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")
            else:
                break
            await asyncio.sleep(0)
    except (asyncio.CancelledError, GeneratorExit):
        print("Frame generation cancelled.")
    finally:
        print("Frame generator exited.")
