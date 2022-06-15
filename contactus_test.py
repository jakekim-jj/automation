from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

# driver = webdriver.Chrome(ChromeDriverManager().install()) // Driver in stall
driver = webdriver.Chrome('/Users/jakekim/Selenium/chromedriver')
# Check Chrome driver version. before start...

driver.maximize_window()
driver.get("https://tamwood.com/careers/")

# print("Application title is ",driver.title)
# print("Application url is",driver.current_url)
# driver.quit()

apply_page = driver.find_element_by_class_name("widget.edgt-button-widget")
apply_page.click()
time.sleep(3)

contact_us = driver.find_elements_by_class_name("edgt-btn.edgt-btn-medium")
contact_us[1].send_keys(Keys.ENTER)

# After call new window, Python has to focus on new tab
# first tab is window_handles[0] / Second tab is window_handles[-1] ....
driver.switch_to.window(driver.window_handles[-2])

time.sleep(3)
firstname = driver.find_element(By.NAME, 'general-firstname')


enableStatus = firstname.is_enabled()
# Check is it enabla or not
displayStatus = firstname.is_displayed()
# Check is it displayed or not
print(enableStatus)
print(displayStatus)


firstname.send_keys("firstname")

time.sleep(2)
lastname = driver.find_element(By.NAME, 'general-lastname')

attrData = lastname.get_attribute("type")
#Get attribute of lastname
fontValue = lastname.value_of_css_property("font-size")
#get css property of lastname
print(attrData)
print(fontValue)

lastname.send_keys("lastname")

time.sleep(2)
country = driver.find_element(By.NAME, 'general-citizenship')
country.send_keys("can")

time.sleep(2)
g_email = driver.find_element(By.NAME, 'general-email')
g_email.send_keys("jake@gmail.com")

time.sleep(2)
inquiry = driver.find_element(By.NAME,'general-inquiry')
inquiry.send_keys("This is test inquiry")

time.sleep(5)
driver.quit()
