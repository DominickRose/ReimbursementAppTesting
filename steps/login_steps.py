from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@given(u'The employee or manager is on the login page')
def on_login_page(context):
    context.driver.get("C:/Users/Dominick/VSCodeProjects/ReimbursementApp/html/login.html")


@when(u'The employee enters their correct username')
def enter_correct_employee_username(context):
	context.login_page.username_input().send_keys("TestEmployee")


@when(u'The employee enters their correct password')
def enter_correct_employee_password(context):
	context.login_page.password_input().send_keys("employee")


@when(u'The employee or manager clicks the login button')
def click_login_button(context):
	context.login_page.login_button().click()


@then(u'The page should redirect to the employee dashboard')
def check_redirect_to_employee_dashboard(context):
	WebDriverWait(context.driver, 5).until(EC.presence_of_all_elements_located((By.ID, 'empDashboardHTML')))
	assert context.driver.title == "Employee Dashboard"


@when(u'The manager enters their correct username')
def enter_correct_manager_username(context):
	context.login_page.username_input().send_keys("TestManager")


@when(u'The manager enters their correct password')
def enter_correct_manager_password(context):
	context.login_page.password_input().send_keys("manager")


@then(u'The page should redirect to the manager dashboard')
def check_redirect_to_manager_dashboard(context):
	WebDriverWait(context.driver, 5).until(EC.presence_of_all_elements_located((By.ID, 'mgrDashboardHTML')))
	assert context.driver.title == "Manager Dashboard"


@when(u'The employee enters an incorrect password')
def step_impl(context):
	context.login_page.username_input().send_keys("fsdfdsaf")


@then(u'The password input should be cleared')
def step_impl(context):
	context.login_page.password_input().send_keys("fdafdsa")


@then(u'An error message should appear')
def step_impl(context):
	error_message = WebDriverWait(context.driver, 5).until(EC.presence_of_element_located((By.ID, 'errorMessage')))
	error_message.text == "The username or password provided was invalid"