# Cookie Setup for YouTube Bot Bypass

YouTube now requires authentication cookies to download videos. Follow these steps:

## Method 1: Browser Extension (Easiest)

1. **Install Extension:**
   - **Chrome/Edge**: [Get cookies.txt LOCALLY](https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc)
   - **Firefox**: [cookies.txt](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/)

2. **Export Cookies:**
   - Go to [YouTube](https://www.youtube.com/)
   - Make sure you're logged in
   - Click the extension icon
   - Click "Export" or "Get cookies.txt"
   - Save as `cookies.txt`

3. **Place Cookie File:**
   - Save `cookies.txt` in `ytdlp_API/` folder
   - The file should be next to `main.py`

## Method 2: Command Line (Advanced)

If you already have yt-dlp installed locally:

```bash
# Export cookies from Chrome
yt-dlp --cookies-from-browser chrome --cookies cookies.txt "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# The cookies.txt will be created in current directory
# Move it to ytdlp_API/ folder
```

## File Format

The `cookies.txt` file must:
- Be in Netscape/Mozilla format
- Start with `# Netscape HTTP Cookie File` or `# HTTP Cookie File`
- Use correct line endings (CRLF for Windows, LF for Unix)

## Security Warning ⚠️

**NEVER commit cookies.txt to git!** It contains your authentication tokens.
- The file is already in `.gitignore`
- Don't share this file with anyone
- Regenerate cookies if compromised

## For Render Deployment

To use cookies on Render:

1. **Create cookies.txt** locally as above
2. **Base64 encode it** for environment variable:
   ```bash
   # Windows PowerShell
   [Convert]::ToBase64String([IO.File]::ReadAllBytes("cookies.txt"))
   
   # Linux/Mac
   base64 cookies.txt
   ```
3. **Add to Render Environment Variables:**
   - Key: `YOUTUBE_COOKIES_BASE64`
   - Value: (paste the base64 string)

4. The code will automatically decode and use it.

## Verify Setup

After placing `cookies.txt`, restart the server and you should see:
```
✅ Using cookies from cookies.txt
```

If missing, you'll see:
```
⚠️ No cookies.txt found - may encounter bot detection
```
