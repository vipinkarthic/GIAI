import discord
from discord.ext import commands
import json
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key="AIzaSyA93YLk9JvqRsyzOGSdBkMtuWEeuobOuUM")

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
    
model = genai.GenerativeModel('gemini-pro')

# response = model.generate_content("What is the meaning of life?")
# print(response.text)

def quickchat(message):
    response = model.generate_content(message)
    return response.text

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{bot.command_prefix}help"))
    print(discord.__version__)

@bot.command()
async def ai(ctx, *, message):
    await ctx.send(quickchat(message))


bot.run("MTE5ODk3MDM2MDQ0NDQ5Mzg4NQ.GSxDmP.4i9WzMTZ_Z9iiF-DlkNE9nOxMCFNqDvLPn8cGA")