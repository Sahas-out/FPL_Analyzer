from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

def get_image(name):
    input_field.send_keys(name)
    time.sleep(0.5)
    search_button.click()
    time.sleep(1)
    
    player_button = driver.find_element(By.XPATH,'//a[@class="player__name"]')
    player_button.click()
    time.sleep(1.5)

    player_link = driver.find_element(By.XPATH,'//img[@data-script="pl_player-image"]').get_attribute('src')
    driver.back()
    time.sleep(0.5)
    input_field.clear()
    time.sleep(0.5)
    return player_link

url = "https://www.premierleague.com/players"

Service = ChromiumService(executable_path="chromedriver")
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : './images/'}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(service=Service,options=chrome_options)
driver.get(url)
time.sleep(1)


acpt_cookies = driver.find_element(By.ID,'onetrust-accept-btn-handler')
acpt_cookies.click()
time.sleep(0.5)

close_button = driver.find_element(By.XPATH,'//a[@id="advertClose"]')
close_button.click()
time.sleep(0.5)

input_field = driver.find_element(By.XPATH,'//input[@id="search-input"]')
time.sleep(0.1)

search_button = driver.find_element(By.XPATH,'//div[@class="searchIconContainer searchCommit"]')

df = pd.read_csv('best-11.csv') # edit name here
names_list = df['name'].values.tolist()

img_url_links = []
for i in names_list:
    img_url_links.append(get_image(i))
df['img-urls'] = img_url_links

df['xfpl'] ="xfpl  " + df['xfpl'].round(2).astype(str)   
df['price'] ="price  " + df['price'].round(2).astype(str)   

driver.quit()
df[['name','img-urls','xfpl','price','team','position']].to_csv('./web_display/best11.csv',index=False)