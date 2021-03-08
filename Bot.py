import urllib.parse
import requests
import re
import discord
import os , sys

from discord import Game
from discord import user
from discord.ext.commands import Bot
from Cred import *




BOT_PREFIX = '!'
TOKEN = botToken

client = Bot(command_prefix=BOT_PREFIX)


@client.event
async def on_ready():
    #await client.change_presence(game=Game(name="Games"))
    print("Logged in as " + client.user.name)


@client.command()
async def Hello(self, ctx):
    await self.channel.send("Hello")



@client.command()
async def jobb(self, Jobb="bagare", Stad="Stockholm", Antal="5"):

    print("Works so far 1")
    jobID = []
    jobURL = []
    jobHead = []
    jobText = []
    jobVac = []
    nums = 0
    jobs = 0
    jobInfo = []
    RealNumb = int(Antal) - 1
    jobInfo.append(Jobb)
    jobInfo.append(Stad)
    main_api = 'https://jobsearch.api.jobtechdev.se/search?'
    #params = {"nyckelord": Jobb + " " + Stad, "sida": "1", "antalrader": Antal}
    params = {"q" : Jobb ,"%20" : Stad}
    headers = {'accept': 'application/json','api-key' : Api}


    url = main_api + urllib.parse.urlencode(params)


  
    json_data = requests.get(url, headers=headers).json()

    print(json_data['hits'][0])

    while nums <= RealNumb:
        
        jobURL.append(json_data['hits'][nums]
                       ['webpage_url'])
                   
        jobHead.append(json_data['hits'][nums]
                       ['headline'])
        
        jobText.append(json_data['hits'][nums]
                       ['description']['text'])

        jobVac.append(json_data['hits'][nums]
                       ['number_of_vacancies'])
        nums += 1

    while jobs <= RealNumb:
        #await self.channel.send( + "\n" + )
        embed=discord.Embed(title= jobHead[jobs], url=jobURL[jobs], description= jobText[jobs], color=0xFF5733)
        embed.add_field(name = "Number of Vacancies" , value = jobVac[jobs], inline = False)
        await self.channel.send( embed = embed )
        jobs += 1


@client.command()
async def PaddySkills(self, ctx = client.user):
    links = ['Patience' 
    , 'Problem-Solving'
    ,'Strategizing'
    ,'Concentration'
    ,'Leadership'
    , 'Social Skills'
    ,'Logistics'
    ,'Risk Taking']
    games = [['Hitman','Thief', 'Startdew valley'], ['The Witness', 'Minecraft', 'Portal','Satisfactory'], ['Stellaris', 'Civilization' , 'Hearthstone', 'Crusader Kings'], ['?'], ['MMO', 'MOBA'] , ['MMO'] , ['Factorio' , 'Satisfactory', 'Sim City', 'Cities: Skylines'],['??']]
    InfoText = ['Do you enjoy games where long-term planning and waiting is important? Like being a sniper? Or waiting for something to grow? Or waiting around for that perfect drop or moment, for days and weeks on end? Then Patience is a skill you have!'
    , 'Do you like puzzles, the more complicated the better? Will you sit for days, trying different solutions? Do you avoid looking up the solution even when its easy to do? Will you try a puzzle over and over to find a more optimal solution even after youre solved it? Do you enjoy making your own puzzles in the games editor? Then welcome, Problem-Solver!'
    , 'Do you like games where the grand strategy is just as important as the moment-to-moment playing? Do you enjoy tweaking your forces for battle? Agonizing over spaceship designs? Trying to anticipate your opponents strategy in order to fine-tune you own? Focusing a whole team, army or empire on one united goal? Then you might be a Strategist!' 
    , 'Is laser-focused concentration something you crave in a game? Can you pursue a game goal for hours, for days, ignoring all else? Do you ignore the world around you until the task is done and realise your tea has gone cold and you forgot to eat? Then welcome on board, here is your Concentration badge!' 
    , 'Are you the one who organises others to get them to play? Do you lead a guild or organise raids? Do other players look to you when decisions have to be made? Do you make an effort to welcome new players, and make sure loot is evenly divided? Do you take responsibility when things go wrong, and share it when they go right? If so, then you just might be showing Leadership!'
    , 'Do you like gaming, but also enjoy the social contact that gaming brings? Like going to cons, extending your network, talking on Discord, taking part in Twitch streams, working with others to make your own levels or other mods, or just generally hanging out with other gamers to have fun? Then you probably have Social Skills.'
    , 'Some games dive deep into the nitty-gritty details of transportation, inventory management, packaging, supply flows and warehousing. Is tweaking a production flow your idea of a fun Friday evening? Will you work for hours to optimise a production cycle? Then Logistics might be your cup to tea.'
    ,'Some games encourage playing it safe, but maybe you like games where taking a risk is the way to progress. ']
    
    for link in links :
       fullGameText = ""
       print(links.index(link))
       for game in games[links.index(link)]:
            fullGameText += "" + game + " "

       embed=discord.Embed(title= link, url="", description= InfoText[links.index(link)], color=0xFF5733)
       embed.add_field(name = "Skills Gained from" , value = fullGameText, inline = False)
       await self.channel.send( embed = embed )


