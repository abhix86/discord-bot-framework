from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # example
    @commands.command()
    async def command(self, ctx):
        await ctx.send("None available commands at the moment, please check back later!")

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def ban(self, ctx, member: commands.MemberConverter, *, reason=None):
        """Ban a member from the server."""
        await ctx.guild.ban(member, reason=reason)
        await ctx.send(f"{member.display_name} has been banned for: {reason}")
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(f"{error} Please mention a valid member.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f"{error} Reach out to an administrator, in case of any mistake.")
        else:
            await ctx.send(f"An error occurred: {error}")

async def setup(bot):
    await bot.add_cog(Commands(bot))
