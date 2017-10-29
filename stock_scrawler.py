from selenium import webdriver
import pandas as pd
import requests
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
driver.set_page_load_timeout(10)

with open('./stock_list.txt', 'r') as fin:
    company_code_list = fin.read().split("\n")
    i = 0
    for company_code in company_code_list:
        i += 1
        if i == 1:
            continue
        print(company_code)
        url = "http://www.cmoney.tw/finance/f00041.aspx?s=" + company_code.strip()
        #print(url)
        driver.get(url)
        table = driver.find_element_by_css_selector(".tb-out")
        #print(table.get_attribute('innerHTML'))
        df = pd.read_html(table.get_attribute('innerHTML'))
        #print(df[0])
        df[0].to_csv('stock_table/'+company_code+'.csv', index=False)
