import os
from webexteamsbot import TeamsBot
from webexteamsbot.models import Response
import requests
import json
import random


# Retrieve required details from environment variables
bot_email = os.getenv("TEAMS_BOT_EMAIL")
teams_token = os.getenv("TEAMS_BOT_TOKEN")
bot_url = os.getenv("TEAMS_BOT_URL")
bot_app_name = os.getenv("TEAMS_BOT_APP_NAME")

# Create a Bot Object
bot = TeamsBot(
    bot_app_name,
    teams_bot_token=teams_token,
    teams_bot_url=bot_url,
    teams_bot_email=bot_email,
)

# set the apikey and limit
key = 'TENORAPIKEY'
apikey = os.getenv(key) 
lmt = 1


# A simple command that returns a basic string that will be sent as a reply
def do_something(incoming_msg):
    """
    Sample function to do some action.
    :param incoming_msg: The incoming message object from Teams
    :return: A text or markdown based reply
    """
    return "i did what you said - {}".format(incoming_msg.text)

def SearchGif(incoming_msg, search_term):
    """
    Function to retrieve a meme on brooklyn99.
    :param incoming_msg: The incoming message object from Teams
    ;param search_term: What to search for
    :return: A text or markdown based reply
    """

    # get the top 8 GIFs for the search term
    r = requests.get(
        "https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

    if r.status_code == 200:
        top_gif = json.loads(r.content)
        print(json.dumps(top_gif, indent=4, sort_keys=True))
        for i in range(len(top_gif['results'])):
            url = top_gif['results'][i]['media'][0]['gif']['url'] 
            print (url)
    else:
        top_gif = None

    response = Response()
    response.files = url

    return response

# A command that returns a funny meme from the office
def TheOffice(incoming_msg):
    """
    Function to retrieve a meme on the office.
    :param incoming_msg: The incoming message object from Teams
    :return: A text or markdown based reply
    """
    # our test search
    search_term = "the office"

    return SearchGif(incoming_msg, search_term)
   
def Brooklyn99(incoming_msg):
    """
    Function to retrieve a meme on brooklyn99.
    :param incoming_msg: The incoming message object from Teams
    :return: A text or markdown based reply
    """
    # our test search
    search_term = "brooklyn99"

    return SearchGif(incoming_msg, search_term)

def ParksAndRecreation(incoming_msg):
    """
    Function to retrieve a meme on Parks and Recreation.
    :param incoming_msg: The incoming message object from Teams
    :return: A text or markdown based reply
    """
    # our test search
    search_term = "parks and rec"

    return SearchGif(incoming_msg, search_term)

def MrRobot(incoming_msg):
    """
    Function to retrieve a meme of Mr.Robot.
    :param incoming_msg: The incoming message object from Teams
    :return: A text or markdown based reply
    """
    # our test search
    search_term = "Mr.Robot"

    return SearchGif(incoming_msg, search_term)

def SchittsCreek(incoming_msg):
    """
    Function to retrieve a meme on schittscreek.
    :param incoming_msg: The incoming message object from Teams
    :return: A text or markdown based reply
    """
    # our test search
    search_term = "schittscreek"

    return SearchGif(incoming_msg, search_term)

def Brawlstars(incoming_msg):
    """
    Function to retrieve a meme on brooklyn99.
    :param incoming_msg: The incoming message object from Teams
    :return: A text or markdown based reply
    """
    # our test search
    search_term = "brawlstars"

    return SearchGif(incoming_msg, search_term)

def GreysAnatomy(incoming_msg):
    """
    Function to retrieve a meme on greys anatomy.
    :param incoming_msg: The incoming message object from Teams
    :return: A text or markdown based reply
    """
    # our test search
    search_term = "greysanatomy"

    return SearchGif(incoming_msg, search_term)

def Coding(incoming_msg):
    """
    Function to retrieve a meme on brooklyn99.
    :param incoming_msg: The incoming message object from Teams
    :return: A text or markdown based reply
    """
    # our test search
    search_term = "coding"

    return SearchGif(incoming_msg, search_term)

def Harden(incoming_msg):
    """
    Function to retrieve a meme on James Harden.
    :param incoming_msg: The incoming message object from Teams
    :return: A text or markdown based reply
    """
    # our test search
    search_term = "james harden"

    return SearchGif(incoming_msg, search_term)

def Magic8Ball(incoming_msg):
    """
    Function to shake a magic 8 ball.
    :param uncoming_msg: The incoming message object from Teams
    :return: A text or mrakdown based reply
    """
    list = ["Yes, most definitely!", "The chances are high!", "Not likely!", "May the odds be ever in your favor.", 
			"You got no shot, kid.", "Try it out and see!", "23% of working", "99.9% success rate",
			"Congratulations, yes!", "Ask a probably question," "Ask again later", "Better not tell you now",
           "Cannot predict now", "Concentrate and ask again", "Don't count on it"
	]

    X = ("Your Response Is: ")
    return X + random.choice(list)

# Add new commands to the box.
bot.add_command("/dosomething", "Help, for do something.", do_something)
bot.add_command("/TheOffice", "Post a meme from The Office.", TheOffice)
bot.add_command("/Brooklyn99", "Post meme from Brooklyn99.", Brooklyn99)
bot.add_command("/ParksAndRecreation", "Post a meme from Parks, and Recreation.", ParksAndRecreation)
bot.add_command("/MrRobot", "Post a meme from Mr.Robot.", MrRobot)
bot.add_command("/SchittsCreek", "Post a meme from Schittscreek.", SchittsCreek)
bot.add_command("/Brawlstars", "Post a meme from brawlstars.", Brawlstars)
bot.add_command("/Coding", "Post memes about coding.", Coding)
bot.add_command("/Magic8Ball", "Post a random Magic 8 Ball response.", Magic8Ball)
bot.add_command("/Harden", "Post a meme of James Harden", Harden)
bot.add_command("/GreysAnatomy", "Post a meme of Greys Anatomy.", GreysAnatomy)

if __name__ == "__main__":
    # Run Bot
    bot.run(host="0.0.0.0", port=5000)