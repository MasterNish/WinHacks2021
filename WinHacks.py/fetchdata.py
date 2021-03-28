#   fetchdata.py
#   Gets league leader statistics from NBA-API and writes to text file "stats.txt"

import pandas as pd
from nba_api.stats.endpoints import leagueleaders       # importing league leaders

lleaders2020 = leagueleaders.LeagueLeaders(league_id = "00")    
lleaders_df = lleaders2020.get_data_frames()[0]         # creating data frame
#sort stats
counter = 0                                             # count amount of players in list
PlayerList = []
for index, row in lleaders_df.iterrows():               # iterate through dataframe
    statlist = []
    counter += 1
    if counter <= 60:
        PPG = round(row["PTS"]/row["GP"],1)             # calculate stat/game
        RPG = round(row["REB"]/row["GP"],1)             
        APG = round(row["AST"]/row["GP"],1)
        BPG = round(row["BLK"]/row["GP"],1)
        SPG = round(row["STL"]/row["GP"],1)
        statlist.append(row["PLAYER"])
        statlist.append(row["TEAM"])
        statlist.append(PPG)                            # append to list
        statlist.append(RPG)
        statlist.append(APG)
        statlist.append(BPG)
        statlist.append(SPG)
        PlayerList.append(statlist)
#write to file
stats = open("stats.txt", "w")                          # open file
for p in PlayerList:
    x = str(p)                                          # write list to file and strip square brackets
    y = x.strip("[")
    z = y.strip("]")
    stats.write("{} \n".format(z))                      
stats.close()