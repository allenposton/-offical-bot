print("I am alive master")
from unittest import async_case
import ffmpeg
from discord import Member
from discord.ext.commands import has_permissions
from async_timeout import timeout
import pytz
import hikari
import os
import DiscordEconomy
import tracemalloc
import music
import discord
from discord.ext import commands
from random import randint
from discord import FFmpegPCMAudio


from youtube_search import YoutubeSearch




  

import aiohttp
from youtube_dl import YoutubeDL
import os

import discord
from discord.ext import tasks, commands
import random
import json
from discord import FFmpegPCMAudio
import Languages

import youtube_dl

import requests

def handler(pd: "pipedream"):
  headers = {"Authorization": f'Bot {pd.inputs["discord_bot"]["$auth"]["bot_token"]}'}
  r = requests.get('https://discord.com/api/users/@me', headers=headers)
  # Export the data for use in future steps
  return r.json()

def handler(pd: "pipedream"):
  # Reference data from previous steps
  print(pd.steps["trigger"]["context"]["id"])
  # Return data for use in future steps
  return {"foo": {"test":True}}

def handler(pd: "pipedream"):
  # Reference data from previous steps
  print(pd.steps["trigger"]["context"]["id"])
  # Return data for use in future steps
  return {"foo": {"test":True}}

  

import asyncio
#import DiscordUtils
import functools
import itertools


import discord
import os
import io
import traceback
import textwrap
import inspect
import aiohttp
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import redirect_stdout
from discord.ext import commands
import json
import subprocess
import asyncio
import math
import re 
import discum
import random
import youtube_dl
import lightbulb
import keep_alive
import requests
from async_timeout import timeout
import time
from datetime import datetime


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
intents=discord.Intents.all()
intents = discord.Intents.default()
intents.message_content = True
from pretty_help import PrettyHelp


intents = discord.Intents().all()

token = os.environ['token']



# Import the command handler
import lightbulb

# Run the bot
# Note that this is blocking meaning no code after this line will run
# until the bot is shut off
  
client = commands.Bot(command_prefix=',',intents=intents)



_afk = []  

bot_fox = commands.Bot(command_prefix=',', intents = intents,help_command=PrettyHelp( no_category = 'test commands', description = "i am learning code with some of these commands"))


@bot_fox.command()
async def test(ctx):
  embed=discord.Embed(title="Poketwo News", description="This role allows access to view updates from Poketwo's Community, from <#1048807062282440834>")
  embed.set_thumbnail(url="https://styles.redditmedia.com/t5_2pw9jd/styles/communityIcon_71vnwum279p51.png?width=256&s=70c83d8d821dfc5bfc8f96d01019186a836da790")
  msg = await ctx.send(embed=embed)
  await msg.add_reaction("✅")

  await ctx.send(msg)


async def run(ctx, arg1):
  ctx.send(os.system(arg1))


@bot_fox.command(pass_context=True)
async def gif(ctx, *, search):
    embed = discord.Embed(colour=discord.Colour.blue())
    session = aiohttp.ClientSession()

    if search == '':
        response = await session.get('https://api.giphy.com/v1/gifs/random?api_key=ICQxdYi29ul8p8uKkIFjrLzj17fr1zBx')
        data = json.loads(await response.text())
        embed.set_image(url=data['data']['images']['original']['url'])
    else:
        search.replace(' ', '+')
        response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=ICQxdYi29ul8p8uKkIFjrLzj17fr1zBx&limit=10')
        data = json.loads(await response.text())
        gif_choice = random.randint(0, 9)
        embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

    await ctx.send(embed=embed)


@bot_fox.command()
async def rp(ctx,ranpoke):
  
  url = "https://pokeapi.co/api/v2/pokemon/"
  x= url
  r = requests.get(f'{x}{ranpoke}')
  
  packages_json = r.json()
  packages_json.keys


  napo = packages_json["name"]
  napo2= packages_json["abilities"]

  embed = discord.Embed(title = "A wild pokémon has appeared!", color = discord.Color.random())
  embed.set_thumbnail(url = f"https://play.pokemonshowdown.com/sprites/ani/{napo}.gif")
  embed.add_field(name="Pokemon Name: ",value = napo ,inline=False)
  embed.add_field(name="abilities",value=napo2 ,inline=False)
  await ctx.send(embed = embed)

  
