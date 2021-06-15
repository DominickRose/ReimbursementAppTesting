from behave import given, when, then

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when(u'The manager clicks an approve request button')
def step_impl(context):
    approve_button = WebDriverWait(context.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'approve-btn')))
    context.driver.execute_script("arguments[0].scrollIntoView();", approve_button)
    approve_button.click()


@then(u'A confirm approval pop-up should appear')
def step_impl(context):
	try:
		WebDriverWait(context.driver, 2).until(EC.visibility_of_element_located((By.ID, 'approveRequestModal')))
		assert True
	except TimeoutException:
		assert False


@when(u'The manager enters a comment in the approve comment input')
def step_impl(context):
	context.manager_dashboard_page.approval_comment_input().send_keys("Comment for approval")


@when(u'The manager clicks the confirm approval button')
def step_impl(context):
	context.manager_dashboard_page.submit_approve_btn().click()


@then(u'The confirm approval pop-up should close')
def step_impl(context):
	try:
		WebDriverWait(context.driver, 2).until(EC.invisibility_of_element_located((By.ID, 'approveRequestModal')))
		assert True
	except TimeoutException:
		assert False


@when(u'The manager clicks the cancel approval button')
def step_impl(context):
	context.manager_dashboard_page.cancel_approve_btn().click()


@when(u'The manager clicks the deny request button')
def step_impl(context):
    approve_button = WebDriverWait(context.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'reject-btn')))
    context.driver.execute_script("arguments[0].scrollIntoView();", approve_button)
    approve_button.click()

@then(u'A confirm rejection pop-up should appear')
def step_impl(context):
	try:
		WebDriverWait(context.driver, 2).until(EC.visibility_of_element_located((By.ID, 'rejectRequestModal')))
		assert True
	except TimeoutException:
		assert False

@when(u'The manager enters a comment in the reject comment input')
def step_impl(context):
	context.manager_dashboard_page.reject_comment_input().send_keys("Comment for approval")



@when(u'The manager clicks the confirm rejection button')
def step_impl(context):
	context.manager_dashboard_page.submit_reject_btn().click()


@then(u'The confirm rejection pop-up should close')
def step_impl(context):
	try:
		WebDriverWait(context.driver, 2).until(EC.visibility_of_element_located((By.ID, 'rejectRequestModal')))
		assert True
	except TimeoutException:
		assert False


@when(u'The manager clicks the cancel rejection button')
def step_impl(context):
	context.manager_dashboard_page.cancel_reject_btn().click()
