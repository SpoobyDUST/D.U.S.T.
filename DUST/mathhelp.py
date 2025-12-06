import discord
from discord.ext import commands
import sys
import datetime
from datetime import datetime
#import math
import cmath
import json
import urllib.request


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents, help_command=None)

@bot.command(name='mathhelp')
async def trighelp(ctx):
  embed = discord.Embed(
    title="Trigonometry Help",
    description="Shows help regarding trigonometry",
  )
  embed.add_field(
    name='$sin',
    value="Takes out the sine value of the expression given; for eg. $sin 90",
    inline=True)
  embed.add_field(
    name='$cos',
    value="Takes out the cosine value of the expression given; for eg. $cos 90",
    inline=True)
  embed.add_field(
    name='$tan',
    value="Takes out the tan value of the expression given; for eg. $tan 90",
    inline=True)
  embed.add_field(name='$solveQuad',
                  value='usage: $solvequad valuea valueb valuec')
  await ctx.send(content=None, embed=embed)


@bot.command(name='sin')
async def sin(ctx, num1):
  num1 = int(num1)
  solution = cmath.sin(num1)
  await ctx.send(solution)


@bot.command(name='cos')
async def cos(ctx, num1):
  num1 = int(num1)
  solution = cmath.cos(num1)
  await ctx.send(solution)


@bot.command(name='tan')
async def tan(ctx, num1):
  num1 = int(num1)
  solution = cmath.tan(num1)
  await ctx.send(solution)


@bot.command(name='solveQuad')
async def solveQuad(ctx, a, b, c):
  #await ctx.send(
  #  "The General Form is: ax²+bx+c, where a, b, and c are real numbers where a != 0, make sure to put it in this form exactly"
  # )
  b = int(b)
  a = int(a)
  c = int(c)
  just = ((b**2) - (4 * a * c))

  just = float(just)

  x = ((-1 * b) + cmath.sqrt(just))
  value_x = x / (2 * a)

  xv2 = ((-1 * b) - cmath.sqrt(just))
  value_xv2 = xv2 / (2 * a)

  if value_x == value_xv2:
    await ctx.send(f'x = {str(value_x)}')
  elif value_x != value_xv2:
    await ctx.send(f'x = {str(value_x)} or {str(value_xv2)}')