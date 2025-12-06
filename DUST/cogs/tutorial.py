import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

class Tutorial(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tutorial(self, ctx, *, subject):
        # Scrape the web for relevant information
        url = "https://www.google.com/search?q=" + subject + "+tutorial"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        links = soup.findAll("a")

        # Extract the top 5 relevant links
        top_links = []
        for link in links:
            link_href = link.get("href")
            if "url?q=" in link_href and not "webcache" in link_href:
                top_links.append(link.get("href")[7:])

            if len(top_links) >= 5:
                break

        # Create an embed with the top links
        embed = discord.Embed(title="Tutorial for " + subject)
        for i, link in enumerate(top_links):
            embed.add_field(name="Link " + str(i+1), value=link, inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Tutorial(bot))