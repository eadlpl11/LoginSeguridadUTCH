from selenium import webdriver
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)

driver.get("http://127.0.0.1:5000/login")

username = driver.find_element_by_id('exampleInputEmail1')

pwd = driver.find_element_by_id('exampleInputPassword1')

username.send_keys("wefwefwe")
pwd.send_keys("12345678@A")

button = driver.find_element_by_id('button')


time.sleep(3)

button.click()