from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service("C:\\Users\\Mustafa Dağtekin\\PycharmProjects\\chromedriver_123.exe"))
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.XPATH,'//*[@id="username"]').send_keys("studentt")
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("Password123")
driver.find_element(By.XPATH,'//*[@id="submit"]').click()
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="error"]'))
    )
    print("test failed")
except:
    print("test passed")
    driver.quit()
