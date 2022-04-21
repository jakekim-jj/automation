from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path="/Users/jakekim/Selenium/chromedriver")
driver.get("http://www.google.com")

print(driver.title)
print(driver.current_url)
# driver.quit()