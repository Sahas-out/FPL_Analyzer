from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.by import By
import time
import pandas as pd

def get_fixtures():
    url = "https://fantasy.premierleague.com/fixtures/fdr"

    Service = ChromiumService(executable_path="chromedriver")
    driver = webdriver.Chrome(service=Service)
    driver.get(url)
    time.sleep(1)

    acpt_cookies = driver.find_element(By.ID,'onetrust-accept-btn-handler')
    acpt_cookies.click()
    time.sleep(1)

    fix = {}
    team_row = driver.find_elements(By.XPATH,'//tr[@data-testid = "team-row"]')

    mp = {'LIV':'Liverpool','MCI':'Man City','ARS':'Arsenal',
     'AVL':'Aston Villa','TOT':'Spurs',
     'MUN':'Man Utd','WHU':'West Ham', 'NEW':'Newcastle',
     'BHA':'Brighton','WOL':'Wolves','CHE':'Chelsea','FUL':'Fulham',
     'BOU':'Bournemouth','CRY':'Crystal Palace','BRE':'Brentford','EVE':'Everton','NFO':'Nottingham Forest',
     'LUT':'Luton','BUR':'Burnley','SHU':'Sheffield Utd','(A)':'(A)','(H)':'(H)','-':''}
    for row in team_row:
        team = row.find_element(By.XPATH,'.//div[@class = "FDRTable__TeamCellName-eidkh5-4 htSJBS"]').text
        cell = row.find_elements(By.XPATH,'.//div[@class = "FDRTable__CellWrapper-eidkh5-0 hUAMzs"]')[:-2]
        fix[team] = ['|'.join([mp[x] for x in i.text.split('\n')]) for i in cell]
        time.sleep(0.05)
    fix['Nottingham Forest'] = fix["Nott'm Forest"]
    del fix["Nott'm Forest"]
    driver.quit()
    return fix
