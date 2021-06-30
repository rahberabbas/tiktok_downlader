from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
driver.get("https://snaptik.app/")
print(driver.title)
driver.quit()