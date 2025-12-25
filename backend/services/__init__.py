"""Services package initialization"""
import os

# Choose which video service to use
USE_EXTERNAL_API = os.getenv("USE_EXTERNAL_API", "false").lower() == "true"

if USE_EXTERNAL_API:
    from .video_downloader_api import video_service
    print("✅ Using External YT-DLP API")
else:
    from .video_downloader import video_service
    print("✅ Using Local YT-DLP")

__all__ = ['video_service']
