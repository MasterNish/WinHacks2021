import pandas as pd
from nba_api.stats.static import players
player_dict = players.get_players()

kd = [player for player in player_dict if player["full_name"] == "Kevin Durant"][0]
kd_id = kd["id"]
print(kd_id)

from nba_api.stats.static import teams
team_dict = teams.get_teams()
BKN = [team for team in team_dict if team["full_name"] == "Brooklyn Nets"][0]
print (BKN)
BKN_id = BKN["id"]

from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll

gamelog_kd = playergamelog.PlayerGameLog(player_id = "201142", season = "2019")
gamelog_kd_df = gamelog_kd.get_data_frames()[0]
