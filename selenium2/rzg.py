# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import random

class CreateDomain(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('D:/soft/chromedriver_win32/chromedriver.exe')
        #self.driver.implicitly_wait(3)
        self.base_url = "http://10.10.5.222/"
        self.verificationErrors = []
        self.accept_next_alert = True
        driver = self.driver
        driver.get(self.base_url + "/NetBrainNG/app/#/")
        time.sleep(3)
        driver.find_element_by_xpath("//input[@type='text']").clear()
        time.sleep(3)
        driver.find_element_by_xpath("//input[@type='text']").send_keys("admin")#"输入用户名"
        #time.sleep(3)
        driver.find_element_by_xpath("//input[@type='password']").clear()
        #time.sleep(3)
        driver.find_element_by_xpath("//input[@type='password']").send_keys("admin")#"输入密码"
        time.sleep(3)
        driver.find_element_by_id("login").click()
        time.sleep(3)

        driver.maximize_window() #将浏览器最大化显示
        time.sleep(5)

    '''#def test_select_tenant(self,tenaneName):
        tenentList = driver.find_elements_by_css_selector("html.ng-scope body.modal-open div.modal.fade.ng-isolate-scope.tenant-popout.in div.modal-dialog div.modal-content div.TenantPopoutFrame.ng-scope div.sessionFrame div.btn-group.dropdown.ng-isolate-scope.ng-valid.ng-dirty.ng-valid-parse.open ul.dropdown-menu.dropdown-menu-custom")
        for tenent in tenentList.find_elements_by_tag_name("li"):
            if(tenent.find_elements_by_tag_name("a").find_elements_by_tag_name("span").text==tenaneName):
                tenent.click()
            else:
                print("Can't Find tennet!!!")'''


    def test_create_domain(self,strr,num,tenaneName):
        time.sleep(3)
        driver = self.driver
        driver.find_element_by_css_selector(".headerFrame").click()


        time.sleep(3)

        driver.find_element_by_xpath("//div[4]/div/div/div/div[3]/div/button[2]").click()
        time.sleep(3)

        tenentList = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/div/ul") #"进行tenant name匹配"
        for tenent in tenentList.find_elements_by_tag_name("li"):
            if(tenaneName in tenent.find_element_by_tag_name("a").find_element_by_tag_name("span").text):
                print(tenent.find_element_by_tag_name("a").find_element_by_tag_name("span").text)
                tenent.click()

        time.sleep(3)
        driver.find_element_by_xpath("//div[4]/div/div/div/button[3]").click()
        time.sleep(3)
        driver.find_element_by_xpath("(//input[@type='text'])[8]").click()
        time.sleep(3)
        driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
        time.sleep(3)
        driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys(strr) #"给domain命名"
        time.sleep(3)
        driver.find_element_by_xpath("(//input[@type='text'])[10]").click()
        time.sleep(3)
        driver.find_element_by_xpath("(//input[@type='text'])[10]").clear()
        time.sleep(3)
        driver.find_element_by_xpath("(//input[@type='text'])[10]").send_keys(num)# "给domain分配node"
        time.sleep(3)
        driver.find_element_by_xpath("//div[3]/button[3]").click()
        time.sleep(3)
        driver.find_element_by_id("btn_yesDialogBtn").click()


    """def is_element_present(self, how, what):
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
        finally: self.accept_next_alert = True"""

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
    def logOut(self):
        driver = self.driver
        time.sleep(3)
        driver.find_element_by_xpath("//span[3]/div/div/img").click()
        time.sleep(3)
        driver.find_element_by_xpath("//span[3]/ul/li[6]").click()
        time.sleep(3)

if __name__ == "__main__":
    #unittest.main()
        p=CreateDomain()
        p.setUp()
        #p.test_create_domain("aaaa","60","tenant3")

        for i in range(1,101):

            name = random.sample(['a','b','c','d','e','f','g','h','i','j','0','1','2','3','4','5','6','7','8','9'], 3)   #"循环100次，并为每次创建的snapshot命名不同的名称"
            p.test_create_domain(name,"10","tenant1") #"用户选取可以创建domain的tenant"
            print(i)
            time.sleep(3)
            i+=1
        p.logOut()
        p.tearDown()

