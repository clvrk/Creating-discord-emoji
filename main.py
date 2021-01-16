from PIL import Image
import requests
import discord
from discord.ext import commands
from io import BytesIO
import os
from dotenv import load_dotenv
client = commands.Bot(command_prefix='!', help_command=None)

load_dotenv()

@client.command()
async def createemoji(ctx, object, *, name):
	guild = ctx.guild
	if ctx.author.guild_permissions.manage_emojis:
		r = requests.get(object)
		img = Image.open(BytesIO(r.content), mode='r')
		try:
			img.seek(1)

		except EOFError:
			is_animated = False

		else:
			is_animated = True

		if is_animated == True:
			await ctx.send("We do not support animated emojis!")

		elif is_animated == False:
			b = BytesIO()
			img.save(b, format='PNG')
			b_value = b.getvalue()
			emoji = await guild.create_custom_emoji(image=b_value, name=name)
			await ctx.send(f'Successfully created emoji: <:{name}:{emoji.id}>')

















token = os.getenv("TOKEN")
client.run(token)