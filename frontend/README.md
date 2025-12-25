# AI Podcast Clip Generator - Frontend

Next.js frontend for the AI Podcast Clip Generator application.

## Features

- ✅ Modern UI with Tailwind CSS
- ✅ YouTube URL input
- ✅ Video fetching integration
- ✅ Real-time feedback and loading states
- ✅ Responsive design
- ✅ TypeScript support

## Setup

### Prerequisites

- Node.js 18+ 
- npm or yarn

### Installation

1. Install dependencies:
```bash
npm install
# or
yarn install
```

2. Create environment file:
```bash
cp .env.example .env
```

3. Update `.env` with your backend API URL (default is http://localhost:8000/api/v1)

### Running the Development Server

```bash
npm run dev
# or
yarn dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

## Project Structure

```
frontend/
├── src/
│   ├── app/
│   │   ├── layout.tsx        # Root layout
│   │   ├── page.tsx          # Home page
│   │   └── globals.css       # Global styles
│   ├── components/
│   │   └── VideoFetcher.tsx  # Video fetch component
│   └── services/
│       └── api.ts            # API service layer
├── public/                   # Static assets
├── package.json
├── tsconfig.json
├── tailwind.config.js
└── next.config.js
```

## Chunk 1 Complete ✅

This frontend includes:
- ✅ Beautiful gradient UI design
- ✅ YouTube URL input form
- ✅ API integration with backend
- ✅ Loading states and error handling
- ✅ Video metadata display
- ✅ Responsive layout

## Building for Production

```bash
npm run build
npm start
```

## Deployment

This frontend can be deployed to:
- **Vercel** (Recommended - Free)
- **Netlify** (Free)
- **Cloudflare Pages** (Free)

### Deploy to Vercel

1. Push code to GitHub
2. Import project in Vercel
3. Set environment variable: `NEXT_PUBLIC_API_URL`
4. Deploy!

## Next Steps

As we build more chunks, we'll add:
- Transcript display (Chunk 2)
- Clip preview (Chunk 5-7)
- Download functionality (Chunk 8)
- User dashboard (Chunk 10)
