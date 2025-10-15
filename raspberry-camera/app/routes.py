from fastapi import APIRouter, Response
from fastapi.responses import StreamingResponse
from typing import Never
from app.stream import gen_frames
from app.camera import camera

router = APIRouter()


@router.get("/video")
async def video_feed() -> StreamingResponse:
    return StreamingResponse(
        gen_frames(), media_type="multipart/x-mixed-replace; boundary=frame"
    )


@router.get("/snapshot")
async def snapshot() -> Response:
    frame = camera.get_frame()  # Optional: use shared camera instead
    if frame:
        return Response(content=frame, media_type="image/jpeg")
    return Response(status_code=404, content="Camera frame not available.")


@router.get("/exit")
async def close() -> Never:
    raise KeyboardInterrupt
