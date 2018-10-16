import random
from discord.ext.commands import Bot
from discord import Game

BOT_PREFIX = ("?", "!")
TOKEN = "NDcxNDI1NzM1ODExMTM3NTQ2.DjlaLQ.8YRYc9ENwZRifAbhJ_cn0ciC32c"

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name ='8ball', description="Answers a Y/N question.",
        brief="Answers from the divine, boi.",
        alaises=['8'],
        pass_context = True)
async def eight_ball(context):
    possible_responses = [
            'Hell no',
            'Not very likely',
            'Too hard to tell',
            'Very possibly',
            'Yes',
            ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Despacito"))
    print("Logged in as " + client.user.name)

@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    value = response.json() ['bpi'] ['USD'] ['rate']
    await client.say("Bitcoin price is: $" + value)

    
client.run('NDcxNDI1NzM1ODExMTM3NTQ2.DjlaLQ.8YRYc9ENwZRifAbhJ_cn0ciC32c')
