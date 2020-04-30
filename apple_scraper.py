# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd

import csv

with open('result.csv', 'w') as f:
    f.write ("Apple prices, Apple Sale Date \n")
maxpage = 13

driver = webdriver.Chrome()

for i in range (1, maxpage+1):
    url = "https://agrobazar.ru/fruit/sale/apples/moskva_rossiya/?page=" + str(i);
    driver.get(url)
    #extract lists of apple prices and dates by xpath
    aprices = driver.find_elements_by_xpath('//span[@class="pl-price"]')
    adate= driver.find_elements_by_xpath('//div[@class="pl-date"]')
    num_page_items = len(aprices)
    with open ('result_apples.csv','a') as f:
        for i in range(num_page_items):
            f.write(aprices[i].text + "," + adate[i].text + "\n")

# print out all apple prices and dates on one page

# close browser once task is completed
driver.close()