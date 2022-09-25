from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import numpy as np
import pandas as pd

def check_exists_by_xpath(xpath):
    try:
        webdriver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True



Options = webdriver.ChromeOptions()
Options.headless = False
Options.add_argument(r'--user-data-dir=C:\Users\Hp\AppData\Local\Google\Chrome\User Data\Default')
Options.add_argument('--profile-directory=Default')
driver = webdriver.Chrome(executable_path=r'C:\Users\Hp\AppData\Local\Programs\Python\Python39\chromedriver.exe',options= Options)
driver.get('https://web.whatsapp.com/')


user_name_list = ['Group1']
msg='https://www.google.co.in/webhp?source=search_app&gfe_rd=cr&ei=slNDV_vHC5KAoAPFloGoAg&gws_rd=ssl'

time.sleep(15)
# try:
#     user = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label').click()
#     # time.sleep(20)
#     print('1')
# except NoSuchElementException as se:
#     print('2')
#     pass

for user_name in user_name_list:

    try:
        user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()
        # user.text(user_name)
    except NoSuchElementException as se:
        print('no element')
        time.sleep(1)
        pass
    time.sleep(2)
    message_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div')
    # message_box = driver.find_element_by_name("_1UWac _1LbR4")
    message_box.click()
    message_box.send_keys(msg)
    while(True):
        if check_exists_by_xpath('//*[@id="main"]/footer/div[2]/div/div[5]/div[1]'):
            message_box = driver.find_element_by_css_selector('#main > footer > div._2BU3P.tm2tP.copyable-area > div > div > div._2lMWa > div._3HQNh._1Ae7k > button').click()
            break
# dataset = pd.read_csv('list_of_group.csv')
# X = dataset.iloc[:,0].values
# print(X)
# # for y in len(X):
# print(len(X))
# import os
#
#
# # Function to Get the current
# # working directory
# def current_path():
#     print("Current working directory before")
#     print(os.getcwd())
#     print()


# # Driver's code
# # Printing CWD before
# current_path()
#
# # Changing the CWD
# os.chdir('../')
#
# # Printing CWD after
# current_path()