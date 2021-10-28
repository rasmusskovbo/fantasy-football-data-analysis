from os import path
import pandas as pd

# C:\Users\rasmu\PycharmProjects\LTCW_Fantasy_Football\Ressources\ltcwff-files-0.9.0\data
DATA_DIR = "C:/Users/rasmu/PycharmProjects/LTCW_Fantasy_Football/Ressources/ltcwff-files-0.9.0/data"
DATA_DIR_MAC = "/Users/rasmusskovbo/PycharmProjects/fantasy-football-data-analysis/Ressources/ltcwff-files-0.9.0/data"

adp_simple = pd.DataFrame(index = ['name', 'position', 'adp'])

pg = pd.read_csv(path.join(DATA_DIR, 'player_game_2017_sample.csv'))

## 3.1.2
pg['rec_pts_ppr'] = (pg['rec_yards'] * 0.1) + (pg['rec_tds'] * 6) + (pg['receptions']) * 1
pg[['player_name', 'rec_pts_ppr']].sample(10)

## 3.1.3
def player_desc(player, pos, team):
    return f'{player} is the {pos} for {team}'


pg['player_desc'] = pg['player_name'] + ' is the ' + pg['team'] + ' ' + pg['pos']


## 3.1.4
pg['is_possesion_rec'] = pg['rec_raw_airyards'] > pg['raw_yac']


## 3.1.5
pg['len_last_name'] = (pg['player_name'].apply(lambda x: len(x.split('.')[-1])))



