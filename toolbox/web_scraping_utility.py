from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Add headless option
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')


driver = webdriver.Chrome(options=options)

driver.get('https://www.google.com')

driver.quit()

