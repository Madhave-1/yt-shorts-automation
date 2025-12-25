import requests
from typing import Dict
from config import settings


class VideoDownloadService:
    """Service to download videos using external YT-DLP API"""
    
    def __init__(self):
        self.api_url = settings.YTDLP_API_URL
    
    @staticmethod
    def validate_youtube_url(url: str) -> bool:
        """Validate if the provided URL is a valid YouTube URL"""
        import re
        youtube_regex = r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+'
        return bool(re.match(youtube_regex, url))
    
    def download_video(self, youtube_url: str) -> Dict[str, any]:
        """
        Download video using external YT-DLP API
        
        Args:
            youtube_url: Valid YouTube video URL
            
        Returns:
            Dict containing video information
            
        Raises:
            ValueError: If URL is invalid
            Exception: If download fails
        """
        # Validate URL
        if not self.validate_youtube_url(youtube_url):
            raise ValueError("Invalid YouTube URL provided")
        
        try:
            # Call external YT-DLP API
            response = requests.post(
                f"{self.api_url}/download",
                json={"youtube_url": youtube_url},
                timeout=120  # 2 minutes timeout for large videos
            )
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'success': data.get('success', False),
                    'video_id': data.get('video_id'),
                    'file_path': data.get('file_path'),
                    'title': data.get('title', 'Unknown'),
                    'duration': data.get('duration', 0),
                    'uploader': data.get('uploader', 'Unknown'),
                    'thumbnail': data.get('thumbnail', ''),
                    'description': data.get('description', ''),
                }
            else:
                error_detail = response.json().get('detail', 'Unknown error')
                raise Exception(f"API returned error: {error_detail}")
                
        except requests.Timeout:
            raise Exception("Download timeout - video might be too large")
        except requests.ConnectionError:
            raise Exception(f"Cannot connect to YT-DLP API at {self.api_url}")
        except Exception as e:
            raise Exception(f"Failed to download video: {str(e)}")
    
    def cleanup_video(self, video_id: str) -> bool:
        """
        Delete a video from the YT-DLP API server
        
        Args:
            video_id: Video ID to delete
            
        Returns:
            bool: True if deleted successfully
        """
        try:
            response = requests.delete(
                f"{self.api_url}/cleanup/{video_id}",
                timeout=10
            )
            if response.status_code == 200:
                return response.json().get('success', False)
            return False
        except Exception as e:
            print(f"Error cleaning up video: {e}")
            return False


# Singleton instance
video_service = VideoDownloadService()
