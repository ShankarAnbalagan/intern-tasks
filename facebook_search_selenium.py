# -*- coding: utf-8 -*-
"""
Created on Fri May 17 23:13:27 2019

@author: User
"""
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://www.facebook.com/nike/')
elem = driver.find_element_by_class_name('_2yav')
elem.click()
driver.save_screenshot('nike.png')
driver.close()
