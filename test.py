from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome('/Users/jakekim/Selenium/chromedriver')
driver.maximize_window()
driver.get("http://www.google.com")

print("Application title is ",driver.title)
print("Application url is",driver.current_url)
# driver.quit()