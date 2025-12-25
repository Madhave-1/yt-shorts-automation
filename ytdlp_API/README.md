# YT-DLP API Service

Microservice for downloading YouTube videos using yt-dlp.

## 🚀 Deployment Instructions

### Option 1: Deploy to Railway (Recommended)

1. **Create Railway Account**
   - Go to https://railway.app
   - Sign up with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Select `ytdlp_api` folder as root

3. **Configure**
   - Railway will auto-detect Python
   - It will use `railway.json` config automatically

4. **Deploy**
   - Click "Deploy"
   - Wait 2-3 minutes
   - Copy the URL (e.g., `https://ytdlp-api-production.up.railway.app`)

5. **Test**
   ```bash
   curl https://your-app.railway.app/health
   ```

---

### Option 2: Deploy to Render

1. **Create Render Account**
   - Go to https://render.com
   - Sign up with GitHub

2. **Create New Web Service**
   - Click "New +"
   - Select "Web Service"
   - Connect your GitHub repo
   - Root directory: `ytdlp_api`

3. **Configure**
   - Name: `ytdlp-api`
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Instance Type: Free

4. **Deploy**
   - Click "Create Web Service"
   - Wait 5-10 minutes for first deploy
   - Copy the URL (e.g., `https://ytdlp-api.onrender.com`)

---

### Option 3: Deploy to Fly.io

1. **Install Fly CLI**
   ```bash
   # Windows (PowerShell)
   iwr https://fly.io/install.ps1 -useb | iex
   ```

2. **Login**
   ```bash
   fly auth login
   ```

3. **Deploy**
   ```bash
   cd ytdlp_api
   fly launch
   # Follow prompts, select free tier
   fly deploy
   ```

4. **Get URL**
   ```bash
   fly status
   # Copy the hostname
   ```

---

## 📡 API Endpoints

### GET /
```json
{
  "service": "YT-DLP API",
  "status": "running"
}
```

### GET /health
```json
{
  "status": "healthy",
  "service": "ytdlp-api",
  "version": "1.0.0"
}
```

### POST /download
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
  "title": "Video Title",
  "duration": 1234,
  "uploader": "Channel Name",
  "thumbnail": "https://...",
  "description": "...",
  "file_path": "./temp_videos/uuid.mp4"
}
```

### DELETE /cleanup/{video_id}
Delete a downloaded video file.

---

## 🧪 Local Testing

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python main.py

# Test
curl http://localhost:8001/health
```

---

## 🔗 Connect to Main Backend

After deployment, update your main backend's `.env`:

```bash
YTDLP_API_URL=https://your-ytdlp-api.railway.app
```

Then modify your backend to call this API instead of downloading directly.

---

## 📊 Free Tier Limits

| Platform | RAM | CPU | Hours | Bandwidth |
|----------|-----|-----|-------|-----------|
| Railway | 512MB | Shared | 500 hrs/month | 100GB |
| Render | 512MB | Shared | 750 hrs/month | 100GB |
| Fly.io | 256MB | Shared | Always on | 160GB |

**Recommendation:** Start with Railway for easiest setup.

---

## ⚠️ Important Notes

1. **SSL is disabled** for development - this works on Linux servers
2. **Temp files** are stored temporarily - implement cleanup in production
3. **No authentication** - add API keys in production
4. **File storage** - use cloud storage (S3/R2) for downloaded videos in production

---

## 🎯 Next Steps

After deploying:
1. Test the API with curl or Postman
2. Update main backend to use this API
3. Deploy main backend separately
4. Connect frontend to main backend

**Status:** Ready to Deploy ✅
