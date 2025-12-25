# 🔧 Troubleshooting Guide

## Common Issues and Solutions

### 🔴 Backend Issues

#### Issue 1: "Python was not found"
**Error:**
```
'python' is not recognized as an internal or external command
```

**Solutions:**
1. Install Python from python.org (3.8 or higher)
2. During installation, check "Add Python to PATH"
3. Restart terminal
4. Test: `python --version`

Alternative:
```bash
# Try python3 instead
python3 --version
python3 -m venv venv
```

---

#### Issue 2: "pip: command not found"
**Error:**
```
'pip' is not recognized as an internal or external command
```

**Solutions:**
```bash
# Use python -m pip instead
python -m pip install -r requirements.txt

# Or upgrade pip
python -m pip install --upgrade pip
```

---

#### Issue 3: "Cannot activate virtual environment"
**Error:**
```
venv\Scripts\activate : cannot be loaded because running scripts is disabled
```

**Solution (Windows PowerShell):**
```powershell
# Run as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Alternative:**
```bash
# Use Command Prompt instead of PowerShell
cmd
cd backend
venv\Scripts\activate.bat
```

---

#### Issue 4: "Port 8000 already in use"
**Error:**
```
ERROR: [Errno 10048] Only one usage of each socket address is normally permitted
```

**Solutions:**
```bash
# Option 1: Find and kill process using port 8000
netstat -ano | findstr :8000
taskkill /PID <PID_NUMBER> /F

# Option 2: Use different port
# In backend/.env, change:
PORT=8001

# Or run directly:
uvicorn main:app --port 8001
```

---

#### Issue 5: "yt_dlp module not found"
**Error:**
```
ModuleNotFoundError: No module named 'yt_dlp'
```

**Solutions:**
```bash
# Ensure virtual environment is activated
cd backend
venv\Scripts\activate

# Install dependencies again
pip install -r requirements.txt

# Or install specifically
pip install yt-dlp
```

---

#### Issue 6: "YouTube video download fails"
**Error:**
```
ERROR: Unable to download video
```

**Solutions:**
```bash
# Update yt-dlp to latest version
pip install --upgrade yt-dlp

# Try a different video URL
# Some videos may be region-restricted or private

# Check internet connection
ping youtube.com

# Try manual download to test
yt-dlp "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

---

#### Issue 7: "No module named 'services'"
**Error:**
```
ModuleNotFoundError: No module named 'services'
```

**Solution:**
```bash
# Ensure you're running from backend directory
cd backend
python main.py

# Or use proper Python path
python -m main
```

---

### 🔵 Frontend Issues

#### Issue 1: "npm not found"
**Error:**
```
'npm' is not recognized as an internal or external command
```

**Solutions:**
1. Install Node.js from nodejs.org (v18 or higher)
2. Restart terminal
3. Test: `npm --version`

---

#### Issue 2: "npm install fails"
**Error:**
```
ENOENT: no such file or directory
npm ERR! code ELIFECYCLE
```

**Solutions:**
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and package-lock.json
rmdir /s /q node_modules
del package-lock.json

# Reinstall
npm install
```

---

#### Issue 3: "Port 3000 already in use"
**Error:**
```
Port 3000 is already in use
```

**Solutions:**
```bash
# Option 1: Kill process on port 3000
netstat -ano | findstr :3000
taskkill /PID <PID_NUMBER> /F

# Option 2: Use different port
# Run with PORT environment variable
$env:PORT=3001; npm run dev
```

---

#### Issue 4: "API connection failed"
**Error (in browser console):**
```
Failed to fetch
Network Error
```

**Solutions:**

1. **Check backend is running:**
   ```bash
   # Open http://localhost:8000/api/v1/health
   # Should return {"status": "healthy"}
   ```

2. **Check .env file:**
   ```bash
   # frontend/.env should have:
   NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
   ```

3. **Restart both servers:**
   ```bash
   # Terminal 1 (Backend)
   cd backend
   venv\Scripts\activate
   python main.py

   # Terminal 2 (Frontend)
   cd frontend
   npm run dev
   ```

4. **Check CORS:**
   - Backend should have CORS middleware enabled (already configured)

---

#### Issue 5: "Module not found: Can't resolve '@/...'"
**Error:**
```
Module not found: Can't resolve '@/components/VideoFetcher'
```

**Solutions:**
```bash
# Check tsconfig.json has path alias
# Should have:
"paths": {
  "@/*": ["./src/*"]
}

# Restart dev server
npm run dev
```

---

#### Issue 6: "Hydration error"
**Error:**
```
Unhandled Runtime Error
Error: Hydration failed
```

**Solutions:**
```bash
# Clear .next cache
rmdir /s /q .next

# Restart server
npm run dev

