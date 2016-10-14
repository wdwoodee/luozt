# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Aa01():
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.10.5.102/NetBrainNG/app/admin.html"
        time.sleep(2)
        self.verificationErrors = []
        self.accept_next_alert = True
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath("//input[@type='text']").clear()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@type='text']").send_keys("admin")
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("admin")
        time.sleep(2)
        driver.find_element_by_id("login").click()
        time.sleep(3)
        driver.find_element_by_xpath("//li[2]/a/tab-heading").click()
        time.sleep(3)
       # driver.find_element_by_xpath("//fieldset/div/div/input").click()
    def test_aa01(self,name,passw):
        driver=self.driver
        driver.find_element_by_css_selector(".default-btns-area a").click()
        time.sleep(3)
        driver.find_element_by_xpath("//fieldset/div/div/input").clear()
        time.sleep(2)
        driver.find_element_by_xpath("//fieldset/div/div/input").send_keys(name)

        time.sleep(2)
        driver.find_element_by_xpath("(//input[@type='password'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys(passw)

        driver.find_element_by_xpath("(//input[@type='password'])[3]").click()
        time.sleep(2)
        driver.find_element_by_xpath("(//input[@type='password'])[3]").clear()
        driver.find_element_by_xpath("(//input[@type='password'])[3]").send_keys(passw)
        driver.find_element_by_xpath("//div[5]/div/input").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[5]/div/input").clear()
        driver.find_element_by_xpath("//div[5]/div/input").send_keys("luozhitao@netbrain.com")
        time.sleep(2)
        driver.find_element_by_xpath("(//input[@type='checkbox'])[6]").click()
        driver.find_element_by_css_selector("div.modal-footer > button.btn.btn-primary").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    #unittest.main()
    p=Aa01()
    p.setUp()
    for i in range(1,101):
      name="cc"+str(i)
      passw="luozt"+str(i)
      p.test_aa01(name,passw)

      with open("D:\\lr_work\\tutorial\\NG70225\\username.dat",'a') as f1:
            f1.write(name+"\n")
      with open("D:\\lr_work\\tutorial\\NG70225\\passwd.dat",'a') as f2:
            f2.write(name+"\n")
      time.sleep(1)
    p.tearDown()
