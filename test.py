from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def visit_site_for_label():
    driver.get('http://tutorialsninja.com/demo/')

    #    searchbox = driver.find_element(By.XPATH, '//*[@id="search"]/input')
    #    searchbox.send_keys('kek')
    #    button = driver.find_element(By.XPATH, '//*[@id="search"]/span/button')
    label = driver.find_element(By.XPATH, '//*[@id="logo"]/h1/a')
    return label.text


#    button.click()


print("text: ", visit_site_for_label())

driver.quit()
