from behave import given, when, then
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@given(u'The manager is on the manager dashboard page')
def step_impl(context):
	context.driver.get("C:/Users/Dominick/VSCodeProjects/ReimbursementApp/html/mgrDashboard.html?id=1")


@when(u'the manager selects pending from the filter drop-down menu')
def step_impl(context):
	context.manager_dashboard_page.status_filter_select().select_by_visible_text("Pending")


@when(u'the manager selects approved from the filter drop-down menu')
def step_impl(context):
	context.manager_dashboard_page.status_filter_select().select_by_visible_text("Approved")


@when(u'the manager selects rejected from the filter drop-down menu')
def step_impl(context):
	context.manager_dashboard_page.status_filter_select().select_by_visible_text("Rejected")


@then(u'The manager table should display only pending requests')
def step_impl(context):
	all_status = WebDriverWait(context.driver, 2).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'reimbursement-status')))
	for status in all_status:
		assert status.text == "Pending"


@then(u'The manager table should display only approved requests')
def step_impl(context):
	all_status = WebDriverWait(context.driver, 2).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'reimbursement-status')))
	for status in all_status:
		assert status.text == "Approved"


@then(u'The manager table should display only rejected requests')
def step_impl(context):
	all_status = WebDriverWait(context.driver, 2).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'reimbursement-status')))
	for status in all_status:
		assert status.text == "Rejected"