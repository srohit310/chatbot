import discord
from Bot.bot import ChatBot
import nltk
nltk.download('punkt')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if not message.author.bot:
        reply = ChatBot.chat(message.content)
        await message.channel.send(reply)


def read_token():
    with open("tokens.txt") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()
print("The bot has started")
client.run(token)
