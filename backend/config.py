import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    # Server Configuration
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8000))
    
    # Storage Configuration
    TEMP_VIDEO_DIR: Path = Path(os.getenv("TEMP_VIDEO_DIR", "./temp_videos"))
    
    # API Configuration
    API_PREFIX: str = os.getenv("API_PREFIX", "/api/v1")
    
    # External YT-DLP API (deployed separately)
    YTDLP_API_URL: str = os.getenv("YTDLP_API_URL", "http://localhost:8001")
    
    # Video Download Configuration
    MAX_VIDEO_DURATION: int = 7200  # 2 hours in seconds
    ALLOWED_VIDEO_FORMATS: list = ["mp4", "webm"]
    
    def __init__(self):
        # Create temp directory if it doesn't exist
        self.TEMP_VIDEO_DIR.mkdir(parents=True, exist_ok=True)

settings = Settings()
