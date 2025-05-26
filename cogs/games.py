from discord.ext import commands

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # example
    @commands.command()
    async def game(self, ctx):
        await ctx.send("Let's play a game!")

async def setup(bot):
    await bot.add_cog(Games(bot))
