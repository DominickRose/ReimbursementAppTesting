from selenium.webdriver.chrome.webdriver import WebDriver 
from selenium.webdriver.support.select import Select

class ManagerDashboardPage():
	def __init__(self, driver: WebDriver):
		self.driver = driver

	def employee_filter_select(self):
		return Select(self.driver.find_element_by_id("employeeFilter"))

	def status_filter_select(self):
		return Select(self.driver.find_element_by_id('statusFilter'))