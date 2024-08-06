# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23159366"))
API_HASH = getenv("API_HASH", "4623dd30dd1303bddb729eb0862262d9")
BOT_TOKEN = getenv("BOT_TOKEN", "7335128385:AAFQIaQ36e3tQ1uZi-wanJFmX6IxQhQLCbU")
OWNER_ID = int(getenv("OWNER_ID", "5222155765"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://testbot:testbot@cluster0.7rzwxwx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1001917606160"))
FORCESUB = getenv("FORCESUB", "WarriorUnitsBots")
