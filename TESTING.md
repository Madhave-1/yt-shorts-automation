# 🧪 Testing Guide - Chunk 1

## Quick Test Checklist

### ✅ Backend Tests

1. **Installation Test**
   ```bash
   cd backend
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```
   ✅ Should complete without errors

2. **Server Start Test**
   ```bash
   python main.py
   ```
   ✅ Should show: "Uvicorn running on http://0.0.0.0:8000"

3. **Health Check Test**
   - Open browser: http://localhost:8000/api/v1/health
   - ✅ Should return:
   ```json
   {
     "status": "healthy",
     "service": "video-ingestion",
     "version": "1.0.0"
   }
   ```

4. **API Documentation Test**
   - Open browser: http://localhost:8000/docs
   - ✅ Should show interactive Swagger UI
   - ✅ Should see POST /api/v1/fetch_video endpoint

### ✅ Frontend Tests

1. **Installation Test**
   ```bash
   cd frontend
   npm install
   ```
   ✅ Should complete without errors

2. **Server Start Test**
   ```bash
   npm run dev
   ```
   ✅ Should show: "ready started server on 0.0.0.0:3000"

3. **UI Load Test**
   - Open browser: http://localhost:3000
   - ✅ Should show gradient background
   - ✅ Should see "AI Podcast Clip Generator" title
   - ✅ Should see YouTube URL input field
   - ✅ Should see "Fetch Video" button

### ✅ Integration Tests

1. **Video Fetch Test - Valid URL**
   - Input: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
   - Click "Fetch Video"
   - ✅ Should show loading spinner
   - ✅ Should show success message
   - ✅ Should display video card with:
     - Title
     - Thumbnail
     - Channel name
     - Duration
     - Video ID

2. **Video Fetch Test - Invalid URL**
   - Input: `https://invalid-url.com`
   - Click "Fetch Video"
   - ✅ Should show error message
   - ❌ Should NOT crash

3. **Video Fetch Test - Empty Input**
   - Leave input empty
   - ✅ Button should be disabled

## 🧪 Detailed Testing

### Backend API Testing (Using curl)

#### Test 1: Health Check
```bash
curl http://localhost:8000/api/v1/health
```
Expected Response:
```json
{
  "status": "healthy",
  "service": "video-ingestion",
  "version": "1.0.0"
}
```

#### Test 2: Fetch Valid Video
```bash
curl -X POST http://localhost:8000/api/v1/fetch_video \
  -H "Content-Type: application/json" \
  -d "{\"youtube_url\": \"https://www.youtube.com/watch?v=dQw4w9WgXcQ\"}"
```
Expected Response:
```json
{
  "success": true,
  "message": "Video downloaded successfully",
  "video_id": "some-uuid",
  "file_path": "./temp_videos/some-uuid.mp4",
  "title": "Rick Astley - Never Gonna Give You Up",
  "duration": 213,
  "uploader": "Rick Astley",
  "thumbnail": "https://...",
  "description": "..."
}
```

#### Test 3: Invalid YouTube URL
```bash
curl -X POST http://localhost:8000/api/v1/fetch_video \
  -H "Content-Type: application/json" \
  -d "{\"youtube_url\": \"https://invalid-url.com\"}"
```
Expected Response:
```json
{
  "detail": "Invalid YouTube URL provided"
}
```
Status Code: 400

### Backend Testing (Using Python)

Create `backend/test_api.py`:
```python
import requests

BASE_URL = "http://localhost:8000/api/v1"

def test_health():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    print("✅ Health check passed")

def test_fetch_video():
    payload = {
        "youtube_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    }
    response = requests.post(f"{BASE_URL}/fetch_video", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["success"] == True
    assert "video_id" in data
    print("✅ Video fetch passed")
    print(f"   Title: {data['title']}")
    print(f"   Duration: {data['duration']}s")

def test_invalid_url():
    payload = {
        "youtube_url": "https://invalid-url.com"
    }
    response = requests.post(f"{BASE_URL}/fetch_video", json=payload)
    assert response.status_code == 400
    print("✅ Invalid URL handling passed")

if __name__ == "__main__":
    print("Running API tests...\n")
    test_health()
    test_fetch_video()
    test_invalid_url()
    print("\n✅ All tests passed!")
```

Run tests:
```bash
cd backend
pip install requests
python test_api.py
```

### Frontend Testing (Manual)

#### Test 1: Component Rendering
1. Open http://localhost:3000
2. ✅ Check title is visible
3. ✅ Check input field is present
4. ✅ Check button is present
5. ✅ Check feature cards are visible

#### Test 2: Form Validation
1. Leave input empty
2. ✅ Button should be disabled
3. Type a URL
4. ✅ Button should be enabled

