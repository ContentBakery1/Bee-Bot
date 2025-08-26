import discord
from discord.ext import commands
import os

# Haal token uit environment variable
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ping2(ctx):
    await ctx.send("pong")

bot.run(TOKEN)
