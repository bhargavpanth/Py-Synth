# Initiate
# import all browsers
# import episode
import os
import time
from lib.browser.chrome import Chrome
from lib.browser.firefox import Firefox
from lib.selenium_builder.selenium_builder import SeleniumBuilder 
from episode.episode import Episode

# to be removed
from selenium.webdriver.common.by import By

# '''
def main():
	print(os.getcwd())

	# firefox = Firefox()
	# driver = firefox.create_browser()

	chrome = Chrome()
	driver = chrome.create_browser()

	episodeReader = Episode(driver, './episodes/login_with_email.json')

	episode = episodeReader.read_episode()

	episodeReader.generate_dom_elements_from_episode()

	# print(episode)



'''
def main():
	firefox = Firefox()
	driver = firefox.create_browser()
	# driver = firefox.create_headless_browser()

	builder = SeleniumBuilder(driver)
	dom = builder.build_dom_elements()
	
	start = time.time()
	driver.get('https://beta.sphere.me')
	# driver.get('https://www.sphere.me/signin')

	one = driver.find_element_by_link_text('Sign in')
	# z = driver.find_element("//a[@class='styled-components__StyledLink-fn65fo-14 czWpGJ']")
	time.sleep(2)
	one.click()

	two = driver.find_element_by_link_text('Sign in with email')
	time.sleep(1)
	two.click()

	# fill up
	three = driver.find_element_by_xpath("//input[@type='email']")
	time.sleep(1)
	three.send_keys('bhargav@sphere.me')

	# click
	four = driver.find_element(By.XPATH, "//span[text()='Sign in']")
	four.click()
	# four = driver.find_element_by_link_text('Sign in')
	# four.click()

	# five
	# check if the message shows up

	end = time.time()

	driver.close()

	print(end-start)
'''

main()

