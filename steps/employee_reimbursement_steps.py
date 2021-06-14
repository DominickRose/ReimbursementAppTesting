import time
from behave import when, then, given
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when(u'The employee clicks the new request button')
def step_impl(context):
	context.employee_dashboard_page.new_reimbursement_button().click() 


@then(u'The new request dialogue should appear')
def step_impl(context):
	WebDriverWait(context.driver, 2).until(EC.visibility_of_element_located((By.ID, 'reimbursementModal')))
	assert True

@when(u'The employee enters the amount of the request')
def step_impl(context):
    context.employee_dashboard_page.amount_input().send_keys(456)


@when(u'The employee enters the reason for the request')
def step_impl(context):
    context.employee_dashboard_page.reason_input().send_keys('Reason for testing')


@when(u'The employee enters the submit request button')
def step_impl(context):
	context.employee_dashboard_page.submit_request_btn().click()


@then(u'The new request dialogue should close')
def step_impl(context):
     WebDriverWait(context.driver, 2).until(EC.invisibility_of_element_located((By.ID, 'reimbursementModal')))
     assert True

@then(u'The new request should appear in the table')
def step_impl(context):
   newLen = len(WebDriverWait(context.driver, 3).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'statusValue'))))
   assert newLen > 0 


@when(u'The employee clicks the cancel button')
def step_impl(context):
    context.employee_dashboard_page.cancel_request_btn().click()


@when(u'The employee clicks the delete button on a request')
def step_impl(context):
    delete_button = WebDriverWait(context.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-danger')))
    context.delete_button = delete_button.get_attribute("id")
    delete_button.click()


@then(u'A confirmation pop-up should appear')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 1).until(EC.alert_is_present())
        assert True
    except TimeoutException:
        assert False

@when(u'The employee clicks the confirm delete button')
def step_impl(context):
    alert = context.driver.switch_to.alert
    alert.accept()


@then(u'The confirmation pop-up should close')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 1).until_not(EC.alert_is_present())
        assert True
    except TimeoutException:
        assert False


@then(u'The request should no longer be in the table')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 2).until_not(EC.presence_of_element_located((By.ID, context.delete_button)))
        assert True
    except TimeoutException:
        assert False


@when(u'The employee clicks the cancel delete button')
def step_impl(context):
    alert = context.driver.switch_to.alert
    alert.dismiss()