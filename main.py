from __future__ import unicode_literals
import discord
import os
from keep_alive import keep_alive
from discord.ext import commands
from discord.utils import get
import random
import youtube_dl
from youtube_dl import YoutubeDL
import youtube_dl
import pafy
import urllib
from discord import FFmpegPCMAudio, PCMVolumeTransformer
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'mp3s/%(title)s.%(ext)s', 
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

from replit import db
keys = db.keys()
os.system("pip install cryptocode")
os.system("pip install PyNaCl")
import cryptocode
client = commands.Bot(command_prefix="unsc-")

db["randomnumber"] = random.randint(1, 10)


@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.command()
async def useless(ctx):
  await ctx.reply("useless")

@client.command()
async def suggestcommand(ctx):
  await ctx.reply("Suggestion?")
  msgstrt = await client.wait_for("message")
  msgcontent = msgstrt.content
  with open('suggest.txt', 'a') as f:
    f.writelines('\n')
    f.writelines(msgcontent)

@client.command()
async def ytaudio(ctx):
  await ctx.reply("Youtube download url?")
  urlmsg = await client.wait_for("message")
  url = urlmsg.content
  await ctx.send("Song downloading Give it a minute you will recieve a message when it has finished.")
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
  await ctx.send("Song Uploaded.")

@client.command()
async def listkeys(ctx):
  keys = db.keys()
  await ctx.reply(keys)

@client.command()
async def breadspam(ctx, user: discord.User=None):
  for i in range(5):
   user_string = '<@>'
   index = user_string.find('>')
   idstring = str(user.id)
   final_string = user_string[:index] + idstring + user_string[index:]
   print(final_string)
   await ctx.send(":bread:" + final_string)

@client.command()
async def spamchat(ctx, amount, msg):
  amountread = int(amount)
  for i in range(amountread):
    await ctx.send(msg)

@client.command()
async def spamdm(context, amount, user: discord.User, message):
    intnum = int(amount)
    for i in range(intnum):
      await user.send(message)

@client.command()
async def getUserId(ctx, user: discord.User=None): # defaults user to None if nothing is passed
    if not user: # you are not using an arg variable, you're using user
        userId = ctx.author.id
    else:
        userId = user.id # same as previous
    await ctx.send(userId)

@client.command()
async def randnumbers(ctx):
  for i in range(5):
    await ctx.channel.send(random.randint(1, 99999999999999999999999))

@client.command(pass_context=True)
async def assignkey(ctx):
  await ctx.reply('You will recieve a message with your private key do not share this with anyone.')
  user= str(ctx.author.id)
  print(user)
  db[user] = random.randint(1, 99999999999999999999999)
  await ctx.author.send(db[user])

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command()
async def pickrandom(ctx):
  await ctx.reply("Item 1?")
  item1 = await client.wait_for("message")
  db["item1"] = item1.content
  await ctx.channel.send("Item 2?")
  item2 = await client.wait_for("message")
  db["item2"] = item2.content
  ranint = random.randint(1, 2)
  if ranint == 1:
    item1win = db["item1"]
    await ctx.channel.send(item1win)
  elif ranint == 2:
    item2win = db["item2"]
    await ctx.channel.send(item2win)

@client.event
async def on_message_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.channel.send("Unknown command")

@client.command()
async def playmp3(ctx):
  await ctx.channel.send(os.listdir("mp3s"))
  await ctx.reply('mp3 to play?')
  mp3 = await client.wait_for("message")
  voice = get(client.voice_clients, guild=ctx.guild)
  voice.play(FFmpegPCMAudio("mp3s/" + mp3.content))

@client.command()
async def stopmp3(ctx):
  await ctx.reply('Stopping music.')
  voice = get(client.voice_clients, guild=ctx.guild)
  voice.stop()

@client.command()
async def immersed(ctx):
  await ctx.reply('command i wrote in vr from my new desktop')

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
