from os import path
import pandas as pd

# C:\Users\rasmu\PycharmProjects\LTCW_Fantasy_Football\Ressources\ltcwff-files-0.9.0\data
DATA_DIR = "C:/Users/rasmu/PycharmProjects/LTCW_Fantasy_Football/Ressources/ltcwff-files-0.9.0/data"
DATA_DIR_MAC = "/Users/rasmusskovbo/PycharmProjects/fantasy-football-data-analysis/Ressources/ltcwff-files-0.9.0/data"

adp_simple = pd.DataFrame(index = ['name', 'position', 'adp'])