import os
os.environ['PATH']
from seleniumextractor import SeleniumExtractor
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from decimal import *
from selenium_error import *
from configReader_MB import configReader_MB
import random
import logging
import logging.config
import sys
import pandas as pd
import time

param1 = str((sys.argv)[1])

print("param is", param1)
def _get_config_details():
    return (configReader_MB.get_setting_all())

def _get_config(property):
    return(configReader_MB.get_setting(property))
    return(configReader_MB.get_setting(property))


def _run_screener(sel,url,path):
    selextractor.driver.get(url)
    sel.get_elem_by_id("runScreenButton").click()
    data1 = sel.get_elem_by_xpath(path).text.split(" ")
    return(data1[0])

def _run_screener_crypto(sel,url,path):
    selextractor.driver.get(url)
    sel.get_elem_by_id("runScreenButton").click()

    #data1 = sel.get_elem_by_xpath(path).text.split(" ")

    data1 = sel.get_elem_by_id("results")
    print("data1",data1)
    nr = {"number_of_matches":0}
    for row in data1.find_elements_by_css_selector('tr'):
        if row == data1.find_elements_by_css_selector('tr')[-1]:
            # this is the last element of the loop
            for cell in row.find_elements_by_tag_name('td')[:1]:

                nr1 = cell.text.split(" ")[0]
            #print("nr1 is",row)
                for k in nr.keys():
                    nr['number_of_matches'] = nr1
    print("nr dict",nr)
    return(nr)

def _run_screener_crypto_hist(sel,url,path):

    left_button_xpath = "/html/body/table[2]/tbody/tr/td[2]/table[3]/tbody/tr/td/table[1]/tbody/tr[1]/td/div/table/tbody/tr/td[3]/table/tbody/tr[2]/td[1]/a"
    date_xpath = "/html/body/table[2]/tbody/tr/td[2]/table[3]/tbody/tr/td/table[1]/tbody/tr[1]/td/div/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]"
    sel.get_elem_by_xpath(left_button_xpath).click()
    #sel.get_elem_by_id("runScreenButton").click()

    date_str = sel.get_elem_by_xpath(date_xpath).text.split(" ")[1]

    data1 = sel.get_elem_by_id("results")
    print("data1",data1)
    nr = {"number_of_matches":0,"date":""}
    for row in data1.find_elements_by_css_selector('tr'):
        if row == data1.find_elements_by_css_selector('tr')[-1]:
            # this is the last element of the loop
            for cell in row.find_elements_by_tag_name('td')[:1]:

                nr1 = cell.text.split(" ")[0]
            #print("nr1 is",row)
                for k in nr.keys():
                    nr['number_of_matches'] = nr1
    #print("nr dict",nr)
    nr['date']=date_str
    return(nr)

def _save_csv(file_name,datalist):
    date_list=[]
    count_list=[]
    for i in range(len(datalist)):
        print("record",datalist[i])
        #df.append(pd.DataFrame(datalist[i], index=[0]), ignore_index=True)

        date_list.append(datalist[i]['date'])
        count_list.append(datalist[i]['number_of_matches'])
    date_ser = pd.Series(date_list)
    count_ser = pd.Series(count_list)
    df = pd.DataFrame()
    df['date'] = date_ser
    df['count'] = count_ser
    print(df)

    df.to_csv(file_name,index=False)
marketinout_loginurl = _get_config("login_link")
marketinout_username = _get_config("username")
selextractor = SeleniumExtractor(marketinout_loginurl)
elem = selextractor.get_elem_by_id("l")
elem.send_keys(marketinout_username)
elem = selextractor.get_elems_by_class("button")[0].click()


