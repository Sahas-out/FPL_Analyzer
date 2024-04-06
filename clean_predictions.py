import pandas as pd

print("running clean_predictions.py ")

df = pd.read_excel('predictions.xlsx')

df['VS'] = df['VS'].str[1:-1].replace(',',' ')
df['performance_ratio'] = df['performance_ratio'].str[1:-1].replace(',',' ')
df['xG'] = df['xG'].str[1:-1].replace(',',' ')
df['xA'] = df['xA'].str[1:-1].replace(',',' ')
df['xGC'] = df['xGC'].str[1:-1].replace(',',' ')
df['xBP'] = df['xBP'].str[1:-1].replace(',',' ')
df['CS%'] = df['CS%'].str[1:-1].replace(',',' ')
df['xS'] = df['xS'].str[1:-1].replace(',',' ')
df['xYC'] = df['xYC'].str[1:-1].replace(',',' ')
df['xPS'] = df['xPS'].str[1:-1].replace(',',' ')
df['xPM'] = df['xPM'].str[1:-1].replace(',',' ')
df['xRC'] = df['xRC'].str[1:-1].replace(',',' ')

(df[df['mp']>1000].sort_values(by='xfpl',ascending= False)).to_excel('player_expected_stats.xlsx',index = False)

# df[df['mp'] >1500][['name','xfpl','VS','position','role']].sort_values(by = 'xfpl',ascending=False).head(15).to_csv('a1.csv')
