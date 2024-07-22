import os
import logging
from logging.handlers import RotatingFileHandler

# Bot token from @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7328135456:AAGDZ4oq_rmfxJxf_RC52HunI6Kti9kdXTU")

# API ID and Hash from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28157070"))
API_HASH = os.environ.get("API_HASH", "9078ae3b29412c4c1220e631edc5ed77")

# Database channel ID
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002217482019"))

# Owner ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6018348449"))

# Port
PORT = os.environ.get("PORT", "8080")

# Database URL and name
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://guruji123ktest:Combotest@cluster0.ulk5omw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

# Shortlink settings
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "publicearn.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "b323441bc55ef14be63018992134d393a62a9da9")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Expiry time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "False")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/Ultroid_Official/18")

# Force subscription channel ID
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

# Number of bot workers
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")

# Force subscription message
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

# Custom caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "This video/Photo/anything is available on the internet. We LeakHubd or its subsidiary channel doesn't produce any of them.")

# Content protection
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Disable channel button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

# Bot stats text
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

# Admins
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6018348449").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

ADMINS.append(OWNER_ID)
ADMINS.append(6695586027)

# Logger configuration
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrofork").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
