
a1,a2,a3,a4,a5,a6 = [10,8,6,5,3,2] 

team_stars = {'Liverpool':a1,'Man City':a1,'Arsenal':a1,
 'Aston Villa':a2,'Spurs':a2,
 'Man Utd':a3,'West Ham':a3, 'Newcastle':a3,
 'Brighton':a4,'Wolves':a4,'Chelsea':a4,'Fulham':a4,
 'Bournemouth':a5,'Crystal Palace':a5,'Brentford':a5,'Everton':a5,'Nottingham Forest':a5,
 'Luton':a6,'Burnley':a6,'Sheffield Utd':a6}

def get_fdr_ratio(fx,team_score):
    fdr_ratio = []
    fx = fx.split('|')
    for i in range(0,len(fx),2):
        home_support = 0.25 if fx[i+1] == '(H)' else -0.25
        fdr_ratio.append((team_score/(team_stars[fx[i]]))+home_support)
    if(fdr_ratio == []):
        return [0]
    return (fdr_ratio)

