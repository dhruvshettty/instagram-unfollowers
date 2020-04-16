"""
Code to find out users
who don't follow you
back on Instagram
"""

from selenium import webdriver
from time import sleep
import config

url = "https://instagram.com"

class InstagramBot:
	def __init__(self, username, password):
		self.driver = webdriver.Chrome("./chromedriver")
		self.username = username
		self.driver.get(url)
		sleep(2)
		# Logging into Instagram
		self.driver.find_element_by_xpath('//input[@name="username"]').send_keys(username)
		self.driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)
		self.driver.find_element_by_xpath('//button[@type="submit"]').click()
		sleep(4)
		# Closing the Push Notifications tab (include only if logging in a new browser)
		self.driver.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()
		sleep(2)

	def get_unfollowers(self):
		# Opening User profile
		self.driver.find_element_by_xpath(f'//a[contains(@href, "/{self.username}/")]').click()
		sleep(4)
		# Opening followers scroll box
		self.driver.find_element_by_xpath(f'//a[contains(@href, "/{self.username}/followers/")]').click()
		followers_list = self._get_names()
		self.driver.find_element_by_xpath(f'//a[contains(@href, "/{self.username}/following/")]').click()
		following_list = self._get_names()
		not_following_back_list = [user for user in following if user not in followers]
		print(not_following_back)

	# Private function to get names from scroll box
	def _get_names(self):
		sleep(2)
		# Add code if you need to remove Suggestions if they appear in the scroll box
		suggestions = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
		self.driver.execute_script('arguments[0].scrollIntoView', suggestions)
		# Selecting scroll box and scrolling it entirely
		scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
		last_height, height = 0, 1
		while last_height != height:
			last_height = height
			sleep(2)
			# Scroll to the end of the scroll box
			# Return height of the scroll box
			height = self.driver.execute_script("""
				arguments[0].scrollTo(0, arguments[0].scrollHeight);
				return arguments[0].scrollHeight;
				""", scroll_box)
		links = scroll_box.find_elements_by_tag_name('a')
		names = [name.text for name in links if name.text != '']
		self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()	# Closing scroll box
		return names



ig_bot = InstagramBot(config.username, config.password)
ig_bot.get_unfollowers()