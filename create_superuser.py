#!/usr/bin/env python
"""
Create superuser automatically for Render deployment.
Place this file in the backend folder (root of Django project).
Usage: python create_superuser.py
"""

import os
import sys
import django
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_django():
    """Setup Django environment"""
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(BASE_DIR)
    
    # ✅ Update this line
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')
    
    django.setup()
    logging.info(f"Django setup complete. BASE_DIR: {BASE_DIR}")

def create_superuser():
    """Create superuser if it doesn't exist"""
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'Admin')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'nurudinikihimbwa@gmail.com')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', '12345678')
    
    if User.objects.filter(username=username).exists():
        logging.info(f"Superuser '{username}' already exists. Skipping creation.")
        return
    
    User.objects.create_superuser(username=username, email=email, password=password)
    logging.info(f"✅ Superuser '{username}' created successfully!")

def main():
    try:
        logging.info("Starting superuser creation script...")
        setup_django()
        create_superuser()
        logging.info("Superuser script completed successfully!")
    except Exception as e:
        logging.error(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()