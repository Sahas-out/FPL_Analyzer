from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.by import By
import time
import pandas as pd

def get_data_from_dialog():
        player_stats=[]
        player_stats.append(driver.find_element(By.XPATH,'//h2[@class="styles__ElementHeading-ahs9zc-5 haxmIv"]').text) #name 
        player_stats.append(driver.find_element(By.XPATH,'//span[@class="styles__ElementTypeLabel-ahs9zc-4 BFSeu"]').text) #position
        player_stats.append(driver.find_element(By.XPATH,'//div[@class="styles__Club-ahs9zc-6 cvAaWL"]').text) #team
        try:
            inj = driver.find_element(By.XPATH,'//div[@type="news"]').text
            try:
                player_stats.append(inj[inj.index('%')-2:inj.index('%')+1])
            except:
                player_stats.append('0%')
        except:
            player_stats.append('100%')

        lst = driver.find_elements(By.XPATH,'//div[@class="styles__StatValue-sc-1tsp201-2 fgGEXH"]')
        player_stats.append(lst[0].text)
        player_stats.append(lst[1].text)
        player_stats.append(lst[4].text)



        path = '//*[@id="root-dialog"]/div/dialog/div/div[2]/div[2]/div/div/div[1]/div[2]/table/tfoot/tr[1]/td'
        for x in range(4,26):
            player_stats.append(driver.find_element(By.XPATH,f'{path}[{str(x)}]').text)
        
        
        stats.append(player_stats)
        driver.find_element(By.XPATH,'//*[@id="root-dialog"]/div/dialog/div/div[1]/div/button').click()

print("running file fpl.py it would create stats.xlsx it would take a very long time :) :) ")

url = "https://fantasy.premierleague.com/statistics"

Service = ChromiumService(executable_path="chromedriver")
driver = webdriver.Chrome(service=Service)
driver.get(url)
time.sleep(1)
columns = ['name','pos','team','inj','prc','form',
           'pts','st','mp','gs','a','xG',
           'xA','xGI','CS','GC','xGC','OG',
           'PS','PM','YC','RC','S','BP',
           'BPS','I','C','T','II']
#  now clicking on accept the cookies buttosn
acpt_cookies = driver.find_element(By.ID,'onetrust-accept-btn-handler')
acpt_cookies.click()
stats =[]   
time.sleep(1)
# driver.find_element(By.XPATH,'//button[@class="PaginatorButton__Button-xqlaki-0 cDdTXr"]').click()
for page in range(18):#(29):
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, -document.body.scrollHeight)")
    time.sleep(0.5)
    xpath = '//button[@class="ElementInTable__MenuButton-y9xi40-0 dSPKUY"]'
    buttons = driver.find_elements(By.XPATH,xpath)
    time.sleep(0.1)
    for i in range(len(buttons)):
        buttons[i].click()
        count = 0
        while(True):
            try:
                time.sleep(0.2) 
                data = get_data_from_dialog()
                if(data!=None):
                    stats.append(data)
                print(page,'',i)
                break
            except:
                continue   
    
    
    if(page == 0):
        driver.find_elements(By.XPATH,'//button[@class="PaginatorButton__Button-xqlaki-0 cDdTXr"]')[0].click()
    else:
        driver.find_elements(By.XPATH,'//button[@class="PaginatorButton__Button-xqlaki-0 cDdTXr"]')[1].click()
    




driver.quit()
df = pd.DataFrame(stats,columns = columns)
df.to_excel('stats.xlsx')


# //*[@id="root-dialog"]/h2[@class="styles__ElementHeading-ahs9zc-5 haxmIv"]