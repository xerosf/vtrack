from API import Get, ReadConfig
from links import *
from datetime import datetime
from json import dump

region = ReadConfig('region')
puuid = ReadConfig('puuid')

today = datetime.now().strftime("%d%m%Y_")

def Main():
    matchList = Get(MatchHistory(region, puuid))

    fileCount = 0

    while True:
        try:
            fileName = f"{today}{fileCount}"
            with open(f'{fileName}.json', 'x') as f:
                dump(matchList, f, indent=4)
                return
        except FileExistsError:
            fileCount += 1

Main()