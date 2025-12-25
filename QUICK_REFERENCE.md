# 🚀 Quick Reference Card

## ⚡ Common Commands

### Setup (First Time Only)
```bash
# Automated setup (Windows)
setup.bat

# Manual setup
cd backend && python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt && cd ../frontend && npm install
```

### Start Application
```bash
# Automated start (Windows)
start.bat

# Manual start - Terminal 1 (Backend)
cd backend
venv\Scripts\activate
python main.py

# Manual start - Terminal 2 (Frontend)
cd frontend
npm run dev
```

### Stop Application
```
Ctrl + C in both terminals
```

---

## 🌐 URLs

| Service | URL | Description |
|---------|-----|-------------|
| Frontend | http://localhost:3000 | Main web interface |
| Backend API | http://localhost:8000 | API base URL |
| API Docs | http://localhost:8000/docs | Interactive API documentation |
| API Redoc | http://localhost:8000/redoc | Alternative API docs |
| Health Check | http://localhost:8000/api/v1/health | Server health status |

---

## 📁 Important Files

### Backend
| File | Purpose |
|------|---------|
| `backend/main.py` | App entry point |
| `backend/config.py` | Settings |
| `backend/services/video_downloader.py` | Download logic |
| `backend/routes/video_routes.py` | API endpoints |
| `backend/.env` | Environment variables |

### Frontend
| File | Purpose |
|------|---------|
| `frontend/src/app/page.tsx` | Home page |
| `frontend/src/components/VideoFetcher.tsx` | Main component |
| `frontend/src/services/api.ts` | API calls |
| `frontend/.env` | Environment variables |

---

## 🔧 Configuration

### Backend Environment (.env)
```bash
HOST=0.0.0.0
PORT=8000
TEMP_VIDEO_DIR=./temp_videos
API_PREFIX=/api/v1
```

### Frontend Environment (.env)
```bash
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
```

---

## 🛠️ Development Commands

### Backend
```bash
# Activate virtual environment
cd backend
venv\Scripts\activate

# Install package
pip install package-name

# Update requirements
pip freeze > requirements.txt

# Run server
python main.py

# Run with custom port
uvicorn main:app --port 8001
```

### Frontend
```bash
# Install package
npm install package-name

# Development server
npm run dev

# Build for production
npm run build

# Start production server
npm start

# Lint code
npm run lint
```

---

## 📡 API Endpoints

### POST /api/v1/fetch_video
```bash
# Using curl
curl -X POST http://localhost:8000/api/v1/fetch_video \
  -H "Content-Type: application/json" \
  -d '{"youtube_url": "https://www.youtube.com/watch?v=VIDEO_ID"}'

# Using Python
import requests
response = requests.post(
    "http://localhost:8000/api/v1/fetch_video",
    json={"youtube_url": "https://www.youtube.com/watch?v=VIDEO_ID"}
)

# Using JavaScript
fetch('http://localhost:8000/api/v1/fetch_video', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ youtube_url: 'https://www.youtube.com/watch?v=VIDEO_ID' })
})
```

### GET /api/v1/health
```bash
curl http://localhost:8000/api/v1/health
```

---

## 🐛 Quick Debugging

### Backend not starting?
```bash
# Check Python version
python --version  # Should be 3.8+

# Check if port is in use
netstat -ano | findstr :8000

# Kill process on port 8000
taskkill /PID <PID> /F
```

### Frontend not starting?
```bash
# Check Node version
node --version  # Should be 18+

# Clear cache
npm cache clean --force
rmdir /s /q node_modules .next
npm install

# Check if port is in use
netstat -ano | findstr :3000
```

### API connection failed?
```bash
# 1. Check backend is running
curl http://localhost:8000/api/v1/health

# 2. Check frontend .env
cat frontend/.env

# 3. Check browser console (F12)
```

---

## 🧪 Quick Test

