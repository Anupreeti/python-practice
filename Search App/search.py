from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# OPTIONAL: Give full path to chromedriver if not in PATH
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Wait for page to load
time.sleep(2)

# Locate the search box
search_box = driver.find_element(By.NAME, "q")

# Type the query and hit Enter
search_box.send_keys("DevOps jobs remote")
search_box.send_keys(Keys.RETURN)

# Wait to see results
time.sleep(5)

# Close browser
driver.quit()
