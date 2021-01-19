from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = "/Users/mhee4/cloud/webdriver/chromedriver"
driver = webdriver.Chrome(path)

driver.get("https://www.github.com/login")
print(driver.title)

elem_email = driver.find_element_by_id("login_field")
elem_email.send_keys("[깃헙 아이디]")
elem_pass = driver.find_element_by_id("password")
elem_pass.send_keys("[깃헙 비밀번호]")

elem_pass.send_keys(Keys.RETURN)