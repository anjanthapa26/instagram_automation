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

from applogger import AppLogger

logger = AppLogger(__name__).getlogger()

class InstaCrawler:

    def __init__(self,username = None,password = None,target = None,timeout = 20) -> None:
        self.username = username
        self.password = password
        self.target = target

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
        self.wait = WebDriverWait(self.driver,timeout)
    

    def get_target_url(self):
        self.driver.get(self.baseurl)

    def validate_login(self):
        """
        validate login
        """

        user_profile_xpaths = [
            '//div[@class="_acut"]/div/span/img',
            '//img[contains(@alt, f"{self.username}\'s profile picture")]'
        ]

        for xpath in user_profile_xpaths:
            try:
                logger.info(f'validating login with xpath: {xpath}')
                self.wait.until(EC.presence_of_element_located((By.XPATH,xpath)))
                return True
            except:
                logger.error(f'Could not find user\'s profile')

        return False

    def login(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="username"]'))).send_keys(self.username)
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="password"]'))).send_keys(self.password)
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))).click()
            if not self.validate_login():
                return False
                
            return True
        except:
            return False