if ("asx" == param1):
        _match_xpath = _get_config("match_xpath")
        _20sma_url = _get_config("20sma")
        _20sma_below_url = _get_config("20sma_below")
        _50sma_url = _get_config("50sma")
        _50sma_below_url = _get_config("50sma_below")
        _20percent_up_url = _get_config("20percent_up")
        _20percent_down_url = _get_config("20percent_down")
        _4_5percent_up_url = _get_config("4.5percent_up")
        _4_5percent_down_url = _get_config("4.5percent_down")

        _4_5percent_up_count = _run_screener_crypto(selextractor,_4_5percent_up_url,_match_xpath)
        _4_5percent_down_count = _run_screener_crypto(selextractor,_4_5percent_down_url,_match_xpath)
        _20percent_up_count = _run_screener_crypto(selextractor,_20percent_up_url,_match_xpath)
        _20percent_down_count = _run_screener_crypto(selextractor,_20percent_down_url,_match_xpath)
        _20sma_up_count = _run_screener_crypto(selextractor,_20sma_url,_match_xpath)
        _20sma_below_count = _run_screener_crypto(selextractor,_20sma_below_url,_match_xpath)
        _50sma_up_count = _run_screener_crypto(selextractor,_50sma_url,_match_xpath)
        _50sma_below_count = _run_screener_crypto(selextractor,_50sma_below_url,_match_xpath)
        #print(_20sma_up_count,_20sma_below_count,_50sma_up_count,_50sma_below_count,_20percent_up_count,_20percent_down_count,_4_5percent_up_count,_4_5percent_down_count)
        print(_4_5percent_up_count['number_of_matches'],_4_5percent_down_count['number_of_matches'],_20percent_up_count['number_of_matches'],_20percent_down_count['number_of_matches'],_20sma_up_count['number_of_matches'],_20sma_below_count['number_of_matches'],_50sma_up_count['number_of_matches'],_50sma_below_count['number_of_matches'])
elif("crypto" == param1):
        # marketinout_testurl = _get_config("test_link")
        # selextractor = SeleniumExtractor(marketinout_testurl)

        _match_xpath = _get_config("match_xpath_crypto")
        _20sma_url = _get_config("20sma_crypto")
        _20sma_below_url = _get_config("20sma_crypto_below")
        _50sma_url = _get_config("50sma_crypto")
        _50sma_below_url = _get_config("50sma_crypto_below")
        _20percent_up_url = _get_config("20percent_crypto_up")
        _20percent_down_url = _get_config("20percent_crypto_down")
        _9_5percent_up_url = _get_config("9.5percent_crypto_up")
        _9_5percent_down_url = _get_config("9.5percent_crypto_up")
        _9_5percent_up_count = _run_screener_crypto(selextractor, _9_5percent_up_url, _match_xpath)
        _9_5percent_down_count = _run_screener_crypto(selextractor, _9_5percent_down_url, _match_xpath)
        _20percent_up_count = _run_screener_crypto(selextractor, _20percent_up_url, _match_xpath)
        _20percent_down_count = _run_screener_crypto(selextractor, _20percent_down_url, _match_xpath)
        _20sma_up_count = _run_screener_crypto(selextractor, _20sma_url, _match_xpath)
        _20sma_below_count = _run_screener_crypto(selextractor, _20sma_below_url, _match_xpath)
        _50sma_up_count = _run_screener_crypto(selextractor, _50sma_url, _match_xpath)
        _50sma_below_count = _run_screener_crypto(selextractor, _50sma_below_url, _match_xpath)
        # print(_20sma_up_count,_20sma_below_count,_50sma_up_count,_50sma_below_count,_20percent_up_count,_20percent_down_count,_4_5percent_up_count,_4_5percent_down_count)
        print(_9_5percent_up_count['number_of_matches'], _9_5percent_down_count['number_of_matches'], _20percent_up_count['number_of_matches'], _20percent_down_count['number_of_matches'], _20sma_up_count['number_of_matches'],_20sma_below_count['number_of_matches'], _50sma_up_count['number_of_matches'], _50sma_below_count['number_of_matches'])
elif ("asxhist" == param1):
    print("something")
    _match_xpath = _get_config("match_xpath")
    _20sma_url = _get_config("4.5percent_up")
    go_back_period = 99
    selextractor.driver.get(_20sma_url)
    selextractor.get_elem_by_id("runScreenButton").click()
    df = pd.DataFrame()
    data_list =[]

    for i in range(go_back_period):
        #url = _20sma_url + '&mov=' + '-' + i
        time.sleep(3)
        _20sma_up_count = _run_screener_crypto_hist(selextractor, _20sma_url, _match_xpath)
        print(_20sma_up_count['date'],_20sma_up_count['number_of_matches'])
        data_list.append(_20sma_up_count)
    #print(data_list)


    _save_csv("C_9_5percent_up_hist.csv",data_list)