import discord
import random
import requests
import database
import json
import youtube_dl
import time
import sys
import subprocess
import sys
import os
from xp import XP
from discord.ext import commands
from functools import wraps
from discord.ext import commands
from xp_module import XP
import subprocess
subprocess.call([r'path where the batch file is stored\name of the batch file.bat'])

sys.path.append('/path/to/xp_module')
sys.path.append('/path/to/module')


# load data.json
with open('data.json', 'r') as f:
    data = json.load(f)

# Example usage
user_id = 1
username = "John Doe"
level = 1
xp = 0

user = {"user_id": user_id, "username": username, "level": level, "xp": xp}

data = database.add_user(data, user_id, username, level, xp)
data = database.update_xp(data, user_id, xp)
data = database.update_level(data, user_id, level)
user = database.get_user(data, user_id)



#mamba
print("\n[38;2;0;255;255mG[38;2;12;243;254me[38;2;24;231;253mm[38;2;36;219;252ma[38;2;48;207;251ma[38;2;60;195;250mk[38;2;72;183;249mt[38;2;84;171;248m [38;2;96;159;247md[38;2;108;147;246mo[38;2;120;135;245mo[38;2;132;123;244mr[38;2;144;111;243m [38;2;156;99;242mm[38;2;168;87;241ma[38;2;180;75;240mm[38;2;192;63;239mb[38;2;204;51;238ma[38;2;216;39;237m [38;2;228;27;236m<[38;2;240;15;235m3")
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())



#This way you can limit the login command to be used only 3 times per minute
def rate_limited(max_per_minute):
    min_interval = 60 / max_per_minute

    def decorate(func):
        last_time_called = [0.0]

        @wraps(func)
        async def rate_limited_function(*args, **kwargs):
            elapsed = time.perf_counter() - last_time_called[0]
            left_to_wait = min_interval - elapsed
            if left_to_wait > 0:
                await asyncio.sleep(left_to_wait)
            last_time_called[0] = time.perf_counter()
            return await func(*args, **kwargs)

        return rate_limited_function

    return decorate


@bot.command()
@rate_limited(max_per_minute=3)
async def login(ctx, *args):
    pass

#kitty cats
@bot.command()
async def cat(ctx):
    api_key = 'YOUR_API_KEY'
    headers = {'x-api-key': api_key}
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url, headers=headers)
    data = response.json()
    cat_url = data[0]['url']
    await ctx.send(cat_url)

#hallo reply 
@bot.command()
async def hello(ctx):
    await ctx.send("Hallo")


@bot.command(name='clear', help='Clears the chat')
async def clear(ctx, amount: int):
    try:
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Cleared {amount} messages.")
        await ctx.send("https://media3.giphy.com/media/oe33xf3B50fsc/giphy.gif")
    except discord.Forbidden:
        await ctx.send("I don't have permission to delete messages.")
    except discord.HTTPException:
        await ctx.send("Failed to delete messages.")



#cat-response 
    @bot.command()
    async def cat(ctx):
        response = requests.get('http://aws.random.cat/meow')
        cat_url = response.json()['file']
        await ctx.send(cat_url)
        

#kick
@bot.command()
@commands.has_any_role("Moderator")
async def kick (ctx, member:discord.User=None, reason =None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot kick the best man of the world")
        return
    if reason == None:
        reason = "For being a jerk!"
    message = f"You have been kicked from {ctx.guild.name} for {reason}"
    await ctx.channel.send(message)
    # await ctx.guild.kick(member, reason=reason)
    await ctx.channel.send(f"{member} is kicked!")
    await member.kick(reason=reason)


#ban
@bot.command()
@commands.has_any_role("Moderator","👑・Server Founder")
async def ban (ctx, member:discord.User=None, reason =None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself")
        return
    if reason == None:
        reason = "For being a jerk!"
    message = f"You have been banned from {ctx.guild.name} for {reason}"
    await ctx.channel.send(message)
    # await ctx.guild.ban(member, reason=reason)
    await ctx.channel.send(f"{member} is banned!")
    await member.ban(reason=reason)


#to run a python script from discord channel 
@bot.command()
async def runscript(ctx, script_name: str):
    output = subprocess.check_output(['python3', script_name])
    await ctx.send(output)
    
#help command
@bot.command()
async def help_command(ctx):
 commands = [command for command in bot.commands]
 response = ''
 for command in commands:
     respone += f'{command.name}: {command.brief}\n'
     await ctx.send(response)




#xp_system
xp_system = XP()

# Add XP points to a user




# Load data.json


# Example usage
data = database.add_user(data, user_id, username, level, xp)
data = database.update_xp(data, user_id, xp)
data = database.update_level(data, user_id, level)
user = database.get_user(data, user_id)

#verfiy-test
@bot.command()
async def add_reaction_role(ctx, message_id: int, emoji: str, role_name: str):
    message = await ctx.fetch_message(message_id)
    if message:
        guild = message.guild
        role = discord.utils.get(guild.roles, name=role_name)
        if role:
            await message.add_reaction(emoji)
            # Store the reaction role mapping in some persistent data store
        else:
            await ctx.send(f"Role with name '{role_name}' not found in the server.")
    else:
        await ctx.send(f"Message with ID '{message_id}' not found in this channel.")


bot.run("replace bot-token")