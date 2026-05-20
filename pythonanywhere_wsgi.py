# This file contains the WSGI configuration required to serve up your
# web application on PythonAnywhere.
#
# Replace 'yourusername' with your actual PythonAnywhere username below.

import sys
import os

# 1. Add your project directory to the sys.path
# Replace 'yourusername' with your actual PythonAnywhere username
project_home = '/home/yourusername/sherise'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# 2. Set environment variables if you are not using a .env file directly, 
# or ensure python-dotenv loads them from your .env file in the project folder.
from dotenv import load_dotenv
load_dotenv(os.path.join(project_home, '.env'))

# 3. Import the Flask app object and set it to 'application'
from app import app as application
