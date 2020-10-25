'''
Defaults
========
command_executor = 'http://localhost:4444/wd/hub'
executable_path = GeckoDriverManager().install()
capabilities = DesiredCapabilities.FIREFOX
'''
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# utils
# from browser import Browser


class FirefoxDriver:
	def __init__(self, executable_path, command_executor, desired_capabilities):
		super(FirefoxDriver, self).__init__()
		self.executable_path = executable_path
		self.command_executor = command_executor
		self.desired_capabilities = desired_capabilities

	def get_headless_firefox_driver(self):
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

	def get_firefox_driver(self):
		return webdriver.Firefox(executable_path=self.executable_path)


class Firefox:
	def __init__(self):
		self.executable_path = GeckoDriverManager().install()
		self.command_executor = 'http://localhost:4444/wd/hub'
		self.capabilities = DesiredCapabilities.FIREFOX
		self.firefox = FirefoxDriver(self.executable_path, self.command_executor, self.capabilities)
	
	def create_browser(self):
		return self.firefox.get_firefox_driver()

	def create_headless_browser(self):
		return self.firefox.get_headless_firefox_driver()


