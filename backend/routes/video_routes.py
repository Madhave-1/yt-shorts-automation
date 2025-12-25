from fastapi import APIRouter, HTTPException, status
from models import VideoFetchRequest, VideoFetchResponse, ErrorResponse
from services import video_service

router = APIRouter()


@router.post(
    "/fetch_video",
    response_model=VideoFetchResponse,
    status_code=status.HTTP_200_OK,
    summary="Fetch YouTube Video",
    description="Download a YouTube video and prepare it for processing"
)
async def fetch_video(request: VideoFetchRequest):
    """
    Endpoint to fetch and download a YouTube video
    
    - **youtube_url**: Valid YouTube video URL
    
    Returns video information and file path
    """
    try:
        # Download video using the service
        result = video_service.download_video(request.youtube_url)
        
        return VideoFetchResponse(
            success=True,
            message="Video downloaded successfully",
            video_id=result['video_id'],
            file_path=result['file_path'],
            title=result['title'],
            duration=result['duration'],
            uploader=result['uploader'],
            thumbnail=result['thumbnail'],
            description=result['description']
        )
        
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to download video: {str(e)}"
        )


@router.get(
    "/health",
    summary="Health Check",
    description="Check if the API is running"
)
async def health_check():
    """Simple health check endpoint"""
    return {
        "status": "healthy",
        "service": "video-ingestion",
        "version": "1.0.0"
    }
