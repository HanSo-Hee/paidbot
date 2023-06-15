# (c) @PredatorHackerzZ || @TeleRoidGroup
import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", "0"))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    GROUP_USERNAME = os.environ.get("GROUP_USERNAME")
    CHANNEL_USERNAME = os.environ.get("CHANNEL_USERNAME")
    DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-100"))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "1445283714"))
    DATABASE_URL = os.environ.get("DATABASE_URL")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
    FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
    OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
    AUTO_DELETE_TIME = int(os.environ.get("AUTO_DELETE_TIME", "30"))
    AUTHORIZED_USERS = [int(user_id) for user_id in os.environ.get("AUTHORIZED_USERS", "").split() if user_id]
#     ABOUT_BOT_TEXT = f"""
# This is a Permanent FileStore Bot. 
# Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

# ╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
# │
# ├🔸🤖 **My Name:** [𝐅𝐢𝐥𝐞 𝐒𝐭𝐨𝐫𝐞 𝐁𝐨𝐭](https://t.me/{BOT_USERNAME})
# │
# ├🔸📝 **Language:** [𝐏𝐲𝐭𝐡𝐨𝐧𝟑](https://www.python.org)
# │
# ├🔹📚 **Library:** [𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦](https://docs.pyrogram.org)
# │
# ├🔹📡 **Hosted On:** [𝐇𝐞𝐫𝐨𝐤𝐮](https://heroku.com)
# │
# ├🔸👨‍💻 **Developer:** [@𝐏𝐫𝐞𝐝𝐚𝐭𝐨𝐫](https://t.me/OwnYourBotz) 
# │
# ├🔹👥 **Bot Support:** [𝐒𝐮𝐩𝐩𝐨𝐫𝐭](https://t.me/TeleRoid14)
# │
# ├🔸🔔 **Bot Updates:** [𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/TeleRoidGroup)
# │
# ╰──────[ 😎 ]───────────⍟
# """
    HOME_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸🤖 **My Name:** [FileStorage Bot](https://t.me/{BOT_USERNAME})
│
├🔸📝 **Language:** [Python 3](https://www.python.org)
│
├🔹📚 **Library:** [Pyrogram](https://docs.pyrogram.org)
│
├🔹📡 **Hosted On:** [Heroku](https://heroku.com)
│
├🔸👨‍💻 **Developer:** [@Owner](https://t.me/Binod_Binod1) 
│
├🔹👥 **Bot Support:** [Support Group](https://t.me/+5QByEUGVImAwY2E1)
│
├🔸🔔 **Bot Updates:** [Updates Channel](https://t.me/Filmy_Night)
│
╰──────[ 😎 ]───────────⍟
"""
    ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [@PredatorHackerzZ](https://t.me/PredatorHackerzZ)
 
 I am Super noob Please Support My Hard Work

[Donate Me](https://t.me/DonateXrobot)
"""
#     HOME_TEXT = """
# Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

# How to Use Bot & its Benefits??

# 📢 Send me any File, and it will be uploaded in My Database, and you will get the File Link.

# ⚠️ Benefits: If you have a Telegram Movie Channel or any Copyright Channel, then it's useful for daily usage. You can send me your file, and I will send a permanent link to you, keeping your channel safe from **Copyright Infringement** issues. I support channels as well. You can check the **About Bot** section.

# ❌ **PORNOGRAPHY CONTENTS** are strictly prohibited and will result in a permanent ban.
# """
