[Mamba test-bot] is a Discord bot built using Python. It is designed to provide users with a fun and interactive experience by responding to commands in chat. The bot offers a range of functionalities such as sending cat pictures, clearing chat, banning or kicking users, and running scripts from the channel. It also has a leveling system to reward users with experience points for their activity.
The bot uses the Discord API to communicate with users, and modules such as requests, database, json, youtube_dl, subprocess, os, discord, functools, and xp to handle various features. It has a login feature that is rate-limited to avoid spamming, and requires the user to log in to use other commands. Additionally, it has functionalities such as clearing chat and banning or kicking users that can only be accessed by moderators with appropriate roles.

Feel free to customize the bio as per your requirements, and provide additional details or instructions if needed.

!login: A command that can be used three times per minute, used for logging in.
!cat: A command that sends a random image of a cat.
!hello: A command that sends a "Hallo" message.
!clear [amount]: A command that clears a specified amount of messages from the chat.
!kick [user] [reason]: A command that can only be used by users with the "Moderator" role, used for kicking a specified user from the server.
!ban [user] [reason]: A command that can only be used by users with the "Moderator" or "Server Founder" roles, used for banning a specified user from the server.
!play [song]: A command that plays a specified song using a YouTube URL. The song is played in the voice channel the user is currently in.
!pause: A command that pauses the current song being played.
!resume: A command that resumes the current song being played.
!stop: A command that stops the current song being played and clears the queue.
!skip: A command that skips the current song being played and plays the next song in the queue.
!queue: A command that displays the current song queue.


> [pip install discord requests youtube_dl xp_module]
> discord: pip install discord
> requests: pip install requests
> youtube_dl: pip install youtube_dl
> xp_module: pip install xp_module
> functools: pip install functools
> database, json, time, sys, subprocess, and os are built-in modules in 


replace > /main.py > line = 194-bot-token 
replace > /main.py > line = 129 > the owners/admin
change the code @commands.has_any_role("Moderator","ðŸ‘‘ãƒ»Server Founder") > to your admim/owner role name 





Copyright (c) [2023] [Mamba]
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
