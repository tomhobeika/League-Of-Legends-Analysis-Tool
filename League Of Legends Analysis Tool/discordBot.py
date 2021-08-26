import discord
import re
import league

#Discord API Commpunication
bot = commands.Bot(command_prefix='!')

@bot.command()
async def leagueBuild(ctx):
	champList = []

	while len(champList) < 5:
		await ctx.send('Please enter {} more champion(s) to be analysed.'.format(5 - len(champList)))

bot.run('')