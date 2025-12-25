import os
import ssl

# Disable SSL verification globally (Development only)
os.environ['PYTHONHTTPSVERIFY'] = '0'
os.environ['CURL_CA_BUNDLE'] = ''
os.environ['REQUESTS_CA_BUNDLE'] = ''
ssl._create_default_https_context = ssl._create_unverified_context

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from routes import video_router

# Create FastAPI app
app = FastAPI(
    title="AI Podcast Clip Generator API",
    description="Backend API for generating viral clips from YouTube videos",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(
    video_router,
    prefix=settings.API_PREFIX,
    tags=["Video Processing"]
)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to AI Podcast Clip Generator API",
        "docs": "/docs",
        "health": f"{settings.API_PREFIX}/health"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )
