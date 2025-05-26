from discord.ext import commands
import discord
from discord import app_commands


class Greetings(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command()
    @commands.has_permissions(administrator=True)
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)  
        await interaction.response.send_message(f"Pong! Latency: {latency}ms")


    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"Hello {ctx.author.display_name}!")

async def setup(bot:commands.Bot):
    """Load the Greetings cog."""
    await bot.add_cog(Greetings(bot))
