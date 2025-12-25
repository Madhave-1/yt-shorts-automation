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

3. **Push Code** ✅ (Already done!)
   ```bash
   git remote add origin https://github.com/Madhave-1/yt-shorts-automation.git
   git branch -M main
   git push -u origin main
   ```
   Your repo: https://github.com/Madhave-1/yt-shorts-automation

---

## Step 2: Deploy YT-DLP API to Render

### 2.1 Sign Up
1. Go to https://render.com
2. Click "Get Started for Free"
3. Click "Sign Up with GitHub"
4. Authorize Render

### 2.2 Create New Web Service
1. From dashboard, click "New +"
2. Select "Web Service"
3. Click "Connect account" if needed
4. Find and select `yt-shorts-automation` repository

### 2.3 Configure Service
Fill in these settings:

**Basic Settings:**
- **Name:** `ytdlp-api`
- **Region:** Choose closest to you (e.g., Oregon, Frankfurt)
- **Branch:** `main`
- **Root Directory:** `ytdlp_api` ⚠️ **IMPORTANT!**

**Build & Deploy:**
- **Runtime:** Python 3
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`

**Instance Type:**
- Select **Free** ($0/month)

### 2.4 Deploy
1. Click "Create Web Service" at the bottom
2. Render will start building (takes 5-10 minutes for first deploy)
3. Watch the logs in real-time
4. Wait for "Your service is live 🎉"

### 2.5 Get URL
1. Once deployed, you'll see the URL at the top
2. It will look like: `https://ytdlp-api.onrender.com`
3. **Copy and save this URL!** You need it for backend

### 2.6 Test
```bash
# Test health endpoint
curl https://ytdlp-api.onrender.com/health

# Expected response:
# {"status":"healthy","service":"ytdlp-api","version":"1.0.0"}
```

**Note:** Free tier services sleep after 15 min of inactivity. First request after sleep takes ~30 seconds to wake up.

---

## Step 3: Update Main Backend

1. **Add environment variable**
   
   Create/update `backend/.env`:
   USE_EXTERNAL_API=true
   YTDLP_API_URL=https://ytdlp-api.onrender.com
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
GitHub repo** with all code - https://github.com/Madhave-1/yt-shorts-automation
✅ **YT-DLP API** deployed on Render (free)ilway (free)
✅ **GitHub repo** with all code
✅ **Main backend** updated to use the API (running locally)
✅ **Frontend** (running locally)

---

## 🧪 Testing After Deployment

1. **Test YT-DLP API directly:**
   ```bashtdlp-api.onrender.com
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
ender deployment fails
- Check "Logs" tab for error messages
- Ensure `requirements.txt` is in `ytdlp_api` folder
- Verify Root Directory is set to `ytdlp_api`
- Check Build Command and Start Command are correct

### API returns 500 error
- Click "Logs" tab in Render dashboard
- Look for Python errors or yt-dlp issues
- SSL should work fine on Render's Linux environment

### Can't access deployed URL / Service sleeping
- Free tier sleeps after 15 min inactivity
- First request takes ~30 seconds to wake up
- Upgrade to paid tier ($7/month) for always-on

### Build takes too long
- First build: 5-10 minutes (normal)
- Subsequent builds: 2-3 minutes
- Cender Free Tier:**
- 750 hours/month (enough for 24/7 with downtime)
- Sleeps after 15 min inactivity
- Auto-wakes on first request
- 100 GB bandwidth/month
- Completely FREE!

**Monitor usage:** Render dashboard → Account
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
