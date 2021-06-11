from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select

class EmployeeDashboardPage:
	def __init__(self, driver: WebDriver) -> None:
		self.driver = driver

	def reimbursement_filter(self):
		return Select(self.driver.find_element_by_id('filterChoices'))
	
	def new_reimbursement_button(self):
		return self.driver.find_element_by_id('newRequestBtn')