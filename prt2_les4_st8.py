from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
message = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
message = browser.find_element_by_id("price")
print(message.text)

assert "$100" in message.text

button = browser.find_element_by_css_selector("button.btn")
button.click()

x = int(browser.find_element_by_id("input_value").text)
print(x)
y = calc(x)
print(y)
input2 = browser.find_element_by_id('answer')
input2.send_keys(y)
	
button = browser.find_element_by_id("solve")
button.click()