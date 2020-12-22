import discord
import os
import requests
import json
import random
from emoji import EMOJI_ALIAS_UNICODE as EMOJIS




client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

AngryEmoji = EMOJIS[':rage:']

Nono_Words = [
  "die",
  "hang yourself",
]

COD_Warzone = [
  "warzone",
  "bunker",
  "bunkers",
  "codes"
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


def get_NorrisQuote():
  response = requests.get("https://api.chucknorris.io/jokes/random")
  json_data = json.loads(response.text)
  quote = json_data[0]
  return(quote)

def get_InspirationQuote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -by " + json_data[0]["a"]
  return(quote)  


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event 
async def on_message(message):
  if message.author == client.user:
    return

  # msg = message.content  

  if message.content.startswith('hello'):
    print('hello msg'.format(client))
    await message.channel.send('Hello! Welcome to the server. say -$hello, -inspire')

  if message.content.startswith('inspire'):
    print('inspiration quote'.format(client))
    quote = get_InspirationQuote()
    await message.channel.send(quote)

  if any(word in message.content for word in Nono_Words):
    print('No no word has been said'.format(client))
    await message.add_reaction(AngryEmoji)
    

  if any(word in message.content for word in COD_Warzone):
    print('warzone codes image'.format(client))
    await message.channel.send(file=discord.File('CardBunkers.jpg'))
    await message.channel.send(file=discord.File('Screenshot_3.png'))
    

  if any(word in message.content for word in sad_words):
      await message.channel.send(random.choice(start_encouragements))

  
client.run(os.getenv('TOKEN'))
