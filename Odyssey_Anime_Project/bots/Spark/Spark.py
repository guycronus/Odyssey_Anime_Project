import sqlite3
import asyncio
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file
BOT_TOKEN = os.getenv('ODYSSEYSPARK_BOT_TOKEN')

# Then use BOT_TOKEN in the bot initialization:
bot = OdysseySpark(BOT_TOKEN)
# Initialize database
def init_db():
    conn = sqlite3.connect("odyssey_spark.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT, premium BOOLEAN, subscriptions TEXT)''')
    conn.commit()
    conn.close()

# Fetch anime news from Jikan API (MyAnimeList)
def fetch_anime_news():
    url = "https://api.jikan.moe/v4/top/anime?type=airing&limit=5"
    try:
        response = requests.get(url)
        data = response.json()
        news = []
        for anime in data["data"]:
            title = anime["title"]
            synopsis = anime["synopsis"][:200] + "..." if len(anime["synopsis"]) > 200 else anime["synopsis"]
            news.append(f"📺 *{title}*\n{synopsis}\nRead more: {anime['url']}")
        return "\n\n".join(news) or "No new anime news today!"
    except Exception as e:
        return f"Error fetching news: {str(e)}"

# Bot class
class OdysseySpark:
    def __init__(self, token):
        self.app = Application.builder().token(token).build()
        self.scheduler = AsyncIOScheduler()
        self.scheduler.add_job(self.broadcast_news, "interval", hours=24, next_run_time=datetime.now())
        self.scheduler.start()

    async def start(self, update, context):
        user_id = update.effective_user.id
        username = update.effective_user.username
        await update.message.reply_text(
            "Welcome to @OdysseySpark! Get daily anime news and updates. 🖌️\n"
            "Commands:\n/news - Get latest news\n/subscribe <anime> - Get alerts for specific anime\n"
            "/premium - Unlock exclusive features\n/promote - Discover other Odyssey bots"
        )
        self.add_user(user_id, username)

    def add_user(self, user_id, username):
        conn = sqlite3.connect("odyssey_spark.db")
        c = conn.cursor()
        c.execute("INSERT OR IGNORE INTO users (user_id, username, premium, subscriptions) VALUES (?, ?, ?, ?)",
                  (user_id, username, False, ""))
        conn.commit()
        conn.close()

    async def news(self, update, context):
        news = fetch_anime_news()
        await update.message.reply_text(news, parse_mode="Markdown")

    async def subscribe(self, update, context):
        user_id = update.effective_user.id
        if not context.args:
            await update.message.reply_text("Usage: /subscribe <anime_name>")
            return
        anime = " ".join(context.args).lower()
        conn = sqlite3.connect("odyssey_spark.db")
        c = conn.cursor()
        c.execute("SELECT subscriptions FROM users WHERE user_id = ?", (user_id,))
        subs = c.fetchone()[0].split(",") if c.fetchone()[0] else []
        if anime not in subs:
            subs.append(anime)
            c.execute("UPDATE users SET subscriptions = ? WHERE user_id = ?", (",".join(subs), user_id))
            conn.commit()
            await update.message.reply_text(f"Subscribed to {anime} updates!")
        else:
            await update.message.reply_text(f"Already subscribed to {anime}.")
        conn.close()

    async def premium(self, update, context):
        await update.message.reply_text(
            "Unlock @OdysseySpark Premium for $7/month!\n"
            "Benefits: Real-time news alerts, exclusive spoilers, ad-free.\n"
            "DM @AnimeOdysseyHub_Bot to subscribe (coming soon)."
        )

    async def promote(self, update, context):
        other_bots = ["@OdysseyQuest", "@OdysseyCanvas", "@OdysseyClan", "@OdysseyBazaar"]
        await update.message.reply_text(f"Explore the Anime Odyssey Hub: {', '.join(other_bots)}")

    async def broadcast_news(self):
        news = fetch_anime_news()
        conn = sqlite3.connect("odyssey_spark.db")
        c = conn.cursor()
        c.execute("SELECT user_id FROM users")
        users = c.fetchall()
        for user in users:
            try:
                await self.app.bot.send_message(chat_id=user[0], text=news, parse_mode="Markdown")
            except Exception:
                pass
        conn.close()

    def run(self):
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("news", self.news))
        self.app.add_handler(CommandHandler("subscribe", self.subscribe))
        self.app.add_handler(CommandHandler("premium", self.premium))
        self.app.add_handler(CommandHandler("promote", self.promote))
        self.app.run_polling()

# Run bot
if __name__ == "__main__":
    init_db()
    bot = OdysseySpark("YOUR_ODYSSEYSPARK_BOT_TOKEN")
    bot.run()