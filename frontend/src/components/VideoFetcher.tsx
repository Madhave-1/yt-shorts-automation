'use client';

import { useState } from 'react';
import { videoApi, VideoFetchResponse } from '@/services/api';

export default function VideoFetcher() {
  const [youtubeUrl, setYoutubeUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [result, setResult] = useState<VideoFetchResponse | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResult(null);

    try {
      const response = await videoApi.fetchVideo(youtubeUrl);
      setResult(response);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const formatDuration = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  };

  return (
    <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-8 shadow-2xl">
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label htmlFor="youtube-url" className="block text-sm font-medium text-white mb-2">
            YouTube Video URL
          </label>
          <input
            id="youtube-url"
            type="text"
            value={youtubeUrl}
            onChange={(e) => setYoutubeUrl(e.target.value)}
            placeholder="https://www.youtube.com/watch?v=..."
            className="w-full px-4 py-3 rounded-lg bg-white/20 border border-white/30 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-purple-500"
            disabled={loading}
          />
        </div>

        <button
          type="submit"
          disabled={loading || !youtubeUrl}
          className="w-full py-3 px-6 rounded-lg bg-gradient-to-r from-purple-600 to-pink-600 text-white font-semibold hover:from-purple-700 hover:to-pink-700 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 transform hover:scale-105"
        >
          {loading ? (
            <span className="flex items-center justify-center">
              <svg className="animate-spin h-5 w-5 mr-3" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none" />
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
              </svg>
              Processing...
            </span>
          ) : (
            '🚀 Fetch Video'
          )}
        </button>
      </form>

      {/* Error Message */}
      {error && (
        <div className="mt-4 p-4 bg-red-500/20 border border-red-500 rounded-lg">
          <p className="text-red-200">
            <strong>Error:</strong> {error}
          </p>
        </div>
      )}

      {/* Success Result */}
      {result && result.success && (
        <div className="mt-6 space-y-4">
          <div className="p-4 bg-green-500/20 border border-green-500 rounded-lg">
            <p className="text-green-200 font-semibold">✅ {result.message}</p>
          </div>

          {/* Video Info Card */}
          <div className="bg-white/5 rounded-lg p-6 border border-white/20">
            <div className="flex gap-4">
              {result.thumbnail && (
                <img
                  src={result.thumbnail}
                  alt={result.title}
                  className="w-32 h-32 object-cover rounded-lg"
                />
              )}
              <div className="flex-1 space-y-2">
                <h3 className="text-xl font-bold text-white">{result.title}</h3>
                <div className="space-y-1 text-sm text-gray-300">
                  <p><strong>Channel:</strong> {result.uploader}</p>
                  <p><strong>Duration:</strong> {result.duration ? formatDuration(result.duration) : 'N/A'}</p>
                  <p><strong>Video ID:</strong> <span className="font-mono text-xs">{result.video_id}</span></p>
                </div>
                {result.description && (
                  <p className="text-sm text-gray-400 mt-2">{result.description}</p>
                )}
              </div>
            </div>
          </div>

          {/* Next Steps */}
          <div className="bg-blue-500/20 border border-blue-500 rounded-lg p-4">
            <p className="text-blue-200 text-sm">
              📝 <strong>Next:</strong> Video is ready! In future chunks, we'll add transcript generation and clip creation.
            </p>
          </div>
        </div>
      )}
    </div>
  );
}
