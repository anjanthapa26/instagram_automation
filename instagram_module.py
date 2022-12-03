# This is the main section of the program that takes the username and password as input
# and crawls through the web and automates task
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import keys
from selenium.webdriver.remote.webelement import WebElement


class InstaCrawler:

    def __init__(self,username = None,password = None) -> None:
        self.username = username
        self.password = password

        #chrome 
        options = ChromeOptions()
        options.add_argument("--disable-notifications")
        options.add_experimental_option('excludeSwitches',['enable-logging'])
        options.add_argument("--log-level=3")
        options.add_argument('start-maximized')
        options.add_experimental_option('detach',True)

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

        self.baseurl = "https://www.instagram.com"
        self.targeturl = self.baseurl
    

    def get_target_url(self):
        self.driver.get(self.baseurl)


insta = InstaCrawler()
insta.get_target_url()