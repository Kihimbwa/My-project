import os
import sys
import django

# Add the project directory to the path
sys.path.insert(0, 'c:/Users/user/Desktop/django/library_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')
django.setup()

# Run makemigrations
from django.core.management import call_command
call_command('makemigrations', 'library')
print("Migration created successfully!")
