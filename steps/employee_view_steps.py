from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@given(u'The employee is on the employee dashboard page')
def step_impl(context):
    context.driver.get('C:/Users/Dominick/VSCodeProjects/ReimbursementApp/html/empDashboard.html?id=2')


@when(u'The employee selects pending from the filter drop-down menu')
def step_impl(context):
    context.employee_dashboard_page.reimbursement_filter().select_by_visible_text('Pending')

@then(u'The table should display only pending requests')
def step_impl(context):
    all_status = WebDriverWait(context.driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'statusValue')))
    for status in all_status:
	    assert status.text == 'Pending'


@when(u'The employee selects approved from the filter drop-down menu')
def step_impl(context):
    context.employee_dashboard_page.reimbursement_filter().select_by_visible_text('Approved')


@then(u'The table should display only approved requests')
def step_impl(context):
    all_status = WebDriverWait(context.driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'statusValue')))
    for status in all_status:
	    assert status.text == 'Approved'


@when(u'The employee selects rejected from the filter drop-down menu')
def step_impl(context):
    context.employee_dashboard_page.reimbursement_filter().select_by_visible_text('Rejected')


@then(u'The table should display only rejected requests')
def step_impl(context):
    all_status = WebDriverWait(context.driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'statusValue')))
    for status in all_status:
	    assert status.text == 'Rejected'