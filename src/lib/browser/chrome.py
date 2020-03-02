'''
Defaults
========
command_executor = 'http://localhost:4444/wd/hub'
executable_path = ChromeDriverManager().install()
capabilities = DesiredCapabilities.CHROME
'''
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# utils
# from browser import Browser


class ChromeDriver:
	def __init__(self, executable_path, command_executor, desired_capabilities):
		super(ChromeDriver, self).__init__()
		self.executable_path = executable_path
		self.command_executor = command_executor
		self.desired_capabilities = desired_capabilities

	def get_headless_chrome_driver(self):
		headless_webdriver = None
		try:
			headless_webdriver = webdriver.Remote(
				command_executor=self.command_executor,
				desired_capabilities=self.desired_capabilities
			)
		except Exception as e:
			raise e
		else:
			return headless_webdriver

	def get_chrome_driver(self):
		return webdriver.Chrome(executable_path=self.executable_path)



