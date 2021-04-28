from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge(executable_path="S:\\Testing\\Python\\msedgedriver.exe")

def test_serach_puppies():
    # Go to the chosen site
    driver.get('https://google.com')
    # type in a search term
    driver.find_element(By.NAME, 'q').send_keys('puppies')
    # submit for search
    driver.find_element(By.NAME, 'btnK').submit()
    # assert if the needed page is loaded
    assert 'puppies' in driver.title

def test_search_frost():
    driver.get('https://statsroyale.com')
    driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()
    card = driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']") # *= in CSS means contains
    assert card.is_displayed() 

def test_search_heal():
    driver.get('https://statsroyale.com')
    driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()
    card = driver.find_element(By.CSS_SELECTOR, "[href*='Heal+Spirit']") # *= in CSS means contains
    assert card.is_displayed()
