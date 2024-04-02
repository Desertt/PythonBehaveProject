from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@when('user input wrong credentials')
def step_impl(context):
    context.driver.get("https://practicetestautomation.com/practice-test-login/")
    context.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("studentt")
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Password123")
    context.driver.find_element(By.XPATH, '//*[@id="submit"]').click()

@then('Error message will come')
def step_impl(context):
    try:
        element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="error"]'))
        )
        print("test failed")
    except:
        print("test passed")
        context.driver.quit()

