from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
import os

chrome_driver = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Drivers', 'chromedriver.exe')
os.environ['webdriver.chrome.driver'] = chrome_driver


class ApplicationTest:
    def __init__(self):
        self.wd = webdriver.Chrome(chrome_driver)
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def destroy(self):
        self.wd.quit()