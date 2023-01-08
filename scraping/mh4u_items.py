# Works properly but with the wrong IDs since Kiranico keeps the in-game order instead of sorting by IDs

import os
import sys
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
os.chdir(os.path.dirname(sys.argv[0]))

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://kiranico.com/en/mh4u/item')

items = pd.DataFrame()
items['ID'] = [None] * 1914
items['Name'] = [None] * 1914
id = 0

for i in range(2,321):
    for k in range(1,7):
        xpath = '/html/body/div[2]/div['+str(i)+']/div['+str(k)+']/p/a'
        if i == 320 and k == 6:
            break
        name = driver.find_element(By.XPATH,xpath).text
        id += 1
        items.iloc[id,0] = id
        items.iloc[id,1] = name

items.to_csv('mh4u_items.csv', index=False)
driver.quit()