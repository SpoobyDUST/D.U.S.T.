import discord
from discord.ext import commands

bot = discord.Bot
class ReactionRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.event()
    async def on_raw_reaction_add(self, payload):
        #Get message information
        message_id = payload.message_id
        if message_id == 1058522821350928414:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

            if payload.emoji.name == 'PC_Master_Race': 
                role = discord.utils.get(guild.roles, name='Developer Operative')
            elif payload.emoji.name == 'laserbearpfp':
                role = discord.utils.get(guild.roles, name='Market Operative')
            elif payload.emoji.name == 'FuckThemPeople':
                role = discord.utils.get(guild.roles, name='Resell Operative')
            elif payload.emoji.name == 'GrannyStickup':
                role = discord.utils.get(guild.roles, name= 'Gaming Operative')
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)
        
            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
                    print("done")
                else:
                    print("Mmber not found.")
            else:
                print("role not found.")

@commands.Cog.event
async def on_raw_reaction_remove(payload):
    pass


def setup(bot):
    bot.add_cog(ReactionRoles(bot))