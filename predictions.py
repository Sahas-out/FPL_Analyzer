import pandas as pd
import os 
from get_fixtures import *
from fdr_calculate import *

print(" running predictions.py it would create a predictions.xlsx file next run clean_predictions.py ")

df = pd.read_excel('stats.xlsx',usecols='B:AD')
cols = ['name','position','team','role','total_points','chance_playing',
        'form','VS','performance_ratio','xfpl','xfpl&f',
        'xG','xA','xGC','xBP','CS%',
        'xS','mp','xYC','xPS','xPM','xRC']
predictions = pd.DataFrame(columns = cols)

# cleaning the data of stats
df['mp'] = df['mp'].str.replace(',','').astype('int64')
df['T'] = df['T'].str.replace(',','').astype('int64')
df['prc'] = df['prc'].str[1:-1].astype('float64')
df['inj'] = df['inj'].str.replace('%','').astype('int64')
df.loc[df['team']=="Nott'm Forest",'team'] = 'Nottingham Forest'


fdr_team = pd.read_csv('team_score.csv')
fdr_team['FDR'] = fdr_team['Score'] / fdr_team['Total_Matches']
fdr_team_map = dict(fdr_team[['Team','FDR']].values.tolist())

total_matches_map = dict(fdr_team[['Team','Total_Matches']].values.tolist())

team_wise_fix = get_fixtures()
gameweek = 0
time.sleep(1) 



# adding total_team_matches
total_team_matches = []
for idx,row in df.iterrows():
    total_team_matches.append(fdr_team[fdr_team['Team'] == row['team']]['Total_Matches'].values.tolist()[0])
df['Total_Matches'] = total_team_matches

predictions['name'] = df['name']# adding the name
# adding the name role 
predictions['role'] = (df['st']*85/df['mp'] > 0.9) & (df['st']/df['Total_Matches'] > 0.5)
predictions.loc[predictions['role'] == True, 'role'] = 'starter'
predictions.loc[predictions['role'] == False, 'role'] = 'not  a starter'
predictions['form'] = df['form'] #adding form
predictions['total_points'] = df['pts'] # adding total_pointss
predictions['mp'] = df['mp'] # adding minutes played
predictions['position'] = df['pos'] #adding the position column
predictions['chance_playing']  = df['inj'] #adding the chance_playing column

#performance ratio and opponent
performance_ratio = []
opponents = []
for idx,row in df.iterrows():
    
    team = row['team']
    performance_ratio.append(get_fdr_ratio(team_wise_fix[team][gameweek],fdr_team_map[team]))
    
    vs = team_wise_fix[team][gameweek]
    vs = vs.split('|')
    opp = []
    for i in range(0,len(vs),2):
        opp.append(vs[i])
    opponents.append(opp)

predictions['performance_ratio'] = performance_ratio
predictions['VS'] = opponents
predictions['team'] = df['team'] # adding the team
predictions['price'] = df['prc']

predictions['xG'] = ((df['xG']/df['mp'])*90) 
predictions['xA'] = ((df['xA']/df['mp'])*90)
predictions['xGC'] = ((df['xGC']/df['mp'])*90) 
predictions['CS%'] = (df['CS']/df['Total_Matches'])    #*1.8  
predictions['xPS'] = ((df['PS']/df['mp'])*90)
predictions['xPM'] = (df['PM']/df['mp'])*90
predictions['xYC'] = (df['YC']/df['mp'])*90
predictions['xRC'] = ((df['RC']/df['mp'])*90)**1.25
predictions['xS'] = (df['S']/df['mp'])*90
predictions['xBP'] = (df['BP']/df['mp'])*90 

xG,xA,xGC,CSp,xPS,xPM,xYC,xRC,xS,xBP = [],[],[],[],[],[],[],[],[],[]
for idx , row in predictions.iterrows():
    
    xG.append(([(row['xG']*i) for i in row['performance_ratio']]))
    xA.append(([(row['xA']*i) for i in row['performance_ratio']]))
    try:
        xGC.append(([(row['xGC']/(i**0.75)) for i in row['performance_ratio']])) #i**0.5
    except ZeroDivisionError:
        xGC.append([0])  
    xPS.append(([(row['xPS']) for i in row['performance_ratio']]))
    xPM.append(([(row['xPM']) for i in row['performance_ratio']]))
    xYC.append(([(row['xYC']) for i in row['performance_ratio']]))
    xRC.append(([(row['xRC']) for i in row['performance_ratio']]))
    xS.append(([(row['xS']) for i in row['performance_ratio']]))
    CSp.append(([(row['CS%']*(i**0.65)) for i in row['performance_ratio']]))

predictions['xG'] = xG
predictions['xA'] = xA
predictions['xGC'] = xGC
predictions['xPS'] = xPS
predictions['xPM'] = xPM
predictions['xYC'] = xYC
predictions['xRC'] = xRC
predictions['xS'] = xS
predictions['CS%'] =  CSp

for idx,row in predictions.iterrows():
    xBP.append(([(row['xBP'] * (team_stars[row['team']] / team_stars[i]))   for i in row['VS']]))

predictions['xBP'] =  xBP

# noww caluclating the xfpl
xfpl = []
for idx,row in predictions.iterrows():
    points = 0
    

    if ( row['position'] == 'Forward'):
        points+=sum(row['xG'])*4
        points+=1.8 # poiints added for playing time 
    elif( row['position'] == 'Midfielder'):
        points+=sum(row['xG'])*5
        points+=sum(row['CS%'])*1
        points+=1.92 # points added for playing time 
    else:
        points+=sum(row['xG'])*6
        points+=sum(row['CS%'])*4
        points-=sum(row['xGC'])*0.5
        points+=2.0 # points added for playing time
    
    points+=sum(row['xA'])*3
    points-=sum(row['xYC'])*1
    points-=sum(row['xRC'])*3
    points+=sum(row['xPS'])*5
    points+=sum(row['xS'])*0.33
    points+=sum(row['xBP'])

    xfpl.append(points)

predictions['xfpl'] = xfpl

#xfpl&f with form adjusted 
predictions['xfpl&f'] = predictions['xfpl'] * ((predictions['form']/((predictions['total_points']/df['mp'])*90))**0.5)

predictions.to_excel('predictions.xlsx',index=False)