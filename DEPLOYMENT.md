# Deployment Guide - Library Management System

## Option 1: Deploy to Render.com (Recommended)

### Backend (Django API)

1. **Prepare your code:**
   - Push your code to GitHub
   - Make sure `requirements.txt` is complete

2. **Create account on Render.com:**
   - Go to render.com and sign up
   - Connect your GitHub account

3. **Create a Web Service:**
   - Click "New" → "Web Service"
   - Select your GitHub repository
   - Configure:
     - Name: library_system
     - Environment: Python
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `gunicorn library_system.wsgi`
     - Python Version: 3.11

4. **Environment Variables:**
   - Add these in Render dashboard:
     - `SECRET_KEY`: django-insecure-m3ko$0l1b2r4ry2024
     - `DEBUG`: False
     - `ALLOWED_HOSTS`: library_system.onrender.com

5. **Database:**
   - Create a PostgreSQL database on Render
   - Update `DATABASES` in settings.py

### Frontend (React)

1. **Build the React app:**
   
```
bash
   cd library-frontend
   npm run build
   
```

2. **Deploy to Netlify or Vercel:**
   - Create account on Netlify.com
   - Drag and drop the `build` folder
   - Or connect GitHub and deploy automatically

### Alternative: Deploy Both to Render

1. Create a new Web Service for Django
2. Create a new Static Site for React
3. Configure environment variables

## Option 2: Deploy to Railway

1. Go to railway.app and sign up
2. Create new project
3. Add PostgreSQL database
4. Add Django project from GitHub
5. Add React project from GitHub

## Option 3: Deploy to PythonAnywhere (Easier for Django only)

1. Go to pythonanywhere.com
2. Create account (free tier available)
3. Upload your code via Files tab
4. Configure WSGI in Web tab
5. Set up database

## Important: Update Frontend API URL

After deployment, update your React app:

1. Create `.env.production` file:
   
```
   REACT_APP_API_URL=https://your-backend-url.onrender.com
   
```

2. Rebuild and redeploy

## Quick Fix for Current Setup

If you want to test now without full deployment:

1. **Use ngrok for temporary public URL:**
   
```
bash
   # Install ngrok
   pip install ngrok
   
   # Run Django
   python manage.py runserver 8000
   
   # In another terminal
   ngrok http 8000
   
```

2. **Use Cloudflare Tunnel:**
   
```
bash
   # Install cloudflared
   cloudflared tunnel --url http://localhost:8000
   
```

## Summary

For permanent worldwide access:
1. Deploy Django backend to Render/Railway/PythonAnywhere
2. Deploy React frontend to Netlify/Vercel
3. Update frontend to point to your backend URL
4. Share the frontend URL with users
