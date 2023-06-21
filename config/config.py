import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
   load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
que = {}
admins = {}

#------------------------ Important Stuff 🤎 -----------------------

API_ID = int(getenv("API_ID", "6853443"))
API_HASH = getenv("API_HASH", "4d12a5b55da2e7093fcd897566336521")
BOT_TOKEN = getenv("BOT_TOKEN", "6224624072:AAHMkg0GgP5XJO0o1bWxd_8o8F0tsBg_DRI")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
STRING_SESSION = getenv("STRING_SESSION", "BACxexkoqBPt5JW4kmH1A89RlAtgoolmxyAk9KZbe366ADUTiBMKIJa1f3Id1cTa6HTmMnrSSH2DG5XIeQbpbRKyDmCWMIoa26O69aVQ8FZgGHx6Swyr9Chi2lnkwk3VAPqfTrgOY1EG-dz4XXVdKxEZGzYp778d8U9DJIElk8jE4UC8_25PzYtAEThQncQ3tvJ3gpGxS1QxTIyN7gYNF5XlG3T2KdDFkAGyC5sTybgsOreHTxVDNL_flPljrnfEuwlfy5JyzV1j_pT_VBR4mHDeOKCoQon6AQdDr3vT07F6uQcmlC_AFtw-MAvQDII_uQfodxU3FfSil9307X6wfaR4AAAAAW5CyFkA")
BOT_USERNAME = getenv("BOT_USERNAME", "myozkmtimbot")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "6144837721").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "")) 

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
#________________________ Updates  & Music bot name________________
NETWORK = getenv("NETWORK", "xl444")
GROUP = getenv("GROUP", "")
BOT_NAME = getenv("myozkmtimbot", "Music")
BANNED_USERS = filters.user()

#************************* Image Stuff  ****************************

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/5fdd8da2461c05d893189.png")

aiohttpsession = aiohttp.ClientSession()


