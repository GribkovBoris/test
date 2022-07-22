from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options)

#AZAZAh

driver.get('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
#driver.get('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
if(False):
    searchbox = driver.find_element(By.XPATH, '//*[@id="search"]/input')
    searchbox.send_keys('kek')
    button = driver.find_element(By.XPATH, '//*[@id="search"]/span/button')
    button.click()

#driver.quit() kek
