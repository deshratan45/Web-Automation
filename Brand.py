from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time
import getpass
import tweepy
import json
# import textile
# import BeautifulSoup
driver = webdriver.Firefox()
driver.get('https://www.myntra.com/')
Search_Box = driver.find_element_by_xpath("//input[@placeholder='Search' or @name='email']")
print(">>>>>>>>>>>")
Brands =["Allen Solly","Manyavar","Being Human","Louis Philippe","Peter England","Police","SHOWOFF","Pepe Jeans","Turtle","Van Heusen","Alcis","Celio","Killer","Lawman pg3","Raymond","Wrangler","Park Avenue","ColorPlus","Integriti"]
for i in range(len(Brands)):
    Search_Box.send_keys(Brands[i])
    time.sleep(5)


    driver.find_element_by_xpath("//ul[@class='desktop-group']//li[. = '"+Brands[i]+"']").click()
    time.sleep(5)
    No=(driver.find_element_by_xpath(".//span[@class = 'horizontal-filters-sub']")).text
    print Brands[i] + No
    Search_Box = driver.find_element_by_xpath("//input[@placeholder='Search' or @name='email']")





print("end")
time.sleep(30)
driver.close()

# driver = webdriver.Firefox()
# driver.get('https://www.myntra.com/')
# Search_Box = driver.find_element_by_xpath("//input[@placeholder='Search' or @name='email']")
# print(">>>>>>>>>>>")
#
# Search_Box.send_keys("Allen Solly")
# time.sleep(3)
# print(">>>>>>>>>>>")
# # Get text from all elements
# # text_contents = [el.text for el in driver.find_elements_by_xpath("//ul[@class='desktop-group']/li")]
# # # Print text
# # for text in text_contents:
# #     print text
# Search_Box.send_keys("Allen Solly")
# # driver.find_element_by_partial_link_text("Allen Solly").click()
# driver.find_element_by_xpath("//ul[@class='desktop-group']//li[. = 'Allen Solly']").click();
#element: //ul[@class='desktop-group']//li[. ='Allen Solly']
# No=(driver.find_element_by_xpath(".//span[@class = 'horizontal-filters-sub']")).text
# print No
#
#
#
#
# print("end")
# time.sleep(30)
# driver.close()
#
