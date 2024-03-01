from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

list_link = [] # This is the list contains prefill google form link

for i in range(100): # This is the number of responses that you want
    driver = webdriver.Chrome()
    driver.get(random.choice(list_link))  

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@role='button']//span[contains(text(), 'G')]"))) # you must change the string 'G' for each language
    driver.execute_script("window.scrollTo(0, 2000);")
    button3 = driver.find_element(By.XPATH, "//div[@role='button']//span[contains(text(), 'G')]") # similar to above code
    driver.execute_script("arguments[0].click();", button3)
    
    try:
        WebDriverWait(driver, 4).until(EC.url_changes(driver.current_url))
    except:
        continue

    driver.quit()
