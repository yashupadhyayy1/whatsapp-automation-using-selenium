# Hey reader , this code is written by yash .
# code one is for the use of

import time
import pyautogui
from selenium import webdriver
# driver = webdriver.Firefox(executable_path=r'C:\Users\Hp\AppData\Local\Programs\Python\Python39\geckodriver.exe')
a = webdriver.ChromeOptions()
a.headless = False
driver = webdriver.Chrome(executable_path=r'C:\Users\Hp\AppData\Local\Programs\Python\Python39\chromedriver.exe',options=a)

driver.get('https://web.whatsapp.com/')


time.sleep(10)
pyautogui.press('tab')

time.sleep(5)
contact = '8764282935'
pyautogui.typewrite(contact)
time.sleep(30)
pyautogui.press('enter')
time.sleep(5)
msg = 'https://us05web.zoom.us/j/82551155962?pwd=MTFWTlQrVjFYY0lMamJUT25OR1VlUT09'
pyautogui.typewrite(msg)
time.sleep(10)
pyautogui.press('enter')
#########################################################################################################################

#2nd Way
#
# import subprocess
# import time
# import pyautogui
#
# subprocess
# subprocess.call('C://Users//Hp//AppData//Local//WhatsApp//WhatsApp.exe')
# time.sleep(20)
# pyautogui.press('tab')
# time.sleep(5)
# contact = 'Me1'
# pyautogui.typewrite(contact)
# time.sleep(3)
# pyautogui.press('enter')
# time.sleep(10)
# msg = 'http://www.lionexpress.in/rajasthan/the-lock-down-will-be-held-in-the-state-from-may-5-to-may-24-the-wedding-ceremony-will-be-banned-till-may-3111/'
# time.sleep(4)
# pyautogui.typewrite(msg)
# for i in range(0):
#     pyautogui.typewrite(msg)
#     time.sleep(5)
#     pyautogui.press('enter')

#########################################################################################################################
# #3nd Way
# # Not using and keyboard buttons import pyautogui
# from selenium import webdriver
# driver = webdriver.Firefox(executable_path=r'C:\Users\Hp\AppData\Local\Programs\Python\Python38\geckodriver.exe')
# # driver = webdriver.Chrome(executable_path=r'C:\Users\Hp\AppData\Local\Programs\Python\Python38\chromedriver.exe')
# driver.get('https://web.whatsapp.com/')
# driver.maximize_window()
#
# contact = '+918764282935'
# msg = 'h'
#
#
# # pyautogui.press('enter')
# # time.sleep(5)
# # msg = 'https://us05web.zoom.us/j/82551155962?pwd=MTFWTlQrVjFYY0lMamJUT25OR1VlUT09'
# # pyautogui.typewrite(msg)
# # time.sleep(10)
# # pyautogui.press('enter')
#
# user = driver.find_element_by_xpath("//span[@title='{}']".format(contact))
# user.click()
# # /html/body/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div/div[8]/div/div/div[2]/div[1]/div[1]/span/span
# #
# #
# # /html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]
# #
# #
# # /html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[3]/button
