# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.support.ui import WebDriverWait
class Cc01(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.10.5.102/NetBrainNG/app/#/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_cc01(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("cc10")
        time.sleep(2)
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("luozt10")
        time.sleep(2)
        driver.find_element_by_id("login").click()
        time.sleep(5)
        #handles=driver.window_handles
        #print(len(handles))

        #driver.switch_to.window(driver.window_handles[-1])
        time.sleep(15)
      #  driver.switch_to_window(driver.window_handles[-1])

        driver.find_element_by_css_selector("div.headerFrame").click()


    #    driver.find_element_by_xpath("/html/body/div[1]/div/span[1]/div/div/img").click()
     #   driver.find_element_by_link_text("luozhitao").click()
     #   driver.find_element_by_css_selector("img[src*='tenant']").click()
     #   driver.find_element_by_tag_name("headerFrame").find_element_by_tag_name("img").click()
        time.sleep(5)
        driver.find_element_by_xpath("(//button[@type='button'])[6]").click()

        time.sleep(2)
        driver.find_element_by_xpath("//html/body/div[4]/div/div/div/div[3]/div/ul/li/a").click()
        #driver.find_element_by_css_selector("#sizzle1456743779483 > a > span.ng-binding.ng-scope").click()
        time.sleep(2)
        #driver.find_element_by_xpath("//*[@id="1456831743257-0-uiGrid-0005-cell"]/div")
        driver.find_element_by_xpath("//div[@id='1456743781314-0-uiGrid-0005-cell']/div").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[4]/div/div/div/button").click()
        time.sleep(2)
    
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
