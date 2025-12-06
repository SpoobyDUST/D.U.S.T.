import discord 
from discord.ext import commands 


class welcome(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

        @commands.Cog()
        async def welcome(self, ctx):
            await ctx.message.reply("welcome To The Show")


async def setup(bot):
    await bot.add_cog(welcome(bot))