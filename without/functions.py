from selenium import webdriver
import time
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

headers = {
        "method": "GET",
        "accept-encoding": "utf-8",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }

def without(url):
    options = Options()
    options.headless = True
    options.add_argument('window-size=1400,600')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument(f'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options, executable_path="/usr/bin/chromedriver")
    driver.get('https://snaptik.app/')   
    input = driver.find_element_by_id('url')
    input.send_keys(url)
    time.sleep(1)
    driver.find_element_by_id('submiturl').click()
    time.sleep(1)
    elms = driver.find_elements_by_xpath("//a[@href]")
    lst = []
    for elem in elms:
        rtr = elem.get_attribute("href")
        lst.append(rtr)
    link = lst[3]
    r = requests.get(link, headers=headers)
    return r