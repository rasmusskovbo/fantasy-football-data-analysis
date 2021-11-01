from os import path
import pandas as pd
import sqlite3

# set directory path
DATA_DIR = "C:/Users/rasmu/PycharmProjects/LTCW_Fantasy_Football/Ressources/ltcwff-files-0.9.0/data"

# create sql connection using sqlite3 module
conn = sqlite3.connect(path.join(DATA_DIR, 'fantasy.sqlite'))

#load csv into panda dataframes
player_game = pd.read_csv(path.join(DATA_DIR, 'game_data_sample.csv'))
player = pd.read_csv(path.join(DATA_DIR, 'game_data_player_sample.csv'))
game = pd.read_csv(path.join(DATA_DIR, 'game_2017_sample.csv'))
team = pd.read_csv(path.join(DATA_DIR, 'teams.csv'))

# create sql tables via panda dataframes
player_game.to_sql('player_game', conn, index=False, if_exists='replace')
player.to_sql('player', conn, index=False, if_exists='replace')
game.to_sql('game', conn, index=False, if_exists='replace')
team.to_sql('team', conn, index=False, if_exists='replace')

sql = """SELECT player_id, player_name AS name, pos FROM player WHERE team = 'MIA' AND pos == 'WR'"""
new_df = pd.read_sql(sql, conn)
new_df.head(10)


