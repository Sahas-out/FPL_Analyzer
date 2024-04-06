import pandas as pd
import os 

def fnc(a,b):
    return a+b
df = pd.read_excel('stats.xlsx',usecols='B:AD')

# cleaning the data of stats
# df['mp'] = df['mp'].str.replace(',','').astype('int64')
# df['T'] = df['T'].str.replace(',','').astype('int64')
# df['prc'] = df['prc'].str[1:-1].astype('float64')
# df['inj'] = df['inj'].str.replace('%','').astype('int64')

# adding some new columns
# df['role'] = (df['st']*85/df['mp'] > 0.9) & (df['st']/30 > 0.4)

#testing
# df[df['team'] == 'Aston Villa'][['name','role']].to_csv('test.csv',index = False)


