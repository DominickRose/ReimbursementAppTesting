from behave import given, when, then

@when(u'The manager clicks the view all statistics button')
def step_impl(context):
   context.manager_dashboard_page.stat_link().click() 


@then(u'The page should redirect to the statistics page')
def step_impl(context):
	assert context.driver.title == "Statistics"

@given(u'The manager is on the statistics page')
def step_impl(context):
	context.driver.get("C:/Users/Dominick/VSCodeProjects/ReimbursementApp/html/mgrStatistics.html")


@when(u'The manager clicks the back to dashboard button')
def step_impl(context):
	button = context.driver.find_element_by_id("backBtn")
	button.click()


@then(u'The manager should redirect to the manager dashboard page')
def step_impl(context):
	assert context.driver.title == 'Manager Dashboard'