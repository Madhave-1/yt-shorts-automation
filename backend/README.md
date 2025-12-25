# AI Podcast Clip Generator - Backend

Backend API for the AI Podcast Clip Generator application.

## Features

- ✅ YouTube video ingestion via yt-dlp
- ✅ URL validation
- ✅ RESTful API with FastAPI
- ✅ Automatic API documentation
- ✅ Video metadata extraction

## Setup

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create environment file:
```bash
cp .env.example .env
```

### Running the Server

```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- API: http://localhost:8000
- Documentation: http://localhost:8000/docs
- Alternative docs: http://localhost:8000/redoc

## API Endpoints

### POST /api/v1/fetch_video
Fetch and download a YouTube video

**Request Body:**
```json
{
  "youtube_url": "https://www.youtube.com/watch?v=VIDEO_ID"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Video downloaded successfully",
  "video_id": "unique-uuid",
  "file_path": "./temp_videos/unique-uuid.mp4",
  "title": "Video Title",
  "duration": 1234,
  "uploader": "Channel Name",
  "thumbnail": "https://...",
  "description": "Video description..."
}
```

### GET /api/v1/health
Health check endpoint

## Project Structure

```
backend/
├── main.py                 # FastAPI application entry point
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── models/
│   ├── __init__.py
│   └── schemas.py        # Pydantic models
├── routes/
│   ├── __init__.py
│   └── video_routes.py   # API route handlers
├── services/
│   ├── __init__.py
│   └── video_downloader.py  # Video download service
└── temp_videos/          # Temporary video storage (auto-created)
```

## Chunk 1 Complete ✅

This implementation includes:
- ✅ YouTube video fetching with yt-dlp
- ✅ URL validation
- ✅ RESTful API endpoint
- ✅ Error handling
- ✅ Automatic documentation
- ✅ Temporary file management

## Next Steps (Future Chunks)

- Chunk 2: Speech-to-Text (Whisper integration)
- Chunk 3: Transcript Chunking
- Chunk 4: Viral Moment Detection (AI Scoring)
- Chunk 5-8: Clip Generation, Captions, Storage
- Chunk 9: Frontend Integration

## Deployment

This backend can be deployed to:
- Railway (Free Tier)
- Render (Free Tier)
- Fly.io (Free Tier)

See deployment guides in the docs folder (coming soon).
