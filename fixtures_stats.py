from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.by import By
import time
import pandas as pd

if __name__ == '__main__':

    url = "https://fixturedownload.com/sport/football"
    Service = ChromiumService(executable_path="chromedriver")
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory' : './fixtures/'}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(service=Service,options=chrome_options)
    driver.get(url)
    time.sleep(1)

    pl_table = driver.find_elements(By.XPATH,'//div[@class="game"]')[17]
    # print(pl_table.text)
    time.sleep(1)

    pl_teams = pl_table.find_elements(By.XPATH,'.//tr[@class="team"]')
    
    for team in pl_teams:
        team.find_element(By.XPATH,'.//td[3]/a').click()
        time.sleep(1)
        driver.back()
        time.sleep(1)
    
    driver.quit()

