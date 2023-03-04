# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
 
from time import sleep

class GetdataSpider(scrapy.Spider):
    name = 'getdata'
    allowed_domains = ['blogabet.com']
    start_urls = ['http://www.blogabet.com']

    def parse(self, response):

        url = 'http://www.blogabet.com'
        self.driver = webdriver.Chrome('C:\DRIVERS\chromedriver_win32\chromedriver.exe')
        self.driver.get(url)
        sleep(5)
        self.driver.find_element_by_class_name('btn-success').click()
        sleep(5)
        self.driver.find_element_by_class_name('btn-outline').click()
        sleep(5)
        username = self.driver.find_element_by_id('email')
        password =  self.driver.find_element_by_id('password')
        username.send_keys("lucasdautz@gmx.de")
        sleep(5)
        password.send_keys("IC2023,")
        self.driver.find_element_by_class_name('btn-danger').click()
        sleep(5)
        
