'''
Args

-h Headless mode
-g GUI mode
-browser (options)
	firefox
	chrome
-url URL
-episode path/to/episode
-epoch number of times to replay the episode

Optional args (WIP)
DOM rendering performance
'''

import argparse
import re
import os
import urllib3
import json

parser = argparse.ArgumentParser(description='')

parser.add_argument('-u', '-url', type=str, required=True, help='URL')
parser.add_argument('--e', '--epoch', type=str, help='Epoch')
parser.add_argument('-ep', '-episode', type=str, required=True, help='Path to episode')

browser = parser.add_mutually_exclusive_group()
browser.add_argument('-f', '-firefox', action='store_true', help='Browser (Firefox)')
browser.add_argument('-c', '-chrome', action='store_true', help='Browser (Chrome)')

browser_mode = parser.add_mutually_exclusive_group()
browser_mode.add_argument('-H', '-headless', action='store_true', help='Browser mode - Headless')
browser_mode.add_argument('-g', '-gui', action='store_true', help='Browser mode - GUI')


class Initiate:
	def __init__(self, url, epoch, episode, browser, browser_mode):
		self.url = url
		self.epoch = epoch
		self.episode = episode
		self.browser = browser
		self.browser_mode = browser_mode


	def validate_url(self):
		print('Validating URL...')
		# django url validation regex
		regex = re.compile(
	        r'^(?:http|ftp)s?://'
	        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
	        r'localhost|'
	        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
	        r'(?::\d+)?'
	        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
		is_url_valid = re.match(regex, self.url) is not None
		if is_url_valid:
			print('URL valid')
			return is_url_valid
		else:
			print('URL invalid')
			exit(1)


	def validate_episode_path(self):
		# check if that path to espisode exists
		# read the json object
		# validate the JSON object
		pass


	def check_browser_availability(self):
		# check if firefox or chrome is installed and available
		if self.browser is 'firefox':
			return os.path.exists('/Volumes/Firefox')
		elif self.browser is 'chrome':
			return os.path.exists('/Volumes/Google Chrome')


	def check_headless_browser_availability(self):
		hub_url = 'http://localhost:4444/grid/api/hub'
		http = urllib3.PoolManager()
		try:
			res = http.request('GET', hub_url)
		except Exception as e:
			print('Selenium grid not running...')
			print('Run `docker-compose up` at the root of the project')
			exit(1)
			# raise e
		else:
			self.selenium_config = json.loads(res.data.decode('utf-8'))
			print('selenium running')
			print(self.selenium_config)

	def is_browser_available(self):
		print(self.browser_mode)
		if self.browser_mode is 'gui':
			if self.check_browser_availability():
				print('Browser available : ', self.browser)
			else:
				print('Browser unavailable. Choose another browser')
				exit(1)
		elif self.browser_mode is 'headless':
			return self.check_headless_browser_availability()

	
	def validate_options(self):
		'''
		check for the following
		-u must be a valid URL
		-ep must be a valid path
		-f or -c with -g must be available
		'''
		self.validate_url()
		self.is_browser_available()
		self.validate_episode_path()


def main(url, epoch, episode, browser, browser_mode):
	init = Initiate(url, epoch, episode, browser, browser_mode)
	init.validate_options()

if __name__ == '__main__':
	args = parser.parse_args()

	if args.f:
		browser = 'firefox'
	elif args.c:
		browser = 'chrome'

	if args.H:
		browser_mode = 'headless'
	elif args.g:
		browser_mode = 'gui'

	main(args.u, args.e, args.ep, browser, browser_mode)


