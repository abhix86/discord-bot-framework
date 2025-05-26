from discord.ext import commands
from discord import app_commands
import discord

class Crazy_shits(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # example
    @app_commands.command()
    async def say(self, Interaction: discord.Interaction, message: str):
        await Interaction.response.send_message(message)

async def setup(bot):
    await bot.add_cog(Crazy_shits(bot))
