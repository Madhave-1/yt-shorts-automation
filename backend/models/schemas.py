from pydantic import BaseModel, HttpUrl, Field
from typing import Optional


class VideoFetchRequest(BaseModel):
    """Request model for video fetching"""
    youtube_url: str = Field(
        ..., 
        description="YouTube video URL",
        example="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    )


class VideoFetchResponse(BaseModel):
    """Response model for video fetching"""
    success: bool
    message: str
    video_id: Optional[str] = None
    file_path: Optional[str] = None
    title: Optional[str] = None
    duration: Optional[int] = None
    uploader: Optional[str] = None
    thumbnail: Optional[str] = None
    description: Optional[str] = None


class ErrorResponse(BaseModel):
    """Error response model"""
    success: bool = False
    error: str
    detail: Optional[str] = None
