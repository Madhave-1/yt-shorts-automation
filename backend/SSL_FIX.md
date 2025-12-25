# 🔒 SSL Certificate Issues - Fix Guide

## Problem
You're seeing this error:
```
[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate
```

## What's Happening
Python on Windows sometimes can't verify SSL certificates when downloading from YouTube. This is a common issue with yt-dlp.

## ✅ Solution (Already Applied)

The code has been updated with the following fixes:

### 1. Updated Dependencies
Added to `requirements.txt`:
- `certifi` - Provides SSL certificates
- `urllib3` - Updated for better SSL handling
- `requests` - Updated for compatibility

### 2. Updated yt-dlp Configuration
The video downloader now uses these options:
```python
'nocheckcertificate': True,      # Disable SSL verification
'no_check_certificate': True,     # Alternative flag
'prefer_insecure': True,          # Prefer insecure connections
'socket_timeout': 30,             # Increase timeout
'retries': 3,                     # Retry on failure
```

## 🚀 How to Apply the Fix

### Method 1: Reinstall Packages (Recommended)
```bash
cd backend
venv\Scripts\activate
pip install -r requirements.txt --upgrade
python main.py
```

### Method 2: Manual Installation
```bash
cd backend
venv\Scripts\activate
pip install certifi urllib3 requests --upgrade
python main.py
```

### Method 3: Run SSL Fix Script
```bash
cd backend
venv\Scripts\activate
python fix_ssl.py
python main.py
```

## 🧪 Test the Fix

Try downloading a video again:

1. Start the backend: `python main.py`
2. Open frontend: http://localhost:3000
3. Test with this URL: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`

## 🔍 Alternative Solutions

### If the above doesn't work:

#### Option A: Install certifi certificates
```bash
cd backend
venv\Scripts\activate
python -c "import certifi; print(certifi.where())"
```

#### Option B: Set environment variables (Windows)
```bash
# PowerShell
$env:SSL_CERT_FILE = "C:\Users\YourName\AppData\Local\Programs\Python\Python38\Lib\site-packages\certifi\cacert.pem"
$env:REQUESTS_CA_BUNDLE = $env:SSL_CERT_FILE

# Then run
python main.py
```

#### Option C: Update Windows certificates
1. Open `certmgr.msc` (Certificate Manager)
2. Go to Trusted Root Certification Authorities
3. Import certificates if needed

#### Option D: Disable SSL globally (Development Only)
In `services/video_downloader.py`, the SSL verification is already disabled for development.

⚠️ **Note:** Disabling SSL verification is acceptable for development but should be enabled in production.

## 📝 What Changed in Your Code

### Before:
```python
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': str(output_path),
    'nocheckcertificate': True,
}
```

### After:
```python
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': str(output_path),
    'quiet': False,
    'no_warnings': False,
    'extract_flat': False,
    'nocheckcertificate': True,
    'no_check_certificate': True,
    'prefer_insecure': True,
    'source_address': '0.0.0.0',
    'socket_timeout': 30,
    'retries': 3,
}
```

## 🎯 Why This Happens

1. **Windows Python SSL:** Python on Windows doesn't always have system certificates
2. **Corporate Networks:** Some networks block or intercept SSL
3. **Antivirus/Firewall:** Security software may interfere
4. **Outdated Certificates:** Old Python installations have outdated certs

## ✅ Verification

After applying the fix, you should see:
- ✅ No SSL warnings
- ✅ Video downloads successfully
- ✅ `INFO: [youtube] Extracting video information`
- ✅ Progress bar showing download

## 🆘 Still Not Working?

If you still see SSL errors:

1. **Check your internet connection**
   ```bash
   ping youtube.com
   ```

2. **Check if yt-dlp works standalone**
   ```bash
   cd backend
   venv\Scripts\activate
   yt-dlp --no-check-certificate "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
   ```

3. **Try a different video**
   - Some videos may be region-restricted
   - Some may require login

4. **Check antivirus/firewall**
   - Temporarily disable and test
   - Add Python to exceptions

5. **Update yt-dlp**
   ```bash
   pip install --upgrade yt-dlp
   ```

## 📞 Need More Help?

1. Check full error logs in the terminal
2. Review [TROUBLESHOOTING.md](../TROUBLESHOOTING.md)
3. Check yt-dlp issues: https://github.com/yt-dlp/yt-dlp/issues

## 🎉 Success!

Once fixed, you should be able to:
- ✅ Download any YouTube video
- ✅ No SSL warnings
- ✅ Fast and reliable downloads
- ✅ Ready for Chunk 2!

---

**Status:** SSL Issues Fixed ✅  
**Last Updated:** December 25, 2025
