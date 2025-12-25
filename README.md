# 🎬 AI Podcast Clip Generator

Transform long YouTube videos into viral short clips using AI. Built with free and open-source technologies.

## ✨ Features (Chunk 1 Complete)

- ✅ YouTube video ingestion via URL
- ✅ Automatic video download and processing
- ✅ Video metadata extraction
- ✅ Modern web interface
- ✅ RESTful API architecture

## 🏗️ Project Structure

```
yt-shorts-automation/
├── backend/           # FastAPI Python backend
│   ├── main.py
│   ├── config.py
│   ├── models/
│   ├── routes/
│   └── services/
└── frontend/          # Next.js React frontend
    ├── src/
    │   ├── app/
    │   ├── components/
    │   └── services/
    └── package.json
```

## 🚀 Quick Start

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
```

3. Activate virtual environment:
```bash
# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Copy environment file:
```bash
cp .env.example .env
```

6. Run the server:
```bash
python main.py
```

Backend will be available at: http://localhost:8000

API Documentation: http://localhost:8000/docs

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Copy environment file:
```bash
cp .env.example .env
```

4. Run development server:
```bash
npm run dev
```

Frontend will be available at: http://localhost:3000

## 🎯 Usage

1. Start both backend and frontend servers
2. Open http://localhost:3000 in your browser
3. Paste a YouTube video URL
4. Click "Fetch Video"
5. View video information and metadata

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **yt-dlp** - YouTube video downloader
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

### Frontend
- **Next.js 14** - React framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **Axios** - HTTP client

## 📋 Roadmap

### ✅ Chunk 1: Video Ingestion (COMPLETE)
- YouTube URL input
- Video download and storage
- Metadata extraction
- Basic web interface

### 🔜 Upcoming Chunks

- **Chunk 2**: Speech-to-Text (Whisper integration)
- **Chunk 3**: Transcript Chunking
- **Chunk 4**: Viral Moment Detection (AI Scoring)
- **Chunk 5**: Clip Generation (FFmpeg)
- **Chunk 6**: Vertical Conversion
- **Chunk 7**: Auto Captions
- **Chunk 8**: Cloud Storage
- **Chunk 9**: Enhanced Frontend
- **Chunk 10**: Full Orchestration

## 🎨 API Endpoints

### POST /api/v1/fetch_video
Fetch and download a YouTube video

**Request:**
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

## 🌟 Free Deployment Options

### Backend
- Railway (Free Tier)
- Render (Free Tier)
- Fly.io (Free Tier)

### Frontend
- Vercel (Free)
- Netlify (Free)
- Cloudflare Pages (Free)

## 📝 Development

### Running Backend Tests
```bash
cd backend
pytest
```

### Building Frontend for Production
```bash
cd frontend
npm run build
npm start
```

## 🤝 Contributing

This is a learning project following the MVP roadmap. Each chunk builds upon the previous one.

## 📄 License

MIT License - feel free to use this project for learning and experimentation.

## 🎓 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Next.js Documentation](https://nextjs.org/docs)
- [yt-dlp Documentation](https://github.com/yt-dlp/yt-dlp)
- [Tailwind CSS](https://tailwindcss.com/)

## � Documentation

We've created comprehensive documentation to help you:

- **[🏗️ Architecture](ARCHITECTURE.md)** - System design, data flow, tech stack diagrams
- **[📊 Development Tracker](DEVELOPMENT.md)** - Progress, roadmap, and metrics
- **[🧪 Testing Guide](TESTING.md)** - Test scenarios, debugging, and validation
- **[🔧 Troubleshooting](TROUBLESHOOTING.md)** - Common issues and solutions
- **[📁 File Structure](FILE_STRUCTURE.md)** - Complete directory tree and file descriptions
- **[⚡ Quick Reference](QUICK_REFERENCE.md)** - Handy command cheat sheet
- **[🎉 Chunk 1 Summary](CHUNK1_COMPLETE.md)** - What we accomplished and next steps

## �📞 Support

For issues or questions, please open an issue in the repository.

---

**Status:** Chunk 1 Complete ✅ | Ready for Chunk 2 🚀
