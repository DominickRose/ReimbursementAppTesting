from poms.login_page import LoginPage
from poms.employee_dashboard_page import EmployeeDashboardPage

from behave.runner import Context
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

def before_all(context: Context):
	context.driver = webdriver.Chrome("C:\\Users\\Dominick\\OneDrive\\Desktop\\chromedriver.exe")
	context.login_page = LoginPage(context.driver)
	context.employee_dashboard_page = EmployeeDashboardPage(context.driver)

def after_all(context):
	context.driver.quit()