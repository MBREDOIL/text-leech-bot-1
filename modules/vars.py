import os

API_ID    = os.environ.get("API_ID", "22182189")
API_HASH  = os.environ.get("API_HASH", "5e7c4088f8e23d0ab61e29ae11960bf5")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", " "))  # Default to 8000 if not set