# Check for browser extensions that might interfere
# Try in incognito mode
```

---

### 🟡 Integration Issues

#### Issue 1: "CORS policy error"
**Error (in browser):**
```
Access to XMLHttpRequest blocked by CORS policy
```

**Solutions:**

1. **Verify backend CORS configuration:**
   ```python
   # In backend/main.py, should have:
   app.add_middleware(
       CORSMiddleware,
       allow_origins=["*"],
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```

2. **Restart backend server**

3. **Clear browser cache**

---

#### Issue 2: "Invalid YouTube URL"
**Error:**
```
Invalid YouTube URL provided
```

**Solutions:**
- Use format: `https://www.youtube.com/watch?v=VIDEO_ID`
- Not: `https://youtu.be/VIDEO_ID` (though this should work)
- Not: `https://www.youtube.com/embed/VIDEO_ID`

**Supported formats:**
- ✅ `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
- ✅ `https://youtu.be/dQw4w9WgXcQ`
- ✅ `https://m.youtube.com/watch?v=dQw4w9WgXcQ`
- ❌ `youtube.com/watch?v=dQw4w9WgXcQ` (missing https://)

---

#### Issue 3: "Video downloads but frontend shows error"
**Symptoms:**
- Backend logs show successful download
- Frontend shows error message

**Solutions:**

1. **Check browser console for actual error:**
   - Press F12 in browser
   - Go to Console tab
   - Look for error messages

2. **Check API response:**
   - Network tab in browser
   - Look at response from `/fetch_video`
   - Check status code and response body

3. **Verify API URL:**
   ```javascript
   // In frontend/src/services/api.ts
   const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1';
   console.log('API URL:', API_URL); // Add this to debug
   ```

---

### 🟢 Performance Issues

#### Issue 1: "Video download is very slow"
**Symptoms:**
- Takes > 5 minutes for short video

**Solutions:**
1. Check internet speed
2. Try smaller video
3. Update yt-dlp: `pip install --upgrade yt-dlp`
4. Check system resources (CPU, RAM)

---

#### Issue 2: "High memory usage"
**Symptoms:**
- System becomes slow
- Backend uses > 2GB RAM

**Solutions:**
```python
# In backend/services/video_downloader.py
# Add format restrictions:
ydl_opts = {
    'format': 'best[height<=720]',  # Limit to 720p
    # ... other options
}
```

---

#### Issue 3: "Temp folder fills up disk space"
**Solution:**
```bash
# Manually clean temp folder
cd backend/temp_videos
del *.mp4

# Or run cleanup from Python
python -c "from services.video_downloader import video_service; video_service.cleanup_old_videos(1)"
```

---

## 🔍 Debugging Tips

### Backend Debugging

1. **Enable verbose logging:**
   ```python
   # In backend/main.py
   import logging
   logging.basicConfig(level=logging.DEBUG)
   ```

2. **Test API directly:**
   ```bash
   # Use curl or Postman
   curl -X POST http://localhost:8000/api/v1/fetch_video \
     -H "Content-Type: application/json" \
     -d "{\"youtube_url\": \"https://www.youtube.com/watch?v=dQw4w9WgXcQ\"}"
   ```

3. **Check API docs:**
   - Visit http://localhost:8000/docs
   - Test endpoints interactively

### Frontend Debugging

1. **Check browser console:**
   - Press F12
   - Look for errors in Console tab
   - Check Network tab for failed requests

2. **Add debug logging:**
   ```typescript
   // In VideoFetcher.tsx
   console.log('Submitting URL:', youtubeUrl);
   console.log('API Response:', response);
   console.log('Error:', error);
   ```

3. **Check environment variables:**
   ```bash
   # In frontend, add to page.tsx
   console.log('API URL:', process.env.NEXT_PUBLIC_API_URL);
   ```

---

## 📞 Getting Help

### Check logs location:
- **Backend logs:** Terminal where `python main.py` is running
- **Frontend logs:** Terminal where `npm run dev` is running
- **Browser logs:** F12 → Console tab

### Information to include when asking for help:
1. Operating system (Windows/Mac/Linux)
2. Python version: `python --version`
3. Node.js version: `node --version`
4. Error message (full text)
5. Steps to reproduce
6. What you've already tried

---

## ✅ Health Check Commands

Run these to verify everything is working:

```bash
# Backend health
curl http://localhost:8000/api/v1/health

# Expected: {"status":"healthy","service":"video-ingestion","version":"1.0.0"}

# Frontend accessibility
curl http://localhost:3000

# Expected: HTML content

# Python packages
cd backend
venv\Scripts\activate
pip list

# Node packages
cd frontend
npm list --depth=0
```

---

## 🔄 Reset Everything

If all else fails, start fresh:

```bash
# 1. Stop all servers (Ctrl+C in terminals)

# 2. Clean backend
cd backend
rmdir /s /q venv
rmdir /s /q __pycache__
rmdir /s /q temp_videos
del .env

# 3. Clean frontend
cd frontend
rmdir /s /q node_modules
rmdir /s /q .next
del .env
del package-lock.json

# 4. Reinstall
cd ..
setup.bat
```

---

**Last Updated:** December 25, 2025  
**For:** Chunk 1 Implementation
