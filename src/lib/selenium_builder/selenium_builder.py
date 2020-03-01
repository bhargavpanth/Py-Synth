'''
Redefined from https://selenium-python.readthedocs.io/locating-elements.html
CSS Selectors : https://saucelabs.com/resources/articles/selenium-tips-css-selectors
'''
from selenium.webdriver.common.by import By

class DOM:

	def __init__(self, driver):
		self.driver = driver

	def get(self, url: str):
		return self.driver.get(url)

	def find_element_with_link(self, text: str, partial: bool = False):
		if partial:
			return self.driver.find_element_by_partial_link_text(text)
		else:
			return self.driver.find_element_by_link_text(text)

	def element_by_path(self, path: str):
		return self.driver.find_element_by_xpath(path)

	def input_box(self, element, text: str):
		return element.send_keys(text)

	def find_element(self, path: str):
		return self.driver.find_element(By.XPATH, path)
	
	def find_element_by_id(self, id: str):
		return self.driver.find_element_by_id(id)

	def find_element_by_name(self, name: str):
		return self.driver.find_element_by_name(name)

	def find_element_by_xpath(self, path: str):
		return self.driver.find_element_by_xpath(path)

	def find_element_by_tag_name(self, tag: str):
		return self.driver.find_element_by_tag_name(tag)

	def find_element_by_class_name(self, className: str):
		return self.driver.find_element_by_class_name(className)

	def find_element_by_css_selector(self, cssSelector: str):
		return self.driver.find_element_by_css_selector(cssSelector)


class SeleniumBuilder:

	def __init__(self, driver):
		self.driver = driver

	def build_dom_elements(self):
		return DOM(self.driver)
