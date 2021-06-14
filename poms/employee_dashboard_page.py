from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EmployeeDashboardPage:
	def __init__(self, driver: WebDriver) -> None:
		self.driver = driver

	def reimbursement_filter(self):
		return Select(self.driver.find_element_by_id('filterChoices'))
	
	def new_reimbursement_button(self):
		return self.driver.find_element_by_id('newRequestBtn')

	def amount_input(self):
		return self.driver.find_element_by_id('amountInput')

	def reason_input(self):
		return self.driver.find_element_by_id('descriptionInput')

	def submit_request_btn(self):
		return self.driver.find_element_by_id('submitRequestBtn')
	
	def cancel_request_btn(self):
		return self.driver.find_element_by_id('cancelRequestBtn')