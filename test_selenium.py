from selenium import webdriver

import time
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    tweet_fill = "http://127.0.0.1:5000/"
    driver.get(tweet_fill)
    driver.maximize_window()
    time.sleep(15)
    driver.find_element_by_name("query").send_keys("BJP")

    driver.find_element_by_id("search").click()
    time.sleep(20)