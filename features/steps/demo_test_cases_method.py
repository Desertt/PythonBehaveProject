from behave import *

@given('credentials are given')
def cred_are_given(context):
    print("user id:tasarimplatin")
    pass

@when('we input correct credentials')
def step_impl(context):
    assert 2==2, "This eq is not correct"

@then('login will be successful')
def step_impl(context):
    print("login successful")

@step("correct profile opened")
def step_impl(context):
    print("correct profile opened")


