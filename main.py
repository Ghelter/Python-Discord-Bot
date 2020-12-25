import discord
import os
import requests
import json
import random
from badWords import Bad_Words
from emoji import EMOJI_ALIAS_UNICODE as EMOJIS





client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

AngryEmoji = EMOJIS[':rage:']

COD_Warzone = [
  "warzone",
  "bunker",
  "bunkers",
  "codes"
]

SoPa_gifs = [
  discord.File('source.gif')
]

COD_Images = [
  discord.File('Screenshot_3.png'),
  discord.File('CardBunkers.jpg'),
]

start_encouragements = [
  "cheer up!",
  "Hang in there.",
  "You got this!"
]

def get_InspirationQuote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -by " + json_data[0]["a"]
  return(quote)  


# async def coin(self, ctx):
#  n = random.randint(0, 1)
#  await ctx.send("Heads" if n == 1 else "Tails")

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event 
async def on_message(message):
  if message.author == client.user:
    return

  # messageContent = message.content  

  if message.content.startswith('hello'):
    print('hello msg'.format(client))
    await message.channel.send('Hello! Welcome to the server. say -$hello, -inspire, !coin to flip a coin')

  if message.content.startswith('inspire'):
    print('inspiration quote'.format(client))
    quote = get_InspirationQuote()
    await message.channel.send(quote)

  if message.content.startswith('!coin'):
    n = random.randint(0, 1)
    if n == 1:
      await message.channel.send("HEADS")
    else:
      await message.channel.send("TAILS")

  if any(word in message.content.lower() for word in Bad_Words):
    print('Bad word has been said'.format(client))
    await message.add_reaction(AngryEmoji)
    

  if any(word in message.content.lower() for word in COD_Warzone):
    print('warzone codes image'.format(client))
    await message.channel.send(file=discord.File('CardBunkers.jpg'))
    await message.channel.send(file=discord.File('Screenshot_3.png'))
    

  if any(word in message.content.lower() for word in sad_words):
      await message.channel.send(random.choice(start_encouragements))

  if len(message.content) > 0:
    for word in Bad_Words:
      if word in message.content:
        #To delete the message from chat
        #await message.delete()
        await message.channel.send('Bro!')
        await message.channel.send(file=discord.File('source.gif'))
  

keep_online()
client.run(os.getenv('TOKEN'))
