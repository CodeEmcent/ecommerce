### REQUIREMENTS FOR HOSTING A PROJECT

# 1. Prepare Your Django Project:

<!-- 
a. Install Required Dependencies

pip install gunicorn
pip install dj-database-url
pip install python-decouple

b. Update Settings for Production

ALLOWED_HOSTS = ["*"]

c. Add Static File Configuration

pip install whitenoise

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this
    ...
]

-->

# 2. Database Configuration:

<!-- 
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3')
}
-->

# 3. Static Files:

<!-- 
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

&
Run: 

python manage.py collectstatic

-->

# 4. Configure Environment Variables

<!-- 
python -m pip install django-environ
pip install python-dotenv

Update your setting configuration

import os
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

create an .env file


-->

# 3. Set Up a Git Repository

# 5. Add a Procfile

<!-- 
web: gunicorn your_project_name.wsgi
-->
