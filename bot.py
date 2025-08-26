import discord
from discord.ext import commands
import os
from flask import Flask
import threading

# ---- Discord bot setup ----
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ping2(ctx):
    await ctx.send("pong")

# ---- Flask webserver ----
app = Flask("")

@app.route("/")
def home():
    return "Bot is running!"

def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

# Start Flask in a separate thread
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

# Start Discord bot
bot.run(TOKEN)
