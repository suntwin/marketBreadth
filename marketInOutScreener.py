from seleniumextractor import SeleniumExtractor
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium_error import *

def _run_screener(sel,url,path):
    selextractor = SeleniumExtractor(url)
    selextractor.driver.get(url)
    sel.get_elem_by_id("runScreenButton").click()
    data1 = sel.get_elem_by_xpath(path).text.split(" ")
    return(data1[0])

def _run_screener_crypto(sel,url,path):
    #selextractor = SeleniumExtractor(url)
    sel.driver.get(url)
    sel.get_elem_by_id("runScreenButton").click()

    #data1 = sel.get_elem_by_xpath(path).text.split(" ")

    data1 = sel.get_elem_by_id("results")
    print("data1",data1)
    nr = {"number_of_matches":0}
    #for row in data1.find_elements_by_css_selector('tr'):
    for row in data1.find_elements(By.CSS_SELECTOR, 'tr'):
        #if row == data1.find_elements_by_css_selector('tr')[-1]:
        if row == data1.find_elements(By.CSS_SELECTOR, 'tr')[-1]:
            # this is the last element of the loop
            #for cell in row.find_elements_by_tag_name('td')[:1]:
             for cell in row.find_elements(By.TAG_NAME, 'td')[:1]:
                nr1 = cell.text.split(" ")[0]
            #print("nr1 is",row)
                for k in nr.keys():
                    nr['number_of_matches'] = nr1
    print("nr dict",nr)
    return(nr['number_of_matches'])

def _run_screener_crypto_hist(sel,url,path):

    left_button_xpath = "/html/body/table[2]/tbody/tr/td[2]/table[3]/tbody/tr/td/table[1]/tbody/tr[1]/td/div/table/tbody/tr/td[3]/table/tbody/tr[2]/td[1]/a"
    date_xpath = "/html/body/table[2]/tbody/tr/td[2]/table[3]/tbody/tr/td/table[1]/tbody/tr[1]/td/div/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]"
    sel.get_elem_by_xpath(left_button_xpath).click()
    #sel.get_elem_by_id("runScreenButton").click()

    date_str = sel.get_elem_by_xpath(date_xpath).text.split(" ")[1]

    data1 = sel.get_elem_by_id("results")
    print("data1",data1)
    nr = {"number_of_matches":0,"date":""}
    for row in data1.find_elements(By.CSS_SELECTOR, 'tr'):
        if row == data1.find_elements(By.CSS_SELECTOR, 'tr')[-1]:
            # this is the last element of the loop
            for cell in row.find_elements(By.TAG_NAME, 'td')[:1]:

                nr1 = cell.text.split(" ")[0]
            #print("nr1 is",row)
                for k in nr.keys():
                    nr['number_of_matches'] = nr1
    #print("nr dict",nr)
    nr['date']=date_str
    return(nr)