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
		