@bot_fox.command()
@commands.has_role("Admin")
async def addrole(ctx,role):
    member = ctx.message.author
    await ctx.add_roles(role)
    await ctx.send(f"{member.mention} had created a role named {role}")
    




import typing
import discord


@bot_fox.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await ctx.send(f'{ctx.author.mention} has locked {channel.mention}, {channel.mention} is now :lock: ')
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

@bot_fox.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await ctx.send(f'{ctx.author.mention} has unlocked {channel.mention}, {channel.mention} is now :unlock:')
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

@lock.error
async def lock_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to lock channels".format(ctx.message.author)
        await ctx.send(text)
      




import discord
from discord import app_commands
from discord.ext import commands

@bot_fox.command()
async def help_fox(ctx, args=None):
    help_embed = discord.Embed(title="My Bot's Help!")
    command_names_list = [x.name for x in bot_fox.commands]

    help_embed.set_thumbnail(url=bot_fox.user.avatar.url)

    # If there are no arguments, just list the commands:
    if not args:
        help_embed.add_field(
            name="List of supported commands:",
            value="\n".join([str(i+1)+". "+x.name for i,x in enumerate(bot_fox.commands)]),
            inline=False
        )
        help_embed.add_field(
            name="Details",
            value="Type `,help <command name>` for more details about each command.",
            inline=False
        )

    # If the argument is a command, get the help text from that command:
    elif args in command_names_list:
        help_embed.add_field(
            name=args,
            value=bot_fox.get_command(args).help
        )

    # If someone is just trolling:
    else:
        help_embed.add_field(
            name="Nope.",
            value="Don't think I got that command, boss!"
        )

    await ctx.send(embed=help_embed)



          
import discord
from discord.ext import commands

import tracemalloc

tracemalloc.start()



import tracemalloc

tracemalloc.start()
@bot_fox.command()
@commands.cooldown(1, 15, commands.BucketType.user)

