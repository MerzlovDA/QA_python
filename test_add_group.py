# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
import os
from group import Group

chrome_driver = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Drivers', 'chromedriver.exe')
os.environ['webdriver.chrome.driver'] = chrome_driver

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(chrome_driver)
        self.wd.implicitly_wait(60)
    
    def test_add_group(self):
        success = True
        wd = self.wd
        self.Open_home_page(wd)
        self.Login(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.create_group(wd, Group(name="123", header="123", footer="132"))
        self.return_to_group_page(wd)
        self.loguot(wd)
        self.assertTrue(success)

    def test_add_empty_group(self):
        success = True
        wd = self.wd
        self.Open_home_page(wd)
        self.Login(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.create_group(wd, Group(name="", header="", footer=""))
        self.return_to_group_page(wd)
        self.loguot(wd)
        self.assertTrue(success)

    def loguot(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd, group):
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group firm
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()

    def open_group_page(self, wd):
        # open group page
        wd.find_element_by_link_text("groups").click()

    def Login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def Open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")


    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
