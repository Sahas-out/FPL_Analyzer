# FPL_Analyzer

# Track -- Data Analytics

## Contributors

- Jayesh Pandit(Jayesh.Pandit@iiitb.ac.in)
- Sahas Sangal(Sahas.Sangal@iiitb.ac.in)
- Parv Sharma(Parv.Sharma@iiitb.ac.in)

## Problem Statement

Using data analytics to address two key challenges in football analysis: predicting player statistics for the upcoming week and optimizing fantasy football team selection using the season's data.

## Goal

Our goal is simple: to provide player statistics predictions for the upcoming premier league week, display some realtions between the different factors affecting a player's performance and the best 11 fantasy team suggestions.
We will use the season's data till the upcoming week to analyze it and predict for the upcoming week.

## Features

### Website
- **Our website** :  https://ff11.webflow.io/
- displays the top 10 forwards, mid-fielders, defenders and top 3 goalkeepers of our sample test premier game week 32 data on the basis of expected fpl points that we have calculated
- it displays stats like name, price, expected fpl points, expected fpl points with respect to their current playing form.
- Also we display a pizza chart analysis for each player to depict how he performs in each sector with respect to top player in that sector.
- Finally it shows the best 11 team for fantasy football
- {we can show all this data for any week..but we are showing for this week only as we are using a static website :)....}

## Tech Stack

#### Web scraping

- selenium

### Data visuzlization and Graph plotting

we have used python libraries like

- matplotlib
- seaborn
- pandas

#### Website

We have used the following website that helps to form
https://webflow.com/?utm_campaign=brandjs

#### Some other py libraries

python libraries like

- requests
- os
- sys

#### Image hosting

this is done to using https://imgbb.com/
which allows free image hosting.
We have done this to easily depict pictures
in webflow.
a application chromedriver which is useful
in maintaining sessions with websites with the help of selenium

## Implementation

### Data Scraping(live scrapper)

We scrapped the following data using selenium from this https://www.premierleague.com/,

- Player stats like name, xg, price, etc.
- Player pfps
- Match Fixtrues
  and used this https://fixturedownload.com/sport/football for extracting season's older match fixtrues.

### Analysis

#### forming predictions

We used two variables, one which measures the fixture difficulty and one which accounts for this season's stats till the upcoming week.
Using these two variables, we have predicted player's performance this week.
Example -->

xg(expcted goals) = (xg/90)\* performance_ratio

90 --> mins played

performance_ratio--> calculated using fixtrue difficulty rating.

Just like this, we have calculated for other factors too and then taking using of all these, we have formed a new variable namely 'xfpl'( expected fantasy points).

### Plotting

Now using newfound expected data, we plotted 3 graphs to display understand the dependencies better.
We used matplot and seaborn for this plotting.
The following plots have been shown -->

- CORRELATION MATRIX HEAT MAP(https://www.quanthub.com/how-to-read-a-correlation-heatmap/)
- SCATTER CHART(https://www.jaspersoft.com/articles/what-is-a-scatter-chart#:~:text=A%20scatter%20chart%2C%20commonly%20referred,on%20a%20two%2Ddimensional%20plane.)
- BOX GRAPH(https://byjus.com/maths/box-plot/)
  ‍

### Website

We have used https://webflow.com/?utm_campaign=brandjs to design a website to display our analysis better.

## How to run

So you can run it in two ways :

- You can run run.sh file which is a series of bash commands which run python files but as some python files take up to 10 mins to run (due to data scraping from web ) it may not be ideal
- the other way is manually running it :(
  - first we need to run **fpl.py** to get the live data of all the players from the fpl webite and create a **stats.xlsx** (it would take a long long time )
  - to create **team_score.csv** we first run **fixture_stats.py** which download 20 excel sheets and then run **data_sorter.py** in the fixtures folder
  - then we need to run **predictions.py** to get predicted stats of the players for the next game week ( it uses files get_fixtures.py ,fdr_calculate and team_score.csv ) and create a **predictions.xlsx**
  - next we need to run **clean_predictions.py** to clean the predictions.xlsx and create a **player_expected_stats.xlsx**
  - then we can run **top_players.py** to get Top defenders,midifielders and attackers for the next gameweek it create respective excel sheets
  - then we can run **best-11.py** to generate top 11 players of this gameweek it creates a **best-11.csv**

**best_11_for web** and **top10_for_web.py** are for just creating csv files for web it scrapes player profiles images from web and put thier links into csv with the links of charts of players we hosted on Internet

## Applications

- The best 11 team for the week suggested by us can be used by fantasy football fans to form their teams by seeing our analysis.
- The statistical analysis of different players can be used by coaches to form strategies for upcoming matches and also in general just to see how each player is performing.

## Further Improvements

- Currently our project can scrap live data from the site and generate the analysis and plot it but it can't display on it our website as it isn't dynamic.
  (Ps - We knew basic web only , and so focused on doing our analysis part better for now due to time constraints :| )

- We plan on making our website dynamic and updating it everytime we run our code thus making it ready for implementation every game week.

## Demo

Insert gif or link to demo
