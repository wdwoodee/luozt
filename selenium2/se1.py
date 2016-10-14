#coding=UTF-8
from selenium import webdriver
import time
try:
 brower=webdriver.Chrome('D:/soft/chromedriver_win32/chromedriver.exe')
 brower.get('http://www.baidu.com')
 time.sleep(2)

 print("浏览器最大化")
 brower.maximize_window()
 time.sleep(2)

 brower.find_element_by_id("kw").send_keys("selenium")
 brower.find_element_by_id("su").click()
 time.sleep(3)

 brower.find_element_by_xpath("//div[@class='result-op c-container xpath-log']/h3/a").click()
 time.sleep(5)

 brower.get('http://baike.baidu.com/link?url=E8UWm1txyH5ravLis08kDaJntSx0k9Lcw2qe2QG1kLQCVHd0jQ5aqii3oL8IwzL6nvd4_08-A1isY0o-j3RekbvMe1Ks41lNl4Klmihax3GnOjs0w7gW63XBIwfqRj7C6yuZzciInGn3GAB9_SKcyK')
 time.sleep(5)
 brower.find_element_by_css_selector("a[title='ThoughtWorks公司开发的web自动化测试工具']").click()
 #brower.find_element_by_xpath("//div[@class='body-wrapper']/div/div/ul/li[1]/a")
 time.sleep(5)
 print (brower.title)
 brower.quit()
except Exception as e:
    print (e)