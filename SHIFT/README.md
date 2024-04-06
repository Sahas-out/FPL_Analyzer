# TeamJhense

first we need to run fpl.py to get data of all the players from the fpl webite
and create a stats.xlsx

to create team_score.csv we first run fixture_stats.py which download 20 previous excel sheets which is calcuated by running data_sorter.py

then we need to run predictions.py to get predicted stats of that players of the next game week ( it uses two files get_fixtures.py and fdr_calculate and team_score.csv ) and create a predictions.xlsx

next we need to run clean_predictions.py to clean the predictions.xlsx and create a player_expected_stats.xlsx

then we can run top_players.py to get Top defenders,midifielders and attackers list and create respecive exxcel sheets

then we can run best-11.py to generate top 11 players of this gameweek it creates a best-11.csv

best_11_for web and top10_for_web.py are for jusst creating csv files for web which scrapes player profiles images from web and put it into csv to display it on website
