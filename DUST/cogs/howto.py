import discord
import requests

from discord.ext import commands


class FreeResources(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def howto(self, ctx, *, query):
        # Build the query URL
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx=<your_cx>&key=<your_api_key>&num=5&cr=countryUS&lr=lang_en&searchType=image"

        # Send request to the Google Custom Search API
        response = requests.get(url).json()

        # Get the first image result
        image_url = response["items"][0]["link"]

        # Create an embed with the image and search query
        embed = discord.Embed(title=f"How to {query}", color=0x00FF00)
        embed.set_image(url=image_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def course(self, ctx, *, query):
        # Build the query URL
        url = f"https://api.coursera.org/api/courses.v1?q=search&query={query}&fields=previewLink&limit=5"

        # Send request to the Coursera API
        response = requests.get(url).json()

        # Create an embed with the search query and preview link of the first course result
        embed = discord.Embed(title=f"Courses for {query}", color=0x00FF00)
        embed.add_field(name="Preview Link", value=response["elements"][0]["previewLink"])

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(FreeResources(bot))