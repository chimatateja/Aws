import sys
import os
import site

# Define the path to the virtual environment
venv_path = "/var/www/html/flaskapp/venv"

# Add the virtual environment's site-packages to sys.path
site.addsitedir(os.path.join(venv_path, "lib/python3.12/site-packages"))

# Set environment variable for mod_wsgi
os.environ["PYTHONHOME"] = venv_path

# Add the Flask app directory to sys.path
sys.path.insert(0, "/var/www/html/flaskapp")

# Use the virtual environment's Python binary
sys.executable = os.path.join(venv_path, "bin", "python3")

# Import and set up the Flask application
from flaskapp import app as application
