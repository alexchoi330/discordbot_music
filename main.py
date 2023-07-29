import discord
from discord.ext import commands
import asyncio
import tracemalloc


import os

#import all of the cogs
from help_cog import help_cog
from music_cog import music_cog

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

#remove the default help command so that we can write out own

bot.remove_command('help')

#register the class with the bot

# async def setup(bot):

#     await bot.add_cog(help_cog(bot))
#     await bot.add_cog(music_cog(bot))

# setup(bot)
bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))

#start the bot with our token
# with open('token.txt') as f:
#     token = f.read()
# bot.run(token)
bot.run(os.getenv("TOKEN"))
