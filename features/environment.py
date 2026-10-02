from selenium import webdriver


def before_scenario(context, scenario):
    """Create a fresh Chrome browser session before each scenario."""
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


def after_scenario(context, scenario):
    """Close the browser session after each scenario."""
    if hasattr(context, "driver"):
        context.driver.quit()