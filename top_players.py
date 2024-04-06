import pandas as pd
import os 

print("running top_players.py it would create top mids top forwards top defenders sheets of this week")

df = pd.read_excel('player_expected_stats.xlsx')

def top_midfielders():
    (df[(df['position'] == 'Midfielder') & (df['role'] == 'starter')].sort_values(by='xfpl',ascending=False)).head(10).to_excel('Top-Mids.xlsx',index = False)
def top_forwards():
    (df[(df['position'] == 'Forward') & (df['role'] == 'starter')].sort_values(by='xfpl',ascending=False)).head(10).to_excel('Top-Forwds.xlsx',index=False)

def top_defenders():
    (df[(df['position'] == 'Defender') & (df['role'] == 'starter')].sort_values(by='xfpl',ascending=False)).head(10).to_excel('Top-Defs.xlsx',index =False)

def top_goalkeepers():
    (df[ (df['position'] == 'Goalkeeper')  & (df['role'] == 'starter')].sort_values(by='xfpl',ascending=False)).head(3).to_excel('Top-Golies.xlsx',index = False)


top_midfielders()
top_forwards()
top_goalkeepers()
top_defenders()