@client.command()
async def FindBy(self, ctx = "Patience"):
    links = ['Patience' 
    , 'Problem-Solving'
    ,'Strategizing'
    ,'Concentration'
    ,'Leadership']
    games = [['Hitman','Thief', 'Startdew valley'], ['The Witness', 'Minecraft', 'Portal','Satisfactory'], ['Stellaris', 'Civilization' , 'Hearthstone', 'Crusader Kings'], ['?'], ['MMO', 'MOBA']]
    InfoText = ['Do you enjoy games where long-term planning and waiting is important? Like being a sniper? Or waiting for something to grow? Or waiting around for that perfect drop or moment, for days and weeks on end? Then Patience is a skill you have!'
    , 'Do you like puzzles, the more complicated the better? Will you sit for days, trying different solutions? Do you avoid looking up the solution even when its easy to do? Will you try a puzzle over and over to find a more optimal solution even after youre solved it? Do you enjoy making your own puzzles in the games editor? Then welcome, Problem-Solver!'
    , 'Do you like games where the grand strategy is just as important as the moment-to-moment playing? Do you enjoy tweaking your forces for battle? Agonizing over spaceship designs? Trying to anticipate your opponents strategy in order to fine-tune you own? Focusing a whole team, army or empire on one united goal? Then you might be a Strategist!' 
    , 'Is laser-focused concentration something you crave in a game? Can you pursue a game goal for hours, for days, ignoring all else? Do you ignore the world around you until the task is done and realise your tea has gone cold and you forgot to eat? Then welcome on board, here is your Concentration badge!' 
    , 'Are you the one who organises others to get them to play? Do you lead a guild or organise raids? Do other players look to you when decisions have to be made? Do you make an effort to welcome new players, and make sure loot is evenly divided? Do you take responsibility when things go wrong, and share it when they go right? If so, then you just might be showing Leadership!']
    gameCheck = False
    gamesIndex = 0
    fullGameText = ""
    for items in games:
        print(items)
        if(ctx in items):
            print(games.index(items))
            gamesIndex = games.index(items)
            gameCheck = True
        else:
            print("Fail")
        

    
    if gameCheck == False:
         for game in games[links.index(ctx)]:
            fullGameText += "" + game + " "

         embed=discord.Embed(title= links[links.index(ctx)], url="", description= InfoText[links.index(ctx)], color=0xFF5733)
         embed.add_field(name = "Skills Gained from" , value = fullGameText, inline = False)
    else:
         for game in games[gamesIndex]:
            fullGameText += "" + game + " "

         embed=discord.Embed(title= links[gamesIndex], url="", description= InfoText[gamesIndex], color=0xFF5733)
         embed.add_field(name = "Skills Gained from" , value = fullGameText, inline = False)

    await self.channel.send( embed = embed )
      




client.run(TOKEN)
