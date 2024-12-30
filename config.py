from os import environ

API_ID = int(environ.get("API_ID", "24267726"))
API_HASH = environ.get("API_HASH", "7500ba8248548cc3864bd033668f9a9a")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002053069822"))
ADMINS = int(environ.get("ADMINS", "6231550362"))
DB_URI = environ.get("DB_URI", "mongodb+srv://EXONTESTMONGO:EXONTESTMONGO@cluster0.bviw7ic.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")
