import os
import re
import uuid
import ssl
import certifi
from pathlib import Path
from typing import Dict, Optional

# Disable SSL verification globally for development
os.environ['PYTHONHTTPSVERIFY'] = '0'
os.environ['CURL_CA_BUNDLE'] = ''
os.environ['REQUESTS_CA_BUNDLE'] = ''
ssl._create_default_https_context = ssl._create_unverified_context

import yt_dlp
from config import settings


class VideoDownloadService:
    """Service to handle YouTube video downloads using yt-dlp"""
    
    def __init__(self):
        self.temp_dir = settings.TEMP_VIDEO_DIR
    
    @staticmethod
    def validate_youtube_url(url: str) -> bool:
        """
        Validate if the provided URL is a valid YouTube URL
        
        Args:
            url: URL string to validate
            
        Returns:
            bool: True if valid YouTube URL, False otherwise
        """
        youtube_regex = r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+'
        return bool(re.match(youtube_regex, url))
    
    def download_video(self, youtube_url: str) -> Dict[str, any]:
        """
        Download video from YouTube URL
        
        Args:
            youtube_url: Valid YouTube video URL
            
        Returns:
            Dict containing video information and file path
            
        Raises:
            ValueError: If URL is invalid
            Exception: If download fails
        """
        # Validate URL
        if not self.validate_youtube_url(youtube_url):
            raise ValueError("Invalid YouTube URL provided")
        
        # Generate unique filename
        video_id = str(uuid.uuid4())
        output_path = self.temp_dir / f"{video_id}.mp4"
        
        # Configure yt-dlp options with aggressive SSL bypass
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': str(output_path),
            'quiet': False,
            'no_warnings': False,
            'extract_flat': False,
            # SSL bypass options
            'nocheckcertificate': True,
            'no_check_certificate': True,
            'prefer_insecure': True,
            # Network options
            'source_address': '0.0.0.0',
            'socket_timeout': 30,
            'retries': 3,
            # Legacy SSL support
            'legacy_server_connect': True,
            # Additional options to bypass restrictions
            'extractor_args': {
                'youtube': {
                    'skip': ['dash', 'hls'],
                    'player_skip': ['configs', 'webpage'],
                    'player_client': ['android'],
                }
            },
        }
        
        try:
            # Download video
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                # Extract video info
                info = ydl.extract_info(youtube_url, download=True)
                
                # Prepare response
                result = {
                    'success': True,
                    'video_id': video_id,
                    'file_path': str(output_path),
                    'title': info.get('title', 'Unknown'),
                    'duration': info.get('duration', 0),
                    'uploader': info.get('uploader', 'Unknown'),
                    'thumbnail': info.get('thumbnail', ''),
                    'description': info.get('description', '')[:200] + '...' if info.get('description') else '',
                }
                
                return result
                
        except Exception as e:
            # Clean up partial downloads
            if output_path.exists():
                output_path.unlink()
            
            raise Exception(f"Failed to download video: {str(e)}")
    
    def delete_video(self, file_path: str) -> bool:
        """
        Delete a video file from temp storage
        
        Args:
            file_path: Path to the video file
            
        Returns:
            bool: True if deleted successfully
        """
        try:
            path = Path(file_path)
            if path.exists() and path.is_file():
                path.unlink()
                return True
            return False
        except Exception as e:
            print(f"Error deleting file: {e}")
            return False
    
    def cleanup_old_videos(self, max_age_hours: int = 24):
        """
        Clean up video files older than specified hours
        
        Args:
            max_age_hours: Maximum age of files in hours
        """
        import time
        current_time = time.time()
        max_age_seconds = max_age_hours * 3600
        
        for file_path in self.temp_dir.glob("*.mp4"):
            if file_path.is_file():
                file_age = current_time - file_path.stat().st_mtime
                if file_age > max_age_seconds:
                    try:
                        file_path.unlink()
                        print(f"Deleted old video: {file_path.name}")
                    except Exception as e:
                        print(f"Error deleting {file_path.name}: {e}")


# Singleton instance
video_service = VideoDownloadService()
