from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path="/Users/jakekim/Selenium/chromedriver")
driver.get("https://techwithtim.net")
time.sleep(5)

print(driver.title)
print(driver.current_url)

#To find elements Id // Name // Class

search = driver.find_element(By.CLASS_NAME,"search-field")
search.send_keys("test")
search.send_keys(Keys.RETURN)

time.sleep(5)


# bring all articles ID = "main"
try:
    main = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articles = driver.find_element(By.ID, "main")
    for article in articles:
        header = driver.find_element(By.CLASS_NAME, "entry-summary")
        print(header.text)
finally:
    driver.quit()
