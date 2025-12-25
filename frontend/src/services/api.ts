import axios from 'axios';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1';

export interface VideoFetchResponse {
  success: boolean;
  message: string;
  video_id?: string;
  file_path?: string;
  title?: string;
  duration?: number;
  uploader?: string;
  thumbnail?: string;
  description?: string;
}

export const videoApi = {
  /**
   * Fetch video from YouTube URL
   */
  fetchVideo: async (youtubeUrl: string): Promise<VideoFetchResponse> => {
    try {
      const response = await axios.post(`${API_URL}/fetch_video`, {
        youtube_url: youtubeUrl,
      });
      return response.data;
    } catch (error: any) {
      throw new Error(
        error.response?.data?.detail || 'Failed to fetch video'
      );
    }
  },

  /**
   * Health check
   */
  healthCheck: async (): Promise<any> => {
    try {
      const response = await axios.get(`${API_URL}/health`);
      return response.data;
    } catch (error) {
      throw new Error('API is not available');
    }
  },
};
