from re import match
import os
import discord
from dotenv import load_dotenv
load_dotenv()

__version__ = '0.1.0'

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('TEST_GUILD')

client = discord.Client()

SERVER_ID = os.getenv('TEST_SERVER_ID')


@client.event
async def on_message(message):
    id = client.get_guild(SERVER_ID)

    if message.author.bot:
        return

    if client.user.mentioned_in(message) and message.mention_everyone is False:
        await message.add_reaction('👀')

    print("VIA ENV", os.getenv("SELF"))
    print("VIA CLIENT", client.user.id)


@client.event
async def on_ready():

    print('Logged in as')
    print(f'Bot-Name: {client.user.name}')
    print(f'Bot-ID: {client.user.id}')
    print(f'Discord Version: {discord.__version__}')
    print(f'Bot Version: {__version__}')
    client.AppInfo = await client.application_info()
    print(f'Owner: {client.AppInfo.owner}')
    print('------')

    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


client.run(TOKEN)


# 1) Prints words randomly from lyrics (Need lyrics here in JSON)

# 2) Responds with quotes to people if they call on him.

# 3) Randomly scrapes web and offers sales of vintage sneakers

# 4) Data on Maine trappers association
