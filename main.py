from selenium import webdriver
import time
from moviepy.editor import *
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
    return lst[12]


without('https://www.tiktok.com/@argenis_1999/video/6967870054994087174?sender_device=pc&sender_web_id=6969977128956642817&is_from_webapp=v1&is_copy_url=0')