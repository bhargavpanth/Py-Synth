'''
'''
import json
import time
from jsonschema import validate
from selenium.webdriver.common.by import By
# from schema import Schema
from lib.selenium_builder.selenium_builder import SeleniumBuilder

class Episode:
	def __init__(self, driver, episode_path):
		self.driver = driver
		self.episode_path = episode_path
		self.selenium_builder = SeleniumBuilder(self.driver).build_dom_elements()
		self.episode = None

	def read_episode(self):
		# read episode from episode path
		try:
			with open(self.episode_path, 'r') as json_data:
				episode = json.load(json_data)
				self.episode = episode
		except Exception as e:
			print('Unable to open file path to episode')
			raise e
		else:
			return episode


	def validate_episode(self):
		# from the path of the episode
		# json.load the content
		# and validate the JSON content
		pass


	def generate_click_operation(self, step):
		element = step['element']

		if element == 'anchor':
			if 'text' in step:
				el = self.selenium_builder.find_element_with_link(step['text'])
				el.click()
				time.sleep(1)
				return el
		# else:
		# 	return self.selenium_builder.

		elif element == 'button':
			if 'text' in step:
				path = '//button[text()=\'' + step['text'] + '\']'
				el = self.selenium_builder.find_element()
				el.click()
				return el
			
			elif 'id' in step:
				pass
			
			elif 'class' in step:
				pass
			
			else:
				pass

		elif element == 'span':
			if 'text' in step:
				path = '//span[text()=\'' + step['text'] + '\']'
				el = self.selenium_builder.find_element(path)
				el.click()
				return el

		# check for ID and class


	def generate_input_operation(self, step):
		element = step['element']

		if element == 'input':

			if 'type' in step:
				path = '//input[@type=\'' + str(step['type']) + '\']'
				el = self.selenium_builder.element_by_path(path)
				text = str(step['input'])
				self.selenium_builder.input_box(el, text)
				return el

			if 'placeholder' in step:
				path = '//input[@placeholder=\'' + str(step['placeholder']) + '\']'
				el = self.selenium_builder.element_by_path(path)
				text = str(step['input'])
				self.selenium_builder.input_box(el, text)
				return el

			elif 'id' in step:
				# check for class
				if 'class' in step:
					pass
				pass

			elif 'class' in step:
				pass

			else:
				pass

		else:
			print('element must be an input')
			exit(1)


	def timeout(self, timout: int = 2):
		time.sleep(timeout)


	def generate_dom_elements_from_episode(self):
		if self.episode is None:
			print('episode not loaded')

		print('Generating DOM elements for episode: ',self.episode['title'])

		seed_driver = self.driver.get(self.episode['seed_url'])

		for step in self.episode['steps']:

			print('generating step: ', step['name'])
			
			if step['operation'] == 'click' :
				self.generate_click_operation(step['DOM_element'])

			elif step['operation'] == 'input' :
				self.generate_input_operation(step['DOM_element'])

			else:
				print('unindentified operation')
				exit(1)



# if __name__ == '__main__':
# 	dom = SeleniumBuilder()
# 	main()
		