#coding=UTF-8
from selenium import webdriver
import time


class login_admin():
 def setUp(self):
        self.driver = webdriver.Chrome('D:/soft/chromedriver_win32/chromedriver.exe')
        #self.driver.implicitly_wait(3)
        self.base_url = "http://10.10.5.102/NetBrainNG/app/admin.html"
        self.verificationErrors = []
        self.accept_next_alert = True
        driver = self.driver
        driver.get(self.base_url)
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
 def create_user(self):
     time.sleep(2)
     driver=self.driver
     driver.find_element_by_xpath("//html/body/div[2]/div/div/div/ul/li[2]/a/tab-heading").click()
     driver.find_element_by_css_selector(".default-btns-area a").click()
    # driver.find_element_by_xpath("//html/body/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div[1]/a[1]").click()
#  driver.switch_to_window(driver.window_handles[-1]) # "切换窗口"
 #   driver.find_element_by_xpath("//html/body/div[4]/div/div/div/div[2]/div/fieldset[1]/div[1]/div/input").send_keys("luo")
     time.sleep(2)

if  __name__== "__main__":
    p=login_admin()
    p.setUp()
    p.create_user()