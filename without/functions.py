from selenium import webdriver
import time
import requests
from pyvirtualdisplay import Display
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
    driver = webdriver.Chrome(options=options)
    driver.get(f'https://ttdownloader.com/?url={url}')
    time.sleep(7)
    elms = driver.find_elements_by_xpath("//a[@href]")
    lst = []
    for elem in elms:
        rtr = elem.get_attribute("href")
        lst.append(rtr)
        # print(rtr)
    link = lst[12]
    r = requests.get(link, headers=headers)
    return r