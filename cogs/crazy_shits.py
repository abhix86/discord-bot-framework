from discord.ext import commands
from discord import app_commands
import discord
import asyncio

class Crazy_shits(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # example
    @app_commands.command()
    async def say(self, Interaction: discord.Interaction, message: str):
        await Interaction.response.send_message(message)

    @commands.command()
    async def annoy(self, ctx, member: commands.MemberConverter, times: int = 10, message: str = ''):
        if times <+ 0:
            await ctx.send("Please provide a positive number of times to annoy.")
            return
        for _ in range(times):
            await ctx.send(f"{member.mention} {message}")
            await asyncio.sleep(0.3)
        await ctx.send(f"Annoyed {member.mention} {times} times!")



async def setup(bot):
    await bot.add_cog(Crazy_shits(bot))
