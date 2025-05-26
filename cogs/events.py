from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hi(self, ctx):
        await ctx.send(f"ohayo {ctx.author.display_name}!")

async def setup(bot):
    await bot.add_cog(Events(bot))
