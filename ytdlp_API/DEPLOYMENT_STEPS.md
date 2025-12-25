# 🚀 Step-by-Step Deployment Guide

## Prerequisites
- GitHub account
- Railway/Render account (free)

---

## Step 1: Push to GitHub

1. **Initialize Git** (if not already done)
   ```bash
   cd D:\yt-shorts-automation
   git init
   git add .
   git commit -m "Initial commit with ytdlp API"
   ```

2. **Create GitHub Repository**
   - Go to https://github.com/new
   - Name: `yt-shorts-automation`
   - Make it Public or Private
   - Don't add README (you have one)

3. **Push Code**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/yt-shorts-automation.git
   git branch -M main
   git push -u origin main
   ```

---

## Step 2: Deploy YT-DLP API to Railway

### 2.1 Sign Up
1. Go to https://railway.app
2. Click "Login with GitHub"
3. Authorize Railway

### 2.2 Create Project
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Click "Configure GitHub App"
4. Give Railway access to your repository
5. Select `yt-shorts-automation` repo

### 2.3 Configure Service
1. Click "Add Service" → "GitHub Repo"
2. Select your repo
3. **Important:** Set root directory:
   - Click on the service
   - Go to "Settings"
   - Find "Root Directory"
   - Set to: `ytdlp_api`
   - Save

### 2.4 Deploy
1. Railway will automatically detect Python
2. It will use `railway.json` configuration
3. Wait 2-3 minutes for deployment
4. Check "Deployments" tab for progress

### 2.5 Get URL
1. Go to "Settings" tab
2. Click "Generate Domain"
3. Copy the URL (e.g., `ytdlp-api-production-xxxx.up.railway.app`)
4. **Save this URL!** You'll need it for the main backend

### 2.6 Test
```bash
# Test health endpoint
curl https://your-ytdlp-api.up.railway.app/health

# Expected response:
# {"status":"healthy","service":"ytdlp-api","version":"1.0.0"}
```

---

## Step 3: Update Main Backend

1. **Add environment variable**
   
   Create/update `backend/.env`:
   ```bash
   # Existing variables
   HOST=0.0.0.0
   PORT=8000
   TEMP_VIDEO_DIR=./temp_videos
   API_PREFIX=/api/v1
   
   # NEW: Add your deployed YT-DLP API URL
   YTDLP_API_URL=https://your-ytdlp-api.up.railway.app
   ```

2. **The backend code is already updated below** (see next files)

---

## Step 4: Deploy Main Backend (Optional - Later)

When ready to deploy main backend:

1. **Create another Railway service**
   - Same GitHub repo
   - Root directory: `backend`
   - Environment variables: Add all from `.env`

2. **Or use Render**
   - Same process but on render.com
   - Free tier: 750 hours/month

---

## Step 5: Deploy Frontend (Optional - Later)

1. **Vercel (Recommended)**
   ```bash
   cd frontend
   npm install -g vercel
   vercel
   # Follow prompts
   ```

2. **Or Netlify**
   - Connect GitHub repo
   - Build command: `cd frontend && npm run build`
   - Publish directory: `frontend/.next`

---

## 📊 Summary

After completing these steps, you'll have:

✅ **YT-DLP API** deployed on Railway (free)
✅ **GitHub repo** with all code
✅ **Main backend** updated to use the API (running locally)
✅ **Frontend** (running locally)

---

## 🧪 Testing After Deployment

1. **Test YT-DLP API directly:**
   ```bash
   curl -X POST https://your-ytdlp-api.up.railway.app/download \
     -H "Content-Type: application/json" \
     -d '{"youtube_url":"https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'
   ```

2. **Test via your local backend:**
   - Start local backend: `python main.py`
   - Open frontend: http://localhost:3000
   - Try downloading a video

---

## ⚠️ Troubleshooting

### Railway deployment fails
- Check "Deployments" tab for logs
- Ensure `railway.json` exists
- Verify Python version compatibility

### API returns 500 error
- Check Railway logs: Click service → "View Logs"
- Might be SSL issue (should work on Linux)
- Check if yt-dlp is updated

### Can't access deployed URL
- Make sure domain is generated in Railway settings
- Check if service is "Active" (not "Sleeping")

---

## 💰 Cost Tracking

**Railway Free Tier:**
- 500 hours/month
- $5 credit/month
- Sleeps after 30 min inactivity
- Auto-wakes on request

**Monitor usage:** Railway dashboard → Usage

---

## 🎯 Next Steps

1. ✅ Deploy YT-DLP API (Steps above)
2. ⏳ Test it works
3. ⏳ Update main backend to use it
4. ⏳ Continue building Chunk 2-10
5. ⏳ Deploy main backend when ready
6. ⏳ Deploy frontend last

---

**You're now ready to deploy!** Start with Step 1 above. 🚀

Need help with any step? Check the Railway/Render docs or ask me!
