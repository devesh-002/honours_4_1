import os 
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup # 4.9.3
import regex as re
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.command import Command
import requests
import urllib.request
# response = urllib.request.urlopen('http://www.example.com/')
# html = response.read()

# defining a global sleep time to sleep after a page is loaded
sleep_time=0.00001

def scraper_func():

# defining the driver and the url
    i=1
    while(i<36):
        
        url="http://164.100.94.191/niti/best-practices/district-wise-statistics?term_node_tid_depth=All&page="+str(i)
        response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', {'class': 'sticky-enabled'})
        for ii,td in enumerate(table.find_all('td')):
            try:
                x=td.find('a').get('href')
                x="http://164.100.94.191"+x
                print(x)
                response = requests.get(x)
                filename=str(ii)+"_"+str(i)+".xlsx"
                open(filename, "wb").write(response.content)
                # html = response.read()
            except:
                pass
        i+=1
scraper_func()