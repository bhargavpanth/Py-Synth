# No Active Support
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
