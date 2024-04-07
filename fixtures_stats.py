from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.by import By
import time
import os 
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
print("running fixtures_stats.py now it would might take a couple of minutes it creaates 20 excel sheets in the fixtures folder")

if __name__ == '__main__':

    url = "https://fixturedownload.com/sport/football"
    Service = ChromiumService(executable_path="chromedriver")
    path = os.path.abspath('fixtures')
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory' : path}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(service=Service,options=chrome_options)
    driver.get(url)

    time.sleep(1)

    pl_table = driver.find_elements(By.XPATH,'//div[@class="game"]')[17]
    time.sleep(1)

    pl_teams = pl_table.find_elements(By.XPATH,'.//tr[@class="team"]')
    for team in pl_teams:
        team.find_element(By.XPATH,'.//td[3]/a').click()
        time.sleep(1)
        driver.back()
        time.sleep(1)
    
    ActionChains(driver).send_keys(Keys.PAGE_UP).perform()
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[27]/table/tbody/tr[3]/td[3]/a').click()
    time.sleep(2)
    driver.quit()