#### Test 3: Loading State
1. Enter valid YouTube URL
2. Click "Fetch Video"
3. ✅ Button should show spinner
4. ✅ Button text should change to "Processing..."
5. ✅ Button should be disabled during loading

#### Test 4: Success State
1. After successful fetch
2. ✅ Success message should appear (green)
3. ✅ Video card should display
4. ✅ Thumbnail should load
5. ✅ Metadata should be correct

#### Test 5: Error State
1. Enter invalid URL
2. Click "Fetch Video"
3. ✅ Error message should appear (red)
4. ✅ Video card should NOT display

## 🎯 Test Scenarios

### Scenario 1: Short Video
- URL: Short video (< 5 minutes)
- ✅ Should download successfully
- ✅ Should complete in < 30 seconds

### Scenario 2: Long Video
- URL: Long video (1-2 hours)
- ✅ Should download successfully
- ⚠️ May take several minutes

### Scenario 3: High Quality Video
- URL: 4K video
- ✅ Should download best available quality
- ⚠️ Large file size

### Scenario 4: Playlist URL
- URL: YouTube playlist
- ⚠️ Should handle first video only
- Or show appropriate error

### Scenario 5: Age-Restricted Video
- URL: Age-restricted content
- ⚠️ May fail with error
- Check error handling

## 📊 Expected Performance

### Backend
- Health check: < 50ms
- Video download (short): < 30s
- Video download (long): 1-5 minutes
- Memory usage: < 500MB

### Frontend
- Initial load: < 2s
- Page interaction: < 100ms
- API response rendering: < 50ms

## 🐛 Common Issues & Solutions

### Issue 1: "Module not found: yt_dlp"
**Solution:**
```bash
cd backend
venv\Scripts\activate
pip install yt-dlp
```

### Issue 2: "Connection refused" error
**Solution:**
- Ensure backend is running
- Check port 8000 is not in use
- Verify NEXT_PUBLIC_API_URL in frontend .env

### Issue 3: "CORS error" in browser
**Solution:**
- Backend already has CORS enabled
- Clear browser cache
- Restart both servers

### Issue 4: Video download fails
**Solution:**
- Check internet connection
- Try different YouTube URL
- Check yt-dlp is up to date: `pip install --upgrade yt-dlp`

### Issue 5: Frontend not connecting to backend
**Solution:**
- Check backend is running on port 8000
- Verify .env file in frontend has correct API_URL
- Check browser console for errors

## ✅ Production Readiness Checklist

Before deploying to production:

### Backend
- [ ] Add rate limiting
- [ ] Add authentication
- [ ] Implement logging
- [ ] Add monitoring
- [ ] Set up error tracking (Sentry)
- [ ] Configure CORS properly
- [ ] Add request validation
- [ ] Implement file size limits
- [ ] Add cleanup cron job
- [ ] Set up database (if needed)
- [ ] Configure environment variables
- [ ] Add health check monitoring

### Frontend
- [ ] Configure production API URL
- [ ] Add analytics
- [ ] Optimize images
- [ ] Add SEO meta tags
- [ ] Configure caching
- [ ] Add error boundary
- [ ] Implement retry logic
- [ ] Add loading skeletons
- [ ] Test on mobile devices
- [ ] Add accessibility features
- [ ] Configure CDN
- [ ] Add security headers

## 🔍 Debug Mode

### Enable Backend Debug Logging
In [config.py](backend/config.py), add:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Enable Frontend Debug Mode
In [next.config.js](frontend/next.config.js), add:
```javascript
module.exports = {
  // ... existing config
  logging: {
    fetches: {
      fullUrl: true,
    },
  },
}
```

## 📝 Test Results Template

```
Date: __________
Tester: __________

Backend Tests:
[ ] Installation
[ ] Server Start
[ ] Health Check
[ ] API Documentation
[ ] Video Download (valid URL)
[ ] Video Download (invalid URL)
[ ] Error Handling

Frontend Tests:
[ ] Installation
[ ] Server Start
[ ] UI Load
[ ] Form Validation
[ ] Loading States
[ ] Success Display
[ ] Error Display

Integration Tests:
[ ] Valid Video Fetch
[ ] Invalid URL Handling
[ ] Error Messages
[ ] Video Metadata Display

Performance:
- Health check response time: _____ ms
- Video download time: _____ seconds
- Frontend load time: _____ seconds

Issues Found:
1. ________________________
2. ________________________
3. ________________________

Notes:
_________________________________
_________________________________
```

---

**Last Updated:** December 25, 2025  
**Test Coverage:** Chunk 1 Complete ✅
