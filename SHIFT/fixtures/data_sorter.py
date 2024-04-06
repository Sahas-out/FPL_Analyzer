import pandas as pd
import os
import sys
sys.path.append('/home/ubuntu/TeamJhense')
a1,a2,a3,a4,a5,a6 = [10,8,6,5,3,2]
map = {'Liverpool':a1,'Man City':a1,'Arsenal':a1,
 'Aston Villa':a2,'Spurs':a2,
 'Man Utd':a3,'West Ham':a3, 'Newcastle':a3,
 'Brighton':a4,'Wolves':a4,'Chelsea':a4,'Fulham':a4,
 'Bournemouth':a5,'Crystal Palace':a5,'Brentford':a5,'Everton':a5,'Nottingham Forest':a5,
 'Luton':a6,'Burnley':a6,'Sheffield Utd':a6}


folder_loc = os.path.expanduser('~/TeamJhense/fixtures/')
csv_list = [file for file in os.listdir(folder_loc  ) if file.endswith('.csv')]
ans = []
def max_team_finder(file):
    d = {}
    for i in file:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i]+=1
    max_val = max(d.values()) 
    for key,value in d.items():
        if value == max_val:
            max_team = key
    return max_team

def find(st):
    return st[st.find('3-')+2:st.find('G')-1]

def team_opp_chooser(file):
    df = pd.read_csv(file)
    concatenated_list = pd.concat([df['Home Team'], df['Away Team']]).tolist()
    team = max_team_finder(concatenated_list)
    sum = 0 #for calculating the sum
    df['Result'] = df['Result'].fillna('0')
    count = 0

    for i,j in df.iterrows():
        if(j['Result'] != '0'):
            if(j['Home Team'] == team):
                sum+=map[j['Away Team']]
            else:
                sum+=map[j['Home Team']]
            count+=1
    
    ans.append([team,sum,count]) 
# team_opp_chooser('~/TeamJhense/fixtures/epl-2023-arsenal-GMTStandardTime.csv')
if __name__ == '__main__':
    for i in csv_list:
        team_opp_chooser('~/TeamJhense/fixtures/'+i)
    ans_df = pd.DataFrame(ans, columns=['Team', 'Score','Total_Matches'])
    print(ans_df)
    ans_df.to_csv('team_score.csv', index=False)
