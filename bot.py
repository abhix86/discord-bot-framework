import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
#intents.message_content = True  # Enable if your bot needs to read message content
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith('aiko') or message.content.startswith('Aiko') or 'aiko' in message.content:
        await message.channel.send(f"Aiko reporting, {message.author.mention}!")
    await bot.process_commands(message)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}(on guild: {id(bot.guilds)})")
    print("Runing bot on discord.py version:", discord.__version__)
    


@bot.event
async def setup_hook():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"✅ Loaded: \"{filename}\"")
            except Exception as e:
                print(f"❌ Failed to load {filename}: {e}")

    await bot.tree.sync()
    print("✅ Synced application commands")



bot.run(TOKEN)
