from selenium.webdriver.chrome.webdriver import WebDriver

class EmployeeDashboardPage:
	def __init__(self, driver: WebDriver) -> None:
		self.driver = driver