### Test Backend
```bash
# 1. Health check
curl http://localhost:8000/api/v1/health

# 2. Fetch video
curl -X POST http://localhost:8000/api/v1/fetch_video \
  -H "Content-Type: application/json" \
  -d '{"youtube_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'
```

### Test Frontend
1. Open http://localhost:3000
2. Paste: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
3. Click "Fetch Video"
4. Should see video info with thumbnail

---

## 📦 Dependencies

### Backend (Python)
```
fastapi==0.109.0
uvicorn==0.27.0
yt-dlp==2024.3.10
python-multipart==0.0.9
pydantic==2.5.3
python-dotenv==1.0.0
```

### Frontend (Node.js)
```
next@14.1.0
react@18.2.0
typescript@5
tailwindcss@3.3.0
axios@1.6.5
```

---

## 🔄 Common Tasks

### Add New API Endpoint
1. Create function in `backend/routes/video_routes.py`
2. Use `@router.post()` or `@router.get()` decorator
3. Test at http://localhost:8000/docs

### Add New Frontend Component
1. Create file in `frontend/src/components/`
2. Import in `page.tsx`
3. Use in JSX

### Change Port
```bash
# Backend
# Edit backend/.env
PORT=8001

# Frontend
# Run with custom port
$env:PORT=3001; npm run dev
```

### Update Dependencies
```bash
# Backend
pip install --upgrade package-name
pip freeze > requirements.txt

# Frontend
npm update package-name
```

---

## 🎨 Tailwind CSS Classes (Quick Reference)

### Layout
- `flex` `grid` `block` `inline`
- `justify-center` `items-center`
- `gap-4` `space-y-4`

### Sizing
- `w-full` `h-screen` `max-w-4xl`
- `p-4` `px-6` `py-8` `m-4`

### Colors
- `bg-blue-500` `text-white`
- `border-gray-300`

### Effects
- `rounded-lg` `shadow-lg`
- `hover:bg-blue-600`
- `transition-all`

---

## 🆘 Emergency Reset

```bash
# Stop all servers (Ctrl+C)

# Reset backend
cd backend
rmdir /s /q venv __pycache__ temp_videos
del .env

# Reset frontend
cd frontend
rmdir /s /q node_modules .next
del .env

# Reinstall
cd ..
setup.bat
```

---

## 📞 Help Resources

### Documentation
- Main README: `README.md`
- Architecture: `ARCHITECTURE.md`
- Testing: `TESTING.md`
- Troubleshooting: `TROUBLESHOOTING.md`

### API Documentation
- http://localhost:8000/docs (Swagger UI)
- http://localhost:8000/redoc (ReDoc)

### Tech Docs
- FastAPI: https://fastapi.tiangolo.com/
- Next.js: https://nextjs.org/docs
- yt-dlp: https://github.com/yt-dlp/yt-dlp
- Tailwind: https://tailwindcss.com/docs

---

## ✅ Health Check Checklist

- [ ] Backend running on port 8000
- [ ] Frontend running on port 3000
- [ ] Health endpoint returns 200
- [ ] Frontend loads without errors
- [ ] Can fetch YouTube video
- [ ] Video metadata displays

---

## 🎯 Project Status

- ✅ Chunk 1: Video Ingestion (COMPLETE)
- 🔜 Chunk 2: Speech-to-Text
- 🔜 Chunk 3: Transcript Chunking
- 🔜 Chunk 4: AI Scoring
- 🔜 Chunks 5-10: Coming soon

---

## 💡 Pro Tips

1. **Keep both terminals open** - One for backend, one for frontend
2. **Use API docs** - http://localhost:8000/docs for testing
3. **Check console** - Press F12 in browser for errors
4. **Git commit often** - Save your progress frequently
5. **Read error messages** - They usually tell you what's wrong
6. **Test incrementally** - Test after each change
7. **Use .env files** - Never commit secrets to git

---

**Print this card or keep it handy for quick reference!**

**Last Updated:** December 25, 2025
