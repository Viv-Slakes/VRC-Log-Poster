 # A very simple discord bot that automatically posts your vrchat log to discord with a set interval or when manually triggered.
 
 A Community i am in uses a AFK Account to keep a grouppublic instance live and to improve moderation quality  (e.g. to moderate when a user inputs malicious or disturbing content into the video player) having easy access for staffmembers is a very useful thing to have. 

Please keep in mind that this log might contain information you consider private, so before giving people access to your log make sure you can trust them.

Setup is very simple and (unless you have set up a custom path for your VRChat cache) all you need to do is input the relevant information into these variables.
```
TOKEN = 'YOURTOKEN' # Your Bot Token
GUILD_ID = YOURSERVERID  # The ID of your server (guild)
CHANNEL_ID = YOURCHANNELID  # The ID of the channel where bot will post files
COMMAND_CHANNEL_ID = YOURCOMMANDCHANNELID  # The ID of the channel where bot will respond to commands
INTERVAL_MINUTES = 20  # The interval in minutes at which the bot should post files
COMMAND_PREFIX = '/'  # The prefix for commands
COMMAND_NAME = 'vrclog'  # The name of the command to respond to
```

I am in no way responsible for how or if you use this bot and i do not offer any kind of support for this. It was made for my own use and whether or not it works lies in your hands.
