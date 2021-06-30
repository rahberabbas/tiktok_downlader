from selenium import webdriver
from selenium.webdriver.chrome.options import Options
headers = {
        "method": "GET",
        "accept-encoding": "utf-8",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }
options = Options()
options.headless = True
options.add_argument('window-size=1400,600')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
driver.get("https://snaptik.app/")
print(driver.title)
driver.quit()