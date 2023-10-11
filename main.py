import discord
from discord.ext import commands

config = {
    'token': 'токен',
    'prefix': 'prefix',
}
myintents = discord.Intents.all()
bot = commands.Bot(command_prefix=config['prefix'],intents =myintents)

@bot.event
async def on_message(ctx):
    if ctx.author != bot.user:
        await ctx.reply(ctx.content)

bot.run(config['token'])
