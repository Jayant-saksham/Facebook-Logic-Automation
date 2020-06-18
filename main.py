from selenium import webdriver                              # pip install selenium
from webdriver_manager.chrome import ChromeDriverManager    # pip install webdriver_manager
from webdriver_manager.firefox import GeckoDriverManager
import time


# Initiliazing Webdriver
try:
	driver = webdriver.Chrome(ChromeDriverManager().install())
except:
	driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

def FacebookLogin():
    # Input Email and Password
	user=input('Enter Email Id: ')  
	password=input('Enter Password: ')

	#Opening Facebook.
    # print ('Opening facebook......')
	driver.get('https://www.facebook.com/') 
	print ("Facebook Opened") 
	time.sleep(1) 
	  
    #Entering Email and Password
	username_box = driver.find_element_by_id('email') 
	username_box.send_keys(user) 
	print ("Email Id entered") 
	time.sleep(1) 
	  
	password_box = driver.find_element_by_id('pass') 
	password_box.send_keys(password) 
	print ("Password entered") 

	#Pressing The Login Button  
	login_box = driver.find_element_by_id('loginbutton') 
	login_box.click() 

	  
	print ("Done") 
	input('Press anything to quit') 
	driver.quit() 
	print("Finished")

if __name__ == "__main__":
    FacebookLogin()


