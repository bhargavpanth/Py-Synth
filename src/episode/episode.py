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
		