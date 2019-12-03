from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait


#This example requires Selenium WebDriver 3.13 or newer
with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    employee_fill = "http://127.0.0.1:5000/index.html"
    driver.get(employee_fill)
    driver.maximize_window()

    driver.find_element_by_name("query").send_keys("BJP")

    driver.find_element_by_id("search").click()
    time.sleep(10)