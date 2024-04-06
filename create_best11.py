import pandas as pd
from itertools import combinations as cmb



def check_condition(team):
    price_sum =0 
    fpl_sum = 0
    team_count ={'Liverpool': 0,'Man City': 0,'Arsenal':0,
 'Aston Villa':0,'Spurs':0,
 'Man Utd':0,'West Ham':0, 'Newcastle':0,
 'Brighton':0,'Wolves':0,'Chelsea':0,'Fulham':0,
 'Bournemouth':0,'Crystal Palace':0,'Brentford':0,'Everton':0,'Nottingham Forest':0,
 'Luton':0,'Burnley':0,'Sheffield Utd':0}
    
    for player in team:
        price_sum += players.iloc[player]['price']
        fpl_sum += players.iloc[player]['xfpl']
        team_count[players.iloc[player]['team']] +=1
    
    for i in team_count.keys():
        if(team_count[i] > 3):
            return 0
    
    if price_sum > 100 :
        return 0
    
    return fpl_sum

print("creating best 11 of this gameweek ")

f,m,d,g = (6,9,5,3)


df = pd.read_excel('player_expected_stats.xlsx')

forwards = df[df['position'] == 'Forward'][['name','price','team','xfpl','position']].sort_values(by = 'xfpl',ascending=False).head(f)
forwards['idx'] = [i for i in range(f)]
forwards.set_index('idx',inplace=True)

midfielders = df[df['position'] == 'Midfielder'][['name','price','team','xfpl','position']].sort_values(by = 'xfpl',ascending=False).head(m)
midfielders['idx'] = [i for i in range(f,f+m)]
midfielders.set_index('idx',inplace=True)

defenders = df[df['position'] == 'Defender'][['name','price','team','xfpl','position']].sort_values(by = 'xfpl',ascending=False).head(d)
defenders['idx'] = [i for i in range(f+m,f+m+d)]
defenders.set_index('idx',inplace=True)

goalkeepers = df[df['position'] == 'Goalkeeper'][['name','price','team','xfpl','position']].sort_values(by = 'xfpl',ascending=False).head(g)
goalkeepers['idx'] = [i for i in range(f+m+d,f+m+d+g)]
goalkeepers.set_index('idx',inplace=True)

players = pd.concat([forwards,midfielders,defenders,goalkeepers])

combs =((3,5,2),(3,4,3),(4,5,1),(4,4,2),(4,3,3),(5,4,1),(5,3,2),(5,2,3))
total_combs = []

for i,j,k in combs:
    comb_def = list(cmb(range(f+m,f+m+d),i))
    comb_mid = list(cmb(range(f,f+m),j))
    comb_for = list(cmb(range(f),k))
    comb_gol = list(cmb(range(f+m+d,f+m+d+g),1))
    
    for cd in range(0,len(comb_def)):
        for cm in range(0,len(comb_mid)):
            for cf in range(0,len(comb_for)):
                for cg in range(0,len(comb_gol)):
                    total_combs.append(comb_def[cd]+comb_mid[cm]+comb_for[cf]+comb_gol[cg])

print(len(total_combs))

best_team = []
max_fpl = 0
for team in total_combs:
    fpl_sum = check_condition(team)
    if(max_fpl<fpl_sum):
        best_team = team
        max_fpl = fpl_sum

print(best_team)
players.iloc[[i for i in best_team]].to_csv('best-11.csv')   