from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("C:\\Users\\Mustafa Dağtekin\\PycharmProjects\\chromedriver_123.exe"))
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.XPATH,'//*[@id="username"]').send_keys("student")
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("Password123")
driver.find_element(By.XPATH,'//*[@id="submit"]').click()
driver.quit()
