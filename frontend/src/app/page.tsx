'use client';

import { useState } from 'react';
import VideoFetcher from '@/components/VideoFetcher';

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
      <div className="container mx-auto px-4 py-16">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold text-white mb-4">
            🎬 AI Podcast Clip Generator
          </h1>
          <p className="text-xl text-gray-300 max-w-2xl mx-auto">
            Transform long YouTube videos into viral short clips with AI-powered moment detection
          </p>
        </div>

        {/* Main Content */}
        <div className="max-w-4xl mx-auto">
          <VideoFetcher />
        </div>

        {/* Features */}
        <div className="mt-16 grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto">
          <div className="bg-white/10 backdrop-blur-lg rounded-lg p-6 text-center">
            <div className="text-4xl mb-3">🎥</div>
            <h3 className="text-xl font-semibold text-white mb-2">
              Easy Upload
            </h3>
            <p className="text-gray-300">
              Just paste a YouTube link and let AI do the magic
            </p>
          </div>
          
          <div className="bg-white/10 backdrop-blur-lg rounded-lg p-6 text-center">
            <div className="text-4xl mb-3">🤖</div>
            <h3 className="text-xl font-semibold text-white mb-2">
              AI-Powered
            </h3>
            <p className="text-gray-300">
              Automatically detect the most engaging moments
            </p>
          </div>
          
          <div className="bg-white/10 backdrop-blur-lg rounded-lg p-6 text-center">
            <div className="text-4xl mb-3">📱</div>
            <h3 className="text-xl font-semibold text-white mb-2">
              Vertical Clips
            </h3>
            <p className="text-gray-300">
              Perfect for TikTok, Instagram Reels, and YouTube Shorts
            </p>
          </div>
        </div>
      </div>
    </main>
  );
}
