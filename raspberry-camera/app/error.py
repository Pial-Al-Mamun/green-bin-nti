from fastapi import HTTPException


CameraNotFoundError = HTTPException(
    status_code=400, detail="Camera frame not available"
)
