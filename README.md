# no u bot for discord
Discord bot that replies with some variant of "no u" to any reply that contains "no u".

## How to set this up:
### 1. Install the rewritten discord.py dependency for python
``
python3 -m pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip
``
### 2. Add your API keys
For information on how to generate a Discord app and API keys, consult the following:

https://discordapp.com/developers/docs/intro

Once you have your API keys, put them in a file called
``
credentials.py
``
in the root of the project with the following contents:
```
TOKEN = '<your-app-token>'
KEY = '<your-user-key>'

BOTID = '<your-app-id>'
OWNERID = '<your-user-id>'
```
### 3. Run it
In the root of the project, use the command
``
python3 no_u_bot_discord.py
``
