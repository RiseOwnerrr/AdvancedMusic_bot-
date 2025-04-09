from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import Config
import pymongo
import asyncio

# Initialize MongoDB
mongo_client = pymongo.MongoClient(Config.MONGO_DB_URI)
db = mongo_client["RiseMusicBot"]

# Create Pyrogram Client
app = Client(
    "RiseMusicBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")
)

# Start Command
@app.on_message(filters.command("start") & filters.private)
async def start(client, message: Message):
    await message.reply_text(
        f"👋 Hello {message.from_user.mention}!\n\n"
        "I'm a multi-feature bot with music, games, and group management capabilities!\n\n"
        "Use /help to see all commands.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Owner", url=f"tg://user?id={Config.OWNER_ID}")],
            [InlineKeyboardButton("Help", callback_data="help")]
        ])
    )

# Help Command
@app.on_message(filters.command("help"))
async def help(client, message: Message):
    help_text = """
📚 **Available Commands:**

🎵 **Music Commands:**
/play [song name] - Play a song
/playlist - Show current playlist
/skip - Skip current song

🛡️ **Group Management:**
/lock - Lock group links
/ban - Ban a user
/mute - Mute a user

🎮 **Games:**
/game - Start a game
/quiz - Start a quiz

🔞 **Adult Chat (Private Only):**
/sexting - Start adult chat (English/Hinglish)
"""
    await message.reply_text(help_text)

# Link Protector
@app.on_message(filters.group & filters.text)
async def link_protector(client, message: Message):
    if "http://" in message.text or "https://" in message.text:
        # Check if user is admin
        user = await message.chat.get_member(message.from_user.id)
        if user.status in ["administrator", "creator"]:
            return
            
        # Mute the user
        await message.chat.restrict_member(
            user_id=message.from_user.id,
            permissions=ChatPermissions(
                can_send_messages=False,
                can_send_media_messages=False,
                can_send_other_messages=False,
                can_add_web_page_previews=False
            )
        )
        await message.reply_text(
            f"⚠️ {message.from_user.mention} was muted for sending links!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Unmute", callback_data=f"unmute_{message.from_user.id}")]
            ])
        )
        await message.delete()

# Random Member Tagging
@app.on_message(filters.command("tagrandom"))
async def tag_random(client, message: Message):
    members = []
    async for member in app.get_chat_members(message.chat.id):
        if not member.user.is_bot:
            members.append(member.user)
    
    if members:
        random_member = random.choice(members)
        await message.reply_text(
            f"Hey {random_member.mention}! You've been randomly selected!",
            reply_to_message_id=message.id
        )

if __name__ == "__main__":
    print("Bot Started!")
    app.run()from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import Config
import pymongo
import asyncio

# Initialize MongoDB
mongo_client = pymongo.MongoClient(Config.MONGO_DB_URI)
db = mongo_client["RiseMusicBot"]

# Create Pyrogram Client
app = Client(
    "RiseMusicBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")
)

# Start Command
@app.on_message(filters.command("start") & filters.private)
async def start(client, message: Message):
    await message.reply_text(
        f"👋 Hello {message.from_user.mention}!\n\n"
        "I'm a multi-feature bot with music, games, and group management capabilities!\n\n"
        "Use /help to see all commands.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Owner", url=f"tg://user?id={Config.OWNER_ID}")],
            [InlineKeyboardButton("Help", callback_data="help")]
        ])
    )

# Help Command
@app.on_message(filters.command("help"))
async def help(client, message: Message):
    help_text = """
📚 **Available Commands:**

🎵 **Music Commands:**
/play [song name] - Play a song
/playlist - Show current playlist
/skip - Skip current song

🛡️ **Group Management:**
/lock - Lock group links
/ban - Ban a user
/mute - Mute a user

🎮 **Games:**
/game - Start a game
/quiz - Start a quiz

🔞 **Adult Chat (Private Only):**
/sexting - Start adult chat (English/Hinglish)
"""
    await message.reply_text(help_text)

# Link Protector
@app.on_message(filters.group & filters.text)
async def link_protector(client, message: Message):
    if "http://" in message.text or "https://" in message.text:
        # Check if user is admin
        user = await message.chat.get_member(message.from_user.id)
        if user.status in ["administrator", "creator"]:
            return
            
        # Mute the user
        await message.chat.restrict_member(
            user_id=message.from_user.id,
            permissions=ChatPermissions(
                can_send_messages=False,
                can_send_media_messages=False,
                can_send_other_messages=False,
                can_add_web_page_previews=False
            )
        )
        await message.reply_text(
            f"⚠️ {message.from_user.mention} was muted for sending links!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Unmute", callback_data=f"unmute_{message.from_user.id}")]
            ])
        )
        await message.delete()

# Random Member Tagging
@app.on_message(filters.command("tagrandom"))
async def tag_random(client, message: Message):
    members = []
    async for member in app.get_chat_members(message.chat.id):
        if not member.user.is_bot:
            members.append(member.user)
    
    if members:
        random_member = random.choice(members)
        await message.reply_text(
            f"Hey {random_member.mention}! You've been randomly selected!",
            reply_to_message_id=message.id
        )

if __name__ == "__main__":
    print("Bot Started!")
    app.run()
