from behave import then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


LOGIN_URL = "https://practicetestautomation.com/practice-test-login/"


@when("the user enters invalid login credentials")
def enter_invalid_login_credentials(context):
    context.driver.get(LOGIN_URL)

    context.driver.find_element(By.ID, "username").send_keys("invalid_user")
    context.driver.find_element(By.ID, "password").send_keys("invalid_password")
    context.driver.find_element(By.ID, "submit").click()


@then("an authentication error message should be displayed")
def verify_authentication_error(context):
    error_message = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "error"))
    )

    assert error_message.is_displayed(), "Authentication error message was not displayed."
    assert error_message.text.strip(), "Authentication error message was empty."