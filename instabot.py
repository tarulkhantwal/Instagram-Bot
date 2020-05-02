from selenium import webdriver
from secret import pw
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui

class InstaBot:
	tarul=[]
	def __init__(self,username,pw):
		self.driver = webdriver.Chrome(executable_path=r'F:/chromedriver_win32/chromedriver.exe')
		self.username=username
		self.driver.get("https://instagram.com")
		self.driver.maximize_window()
		sleep(2)

		#self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
		self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
		self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
		#self.driver.find_element_by_xpath('//button[@type="submit"]').click()
		self.driver.find_element_by_xpath('//button[@type="submit"]').click()
		sleep(3)
		self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
		sleep(2)

	def get_unfollowers(self):  
		self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username)).click() 
		sleep(2)
		self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()

		  
		following = self._get_names()
		
		self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
			
		followers = self._get_names()
		
		not_following_back = [user for user in following if user not in followers]
		#print(not_following_back)
		#un = int(input("How many accounts would you like to unfollow in the list of "+str(len(not_following_back))))
		nfb = len(not_following_back)
		
		self.driver.implicitly_wait(2)
		
		for i in range(0,nfb):
			self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]').click()
			sleep(2)
			self.random=pyautogui.typewrite("{}".format(not_following_back[i]))
			sleep(2)
			self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(not_following_back[i])).click()
			#self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div[2]/div").click()
			#self.driver.find_element_by_class_name("_5f5mN").click()
			self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button').click()
			self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
		#self.driver.find_element_by_class_name("_6q-tv").click()
		print("ALL THOSE WHO DON'T FOLLOW YOU BACK WERE SUCESSFULLY UNFOLLOWED")



		
	def _get_names(self):
		sleep(2)
		#sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
		scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
		last_ht, ht = 0, 1
		while last_ht != ht:
			last_ht = ht
			sleep(2)
			ht = self.driver.execute_script("""
				arguments[0].scrollTo(0, arguments[0].scrollHeight); 
				return arguments[0].scrollHeight;
				""", scroll_box)
		links = scroll_box.find_elements_by_tag_name('a')
		names = [name.text for name in links if name.text != '']
		# close button
		self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
			.click()
		return names

bot = InstaBot('tar.ul', pw)
bot.get_unfollowers()

