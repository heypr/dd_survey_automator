from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import random

options = Options()
options.headless = False
driver = webdriver.Firefox(options=options)

driver.get("https://dunkinrunsonyou.com/?dunkin-dd-live/")

element = driver.find_element(By.ID, "spl_q_inrest_rcpt_code_txt")
random_number = random.randint(1000, 9999)
final_int = "92401455000912" + str(random_number)
print(final_int)
element.send_keys(final_int)
button = driver.find_element(By.ID, "buttonBegin")
button.click()
