import discord
from discord.ext import commands
import os

# Haal token uit environment variable
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Zet de intents die je nodig hebt
intents = discord.Intents.default()
intents.message_content = True  # Nodig om commands te gebruiken

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ping2(ctx):
    await ctx.send("pong")

bot.run(TOKEN)
