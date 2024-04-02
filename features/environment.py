from selenium import webdriver
from selenium.webdriver.chrome.service import Service
def before_scenario(context,scenario):
    print("Chrome Driver Executed")
    context.driver = webdriver.Chrome(service=Service("C:\\Users\\Mustafa Dağtekin\\PycharmProjects\\chromedriver_123.exe"))
    context.driver.maximize_window()

def after_scenario(context, scenario):
    print("Chrome Driver Closed")
    context.driver.close()