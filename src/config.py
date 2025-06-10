import os

# Base directory for storing crawled data
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

# Ensure the directory exists
os.makedirs(DATA_DIR, exist_ok=True)