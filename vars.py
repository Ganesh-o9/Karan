#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "xxxxxxxxx"))
API_HASH = environ.get("API_HASH", "xxxxxxxxxxxxxxxxxxxxxxx")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "5215296789"))
CREDIT = environ.get("CREDIT", "𝗞𝗮𝗿𝗮𝗻'𝘀 𝗕𝗼𝘁")
AUTH_USER = os.environ.get('AUTH_USERS', '5215296789,5664992018,5789145706').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
