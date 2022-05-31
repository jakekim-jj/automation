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
firstname.send_keys("firstname")
time.sleep(2)

lastname = driver.find_element(By.NAME, 'general-lastname')
lastname.send_keys("lastname")
time.sleep(2)








# time.sleep(5)
# link = driver.find_element_by_link_text("Camps")
# link.click()


# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element((By.CLASS_NAME, "edgt-btn-text"))
#     )
#     element.click()
#     # element = WebDriverWait(driver, 10).until(
#     #     EC.presence_of_element_located((By.NAME, "careersfull-firstname"))
#     # )
#     # element.click()
# finally:
#     driver.quit()