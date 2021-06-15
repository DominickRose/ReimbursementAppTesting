from selenium.webdriver.chrome.webdriver import WebDriver 
from selenium.webdriver.support.select import Select

class ManagerDashboardPage():
	def __init__(self, driver: WebDriver):
		self.driver = driver

	def employee_filter_select(self):
		return Select(self.driver.find_element_by_id("employeeFilter"))

	def status_filter_select(self):
		return Select(self.driver.find_element_by_id('statusFilter'))

	def approval_comment_input(self):
		return self.driver.find_element_by_id('approvalCommentInput')

	def cancel_approve_btn(self):
		return self.driver.find_element_by_id('cancelApproveBtn')

	def submit_approve_btn(self):
		return self.driver.find_element_by_id('submitApproveBtn')

	def reject_comment_input(self):
		return self.driver.find_element_by_id('rejectionCommentInput')
	
	def cancel_reject_btn(self):
		return self.driver.find_element_by_id('cancelRejectBtn')

	def submit_reject_btn(self):
		return self.driver.find_element_by_id('submitRejectBtn')