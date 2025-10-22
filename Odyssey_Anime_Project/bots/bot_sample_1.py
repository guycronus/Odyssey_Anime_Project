from telegram.ext import Application, CommandHandler, MessageHandler, filters
import sqlite3
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# Initialize database
def init_db():
    conn = sqlite3.connect("anime_bot_army.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT, premium BOOLEAN)''')
    conn.commit()
    conn.close()

# Bot class for shared functionality
class AnimeBot:
    def __init__(self, token, name):
        self.app = Application.builder().token(token).build()
        self.name = name
        self.scheduler = AsyncIOScheduler()
        self.scheduler.start()

    async def start(self, update, context):
        user_id = update.effective_user.id
        await update.message.reply_text(f"Welcome to {self.name}! Try /subscribe for premium features.")
        self.add_user(user_id, update.effective_user.username)

    def add_user(self, user_id, username):
        conn = sqlite3.connect("anime_bot_army.db")
        c = conn.cursor()
        c.execute("INSERT OR IGNORE INTO users (user_id, username, premium) VALUES (?, ?, ?)", (user_id, username, False))
        conn.commit()
        conn.close()

    async def promote_others(self, update, context):
        other_bots = ["@AnimePulse", "@AnimeQuizMaster", "@AnimeArtCraft", "@AnimeHub", "@AnimeDeals"]
        await update.message.reply_text(f"Check out our other bots: {', '.join([b for b in other_bots if b != self.name])}")

    def run(self):
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("promote", self.promote_others))
        self.app.run_polling()

# Example: Initialize Anime News Bot
if __name__ == "__main__":
    init_db()
    news_bot = AnimeBot("YOUR_TELEGRAM_BOT_TOKEN", "@AnimePulse")
    news_bot.run()