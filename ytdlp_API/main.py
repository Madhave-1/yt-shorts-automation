import os
import ssl
import uuid
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import yt_dlp

# Disable SSL verification
os.environ['PYTHONHTTPSVERIFY'] = '0'
ssl._create_default_https_context = ssl._create_unverified_context

app = FastAPI(
    title="YT-DLP API Service",
    description="Microservice for downloading YouTube videos",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure temp directory exists
TEMP_DIR = Path("./temp_videos")
TEMP_DIR.mkdir(exist_ok=True)


class DownloadRequest(BaseModel):
    youtube_url: str


class DownloadResponse(BaseModel):
    success: bool
    message: str
    video_id: str = None
    title: str = None
    duration: int = None
    uploader: str = None
    thumbnail: str = None
    description: str = None
    file_path: str = None


@app.get("/")
def root():
    return {
        "service": "YT-DLP API",
        "status": "running",
        "endpoints": {
            "download": "POST /download",
            "health": "GET /health"
        }
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "ytdlp-api",
        "version": "1.0.0"
    }


@app.post("/download", response_model=DownloadResponse)
def download_video(request: DownloadRequest):
    """Download video from YouTube and return metadata"""
    
    try:
        # Generate unique ID
        video_id = str(uuid.uuid4())
        output_path = TEMP_DIR / f"{video_id}.mp4"
        
        # yt-dlp options with SSL bypass
        ydl_opts = {
            'format': 'best[ext=mp4]/best',
            'outtmpl': str(output_path),
            'quiet': True,
            'no_warnings': True,
            'nocheckcertificate': True,
            'no_check_certificate': True,
            'prefer_insecure': True,
            'socket_timeout': 30,
            'retries': 3,
            'legacy_server_connect': True,
            'extractor_args': {
                'youtube': {
                    'player_client': ['android'],
                }
            },
        }
        
        # Download video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(request.youtube_url, download=True)
            
            return DownloadResponse(
                success=True,
                message="Video downloaded successfully",
                video_id=video_id,
                title=info.get('title', 'Unknown'),
                duration=info.get('duration', 0),
                uploader=info.get('uploader', 'Unknown'),
                thumbnail=info.get('thumbnail', ''),
                description=info.get('description', '')[:200] if info.get('description') else '',
                file_path=str(output_path)
            )
            
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Download failed: {str(e)}"
        )


@app.delete("/cleanup/{video_id}")
def cleanup_video(video_id: str):
    """Delete a downloaded video"""
    try:
        file_path = TEMP_DIR / f"{video_id}.mp4"
        if file_path.exists():
            file_path.unlink()
            return {"success": True, "message": "Video deleted"}
        else:
            return {"success": False, "message": "Video not found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8001))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
