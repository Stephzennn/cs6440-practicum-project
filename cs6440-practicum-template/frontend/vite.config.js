import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// In local dev, forward /api calls to the FastAPI server (uvicorn on :8000).
// On Vercel, vercel.json routes /api/* to the Python service instead.
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': 'http://localhost:8000',
    },
  },
})
