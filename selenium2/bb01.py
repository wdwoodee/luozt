# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Bb01(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.10.5.102/NetBrainNG/app/#/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_bb01(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("admin")
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("admin")
        driver.find_element_by_id("login").click()
        time.sleep(2)
        driver.find_element_by_css_selector(".headerFrame").click()
#        driver.find_element_by_xpath("//div[@id=]")
        time.sleep(2)
        driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
        time.sleep(2)
        driver.find_element_by_css_selector("a.selected > span.ng-binding.ng-scope").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[4]/div/div/div/button").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
