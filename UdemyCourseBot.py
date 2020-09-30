import selenium
import time
import urllib
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from python_anticaptcha import AnticaptchaClient, ImageToTextTask
from anticaptchaofficial.recaptchav2proxyless import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings
     
warnings.filterwarnings('ignore')

PATH = "C:\Program Files (x86)\chromedriver.exe" #default path of chromedriver
driver = webdriver.Chrome(PATH)
driver.get("https://www.tutorialbar.com/all-courses/")

udemy_useremail = " " #your udemy login email

udemy_pw = " " #your udemy password


#for getting tutorialsbar links of udemy courses
tutorialbarlinks = driver.find_element_by_class_name("rh-post-wrapper")
hrefs = [x.get_attribute('href') for x in tutorialbarlinks.find_elements_by_css_selector('a')]

temp_var = 0
tutorialslink_list = []
for i in range(0,12):
	tutorialslink_list.append(hrefs[temp_var])
	temp_var += 3

#now for getting the udemy courses coupon links which we will get from tutorialslinks
udemycouponlink_list=[]
for i in range(0,12):
	driver.get(tutorialslink_list[i])
	
	time.sleep(2)
	udemycouponlink = driver.find_element_by_class_name("priced_block")
	udemycouponlist = udemycouponlink.find_element_by_css_selector('a').get_attribute('href')
	if len(udemycouponlist) > 25: #Sometimes it fetches an add link(bit.ly which is 22words), so to escape that we use this
		udemycouponlink_list.append(udemycouponlist)

#login to udemy
driver.get("https://www.udemy.com/join/login-popup/")

#------------------------------------Google re-captcha solver with anti-captcha api--------------------
# googlecaptcha = driver.find_element_by_class_name("g-recaptcha")
# if(googlecaptcha.is_displayed()==True):
# 	try:
# 		solver = recaptchaV2Proxyless ()
# 		solver.set_verbose ( 1 )
# 		solver.set_key ( "" ) #Your anti-captcha api key
# 		solver.set_website_url ( "https://www.udemy.com/join/login-popup/" ) 
# 		solver.set_website_key ( "6Lcj-R8TAAAAABs3FrRPuQhLMbp5QrHsHufzLf7b" )#udemys google recaptcha website key

# 		g_response = solver.solve_and_return_solution ()
# 		if g_response != 0 :
# 		     print  ("g-response:" + g_response)
# 		else:
# 		     print  ("task finished with error" + solver.error_code)
# 	except: 
# 		pass


time.sleep(3)
user_email = driver.find_element_by_name("email") 
user_password = driver.find_element_by_name("password")

user_email.send_keys(udemy_useremail) #enter user email
user_password.send_keys(udemy_pw) #enter user password

driver.find_element_by_name("submit").click()

#now for applying the codes on udemy
for i in range(len(udemycouponlink_list)):
		try:
			driver.get(udemycouponlink_list[i])
			#------------------------------Add to cart/Go to cart----------------------------------
			element_present = EC.presence_of_element_located((By.XPATH, "//button[@data-purpose='buy-this-course-button']"))
			WebDriverWait(driver, 10).until(element_present)

			#------------------------------Click on add to cart/Enroll now---------------------------
			udemyadd_to_cart = driver.find_element_by_xpath("//button[@data-purpose='buy-this-course-button']")
			udemyadd_to_cart.click()


			#--------------------------------Wait for Enroll Button------------------------------------------
			element_present = EC.presence_of_element_located((By.XPATH, "//*[@id=\"udemy\"]/div[1]/div[2]/div/div/div/div[2]/form/div[2]/div/div[4]/button"))
			WebDriverWait(driver, 10).until(element_present)
			#--------------------------------Click on Enroll on Course---------------------------------------
			udemybuy = driver.find_element_by_xpath("//*[@id=\"udemy\"]/div[1]/div[2]/div/div/div/div[2]/form/div[2]/div/div[4]/button") #Udemy
			udemybuy.click()
			
		except BaseException as e:
               		print("You are already in this course or it was just a discount offer!!!")

driver.close()