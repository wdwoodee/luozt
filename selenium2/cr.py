#coding=UTF-8
from selenium import webdriver
import time
import unittest
try:

     brower=webdriver.Chrome('D:/soft/chromedriver_win32/chromedriver.exe')
     base_url="http://10.10.5.102/NetBrainNG/app/admin.html"
     verificationErrors = []
     accept_next_alert = True
     brower.get(base_url)
     time.sleep(2)
     brower.find_element_by_xpath("//html/body/div/div/form/div[3]/div[1]/input").clear()
     brower.find_element_by_xpath("//html/body/div/div/form/div[3]/div[1]/input").send_keys("admin")
     brower.find_element_by_xpath("//html/body/div/div/form/div[3]/div[2]/input").clear()
     brower.find_element_by_xpath("//html/body/div/div/form/div[3]/div[2]/input").send_keys("admin")
     brower.find_element_by_id("login").click();
     time.sleep(2)
     brower.find_element_by_xpath("//html/body/div[2]/div/div/div/ul/li[2]/a/tab-heading").click()

except Exception as e:
    print (e)