async def hug(ctx, *, user: discord.Member = None):
    with open("hug.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))   
        x = random.choice(words)

    if user == bot_fox.user: 
       msg =  await ctx.send(f'Aww, "Thank You!"  {ctx.author.mention}')
       emoji='😄'      
       await ctx.message.add_reaction(msg,emoji)  #:pokelove:1055822955084513303


  
    elif user:

       embed = discord.Embed(title=f"Hugs {user}", color=0xffffff)

       embed.set_image(url=x)
       await ctx.send(embed=embed)

    else:
        await ctx.send("if you wanna hug anyone just do:` hug <@mention .user>`")


@bot_fox.command()
async def kill(ctx, *, member: discord.Member = None):
    with open("kill.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))   
        x = random.choice(words)

    if member == bot_fox.user:
                 await ctx.reply("..." , delete_after=40)

  
    elif member:

      embed = discord.Embed(title=f"Kills {member}",color=0xffffff)

      embed.set_image(url=x)
      await ctx.send(embed=embed)

    else:
        await ctx.send("command is missing. ,kill `[@mention_member]`")


@bot_fox.command()
async def info(ctx,*, member: discord.Member):
      embed=discord.Embed(description=f"About {member}")
      joined = member.joined_at.strftime("%b %d, %Y, %I:%M %p")
      registered =  member.created_at.strftime("%b %d, %Y, %I:%M %p")

      embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)      
      embed.set_image(url=str(member.display_avatar.url))
      embed.add_field(name="Joined", value=joined, inline=False)
      embed.add_field(name="Registered", value=registered, inline=False)
      embed.add_field(name=f"Roles [{len([role.mention for role in member.roles])}]",value=f"{' '+' '.join ([role.mention for role in member.roles [1:]])}",inline=False)

  
      await ctx.send(embed=embed)

@bot_fox.command(name="ping", help="see ping")
async def ping(ctx):
        message = await ctx.send("Pong!")
        await message.edit(content=f" Pong: **{round(bot_fox.latency *1000)}ms **")



@bot_fox.command()
async def joined(ctx,*, member: discord.Member):
    await ctx.send(f'{member} joined on {member.joined_at}')



t=True
@bot_fox.command(pass_context=True, description=',cd [any number between 1-150]')
@commands.cooldown(1, 60, commands.BucketType.user)
async def cd(ctx, time: int):
    with open("cela.txt", "r") as file:
      allText = file.read()
      words = list(map(str, allText.split()))   
      x = random.choice(words)

      while time > 150:
        await ctx.send("https://media.discordapp.net/attachments/1048796812531728404/1049042029184831509/cute-fox-is-bored-illustration-vector_617647-8.png?width=120&height=100")
        await ctx.reply("Bruh [the limit is 150]")
        await asyncio.run(stop())
        break
        
        #error point
        while time < 100:
          async with ctx.typing():
            await ctx.send("Loading ...",delete_after=4.9)
            await asyncio.sleep(3)
            await ctx.send(f"Counting down from {time} ")
        #end off error forever loop
      async with ctx.typing():
            await ctx.send(f"{ctx.author.mention} used ,cd",delete_after=4.9)
            await asyncio.sleep(3)
            await ctx.send(f"Counting down from {time} ")
            await ctx.send(time, delete_after=10)
      while time > 0:
        time-= 1        # Sleep for 1 second
        await asyncio.sleep(1)
        await ctx.send(f'{time}' ,delete_after=10)
      await ctx.send(f"Countdown has completed")
      await ctx.reply(f"{x}")

  



def stop():
  pass


@bot_fox.event
async def on_command_error(ctx , error):

  if isinstance(error, commands.CommandOnCooldown):
          reactions = '⌛'
          reaction2 = '🦊'
          await ctx.author.send(f"sorry please try again , after:  **`{round(error.retry_after)}`** seconds", delete_after=10)

          await ctx.message.add_reaction(reactions)
          await ctx.message.add_reaction(reaction2)



#delete if 


# Say hi Functoin
collection = []



@bot_fox.command(name="hi",description='Yay you made it, this is for starters')
@commands.cooldown(1, 10, commands.BucketType.user)
async def hi(ctx):
  with open("hello.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))   
    x = random.choice(words)
    await asyncio.sleep(1.5)
    mention = ctx.author.mention
    response = f"Hello {mention} !"
    await ctx.send(response, delete_after=10.5)    
    await ctx.send(x)
    await asyncio.sleep(2.5)
    await ctx.send(" --    こんにちわ   -- ", delete_after=4.23)
    async with ctx.typing():
      await asyncio.sleep(2.7)
      await ctx.reply("**PRO TIP : ** If you need help just do |`,help`|  :wink: -> k" , delete_after=50)

# Say bye Functoin
@bot_fox.command(name="bye",description='Send others a sign of you being ready to leave ')

async def bye(ctx):

    response = f"Good Bye {ctx.author} !"
    await ctx.say(f"{ctx.author} said: "+ response)
    await ctx.reply(response, delete_after=19)    
    await asyncio.sleep(1)
    await ctx.say(response)   






@bot_fox.command(pass_context=True,)
@has_permissions(administrator=True, ban_members=True)
async def meme(ctx,):
    embed = discord.Embed(title="", description="im not responesable for this meme is ")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemer/new.json?sort=hot ')as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 80)]['data']['url'])
            await ctx.send(embed=embed)

async def quote(ctx):
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  await ctx.reply(quote)




@bot_fox.command()
async def umm(ctx):
  pixelPlanetUrl = requests.get("https://app.pixelencounter.com/api/basic/planets?")
  json_data = json.loads(pixelPlanetUrl.text)
  image = json_data[0]['q'] + " -" + json_data[0]['a']
  await ctx.reply(image)



#but if you want to make the bot change status every 5 minutes try this :



status1=[
  discord.Status.dnd,
  discord.Status.idle,
  discord.Status.online
]

@bot_fox.event
async def on_ready():
  with open("online.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.splitlines()))   
        e = random.choice(words)
        y=random.choice(status1)
  print("---------------------------------------------")
  print(f"Discord bot : {bot_fox.user}")
  print("Has successfully logged in = True")
  print(f"Current status: discord.status.{y}")
  print("---------------------------------------------")

  print(f"Welcome : {bot_fox.user}")
  print("---------------------------------------------")
  time.sleep(2)

  print("-------------------------")

  with open("alive.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.splitlines()))   
    x = random.choice(words)
  with open("bot_status.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.splitlines()))   
    s = random.choice(words)
    for guild in bot_fox.guilds:
        for channel in guild.text_channels :
            if str(channel) == "002-foxy-test🦊":
                await channel.purge()#deletes all messages
                await channel.send(f'{x}')
        print("=============")

        print('Active in {}\n Member Count {}'.format(guild.name,guild.member_count))

        time.sleep(0.5)

    my_time =  pytz.timezone("America/Indiana/Indianapolis")
    currentDateAndTime = datetime.now(my_time)
  

    currentTime = currentDateAndTime.strftime("%I:%M")

    
  await bot_fox.change_presence(status=y)
  await bot_fox.change_presence(status=y,activity=discord.Activity(type=discord.ActivityType.watching, name =f'{s} {" since"} {currentTime}'))
  print("-------------------------")
  print("Enjoy coding")
  print("-------------------------")

  print("--------------- -> INFO <- ------------------")
  print(f"Discord bot : {bot_fox.user}")
  print("Has successfully logged in = True")
  print(f"Current status: discord.status.{y}")
  print("---------------------------------------------")

  print(f"Welcome : {bot_fox.user}")
  print("---------------------------------------------")

  
  if y == discord.Status.idle:
    print("idle status updated")
    
    await bot_fox.change_presence(status=y,activity=discord.Activity(type=discord.ActivityType.listening, name =",help"))
  else:
      print("idle status is not true")
      for guild in bot_fox.guilds:
         
       await bot_fox.change_presence(status=y,activity=discord.Activity(type=discord.ActivityType.watching, name =f"over {len(bot_fox.guilds)} servers."))

@tasks.loop(seconds = 10) # repeat after every 10 seconds
async def change():
      info=[
        discord.ActivityType.playing,
        discord.ActiviyType.watching,
        discord.ActivityType.listening
      ]
      name=[
         "Foxy games"
         f"over {len(bot_fox.guilds)} servers."
         ",help :fox:"
       ]

      k = random.choice(info)
      if x == discord.ActivityType.playing:
         await bot_fox.change_presence(status=y,activity=discord.Activiy(type=k,name= "Foxy games"))






import os

#db = sqlite3.connect('poke2auto.db')
#cur = db.cursor()
import discord
from discord.ext import commands
from discord.ext import tasks

token = os.environ['token']





global x
x = "[AFK] "

#AFK


#say
import tracemalloc

tracemalloc.start()

@bot_fox.command(name='say')
async def say(ctx, *, content):
    await ctx.reply(content)

print("music file is activated")


@bot_fox.event
async def on_message(message):
    if " " in message.content:
       message.replace(" ", '_')

      



youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn',
}
import discord
from discord.ext import commands
import random
import asyncio
import itertools
import sys
import traceback
from async_timeout import timeout
from functools import partial
import youtube_dl
from youtube_dl import YoutubeDL

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

ytdlopts = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'  # ipv6 addresses cause issues sometimes
}

ffmpegopts = {
    'before_options': '-nostdin',
    'options': '-vn'
}

ytdl = YoutubeDL(ytdlopts)


class VoiceConnectionError(commands.CommandError):
    """Custom Exception class for connection errors."""


class InvalidVoiceChannel(VoiceConnectionError):
    """Exception for cases of invalid Voice Channels."""


class YTDLSource(discord.PCMVolumeTransformer):

    def __init__(self, source, *, data, requester):
        super().__init__(source)
        self.requester = requester

        self.title = data.get('title')
        self.web_url = data.get('webpage_url')
        self.duration = data.get('duration')

        # YTDL info dicts (data) have other useful information you might want
        # https://github.com/rg3/youtube-dl/blob/master/README.md

    def __getitem__(self, item: str):
        """Allows us to access attributes similar to a dict.
        This is only useful when you are NOT downloading.
        """
        return self.__getattribute__(item)

    @classmethod
    async def create_source(cls, ctx, search: str, *, loop, download=False):
        loop = loop or asyncio.get_event_loop()

        to_run = partial(ytdl.extract_info, url=search, download=download)
        data = await loop.run_in_executor(None, to_run)

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        embed = discord.Embed(title="", description=f"Queued [{data['title']}]({data['webpage_url']}) [{ctx.author.mention}]", color=discord.Color.green())
        await ctx.send(embed=embed)

        if download:
            source = ytdl.prepare_filename(data)
        else:
            return {'webpage_url': data['webpage_url'], 'requester': ctx.author, 'title': data['title']}

        return cls(discord.FFmpegPCMAudio(source), data=data, requester=ctx.author)

    @classmethod
    async def regather_stream(cls, data, *, loop):
        """Used for preparing a stream, instead of downloading.
        Since Youtube Streaming links expire."""
        loop = loop or asyncio.get_event_loop()
        requester = data['requester']

        to_run = partial(ytdl.extract_info, url=data['webpage_url'], download=False)
        data = await loop.run_in_executor(None, to_run)

        return cls(discord.FFmpegPCMAudio(data['url']), data=data, requester=requester)


import discord
import youtube_dl

from discord.ext import commands


#=============== MUSIC









@bot_fox.command()
@has_permissions(administrator=True, ban_members=True)

async def c(ctx):
  await ctx.channel.purge()#deletes all messages



@c.error
async def ar_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to purge ".format(ctx.message.author)
        await ctx.send(text)
      



@bot_fox.event
async def on_message(msg):
    
    await bot_fox.process_commands(msg)






  
from discord.ext import commands

from discord.ext.commands import has_permissions, MissingPermissions






import discord
from discord.ext import commands
import youtube_dl
import asyncio
import discord
from discord.ext import commands
import youtube_dl
class music(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("You're not in a voice channel!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self,ctx,url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            if not vc:
                      await ctx.invoke(self.connect_)

                      player = self.get_player(ctx)


            source2 = await YTDLSource.create_source(ctx, url, loop=self.bot_fox.loop, download=False)

            await player.play(source)
            vc.play(source)
            await ctx.reply(f"Now playing {url}") 
    
    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.channel.send("Paused ⏸")
    
    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.channel.send("resume ⏯")




class special(commands.Cog):
  def __init__(self, bot_fox):
        self.bot_fox = bot_fox

  @commands.has_permissions(manage_channels=True)
  async def lock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('Channel locked.')


from youtubesearchpython import SearchVideos


class music(commands.Cog):
    def __init__(self, bot_fox):
        self.bot_fox = bot_fox
    
    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("You're not in a voice channel!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
            await ctx.reply(f"I connected to you vc channel titled : {voice_channel.mention} ")
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self,ctx,url:str):
        ctx.voice_client.stop()
        await ctx.send("please wait")
        search = SearchVideos(url, offset = 1, mode = "json", max_results = 3)
        r = search.result()
        res = json.loads(r)
        res1 = res['search_result']
        res2 = res1[0]
        res_fin = res2['link']

        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {
          'format':"bestaudio",
          'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
          'restrictfilenames': True,
          'noplaylist': True,
          'nocheckcertificate': True,
          'ignoreerrors': False,
          'logtostderr': False,
          'quiet': True,
          'no_warnings': True,
          'default_search': 'auto',
          'source_address': '0.0.0.0'
        }
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(res_fin, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            results = YoutubeSearch(url2, max_results=1).to_json()
            await ctx.reply(f"**Now Playing:** {res_fin} ")

            vc.play(source)
            vc.play(results)
            print (results)
            print(f"Now Playing {res_fin}")

    
    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.channel.send("Paused ⏸")
    
    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.channel.send("resume ⏯")



class afk(commands.Cog):
  def __init__(self,bot_fox):
    self.bot_fox = bot_fox
    self.data = []

  @commands.command()
  @commands.cooldown(1, 1, commands.BucketType.user)

  async def afk(self, ctx, args=None):
    msg = args

    self.data.append(ctx.author.id)
    self.data.append(msg)
      
    await ctx.send(f"{ctx.author.mention} **I set your AFK to** - AFK: {args} ",delete_after=15)
      
  @commands.Cog.listener()
  async def on_message(self, message):
    for i in range(len(self.data)):
      if (f"<@{self.data[i]}>" in message.content) and (not message.author.bot):
        await message.channel.send(f"<@{self.data[i]}> is currently AFK, reason: {self.data[i+1]}",delete_after=15)
        return None
        break

  @commands.Cog.listener()
  async def on_typing(self, channel, user, when):
    if user.id in self.data:
      i = self.data.index(user.id)
      self.data.remove(self.data[i+1])
      self.data.remove(user.id)
   
      await channel.send(f"Welcome back {user.mention}, I removed your AFK!", delete_after=15)





@bot_fox.event
async def setup(bot_fox):
   await bot_fox.add_cog(music(bot_fox))
  
   await bot_fox.add_cog(afk(bot_fox))






asyncio.get_event_loop().run_until_complete(setup(bot_fox))



#host alive
from keep_alive import keep_alive #keep keep_alive and import toghther


keep_alive()
#---end---

if __name__ == '__main__':
  bot = discum.Client(token= os.environ['token'])
  bot_fox.run(token)

  
  client.run(token)
#==----
 
