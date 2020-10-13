# Program intended to solve the Challenge "Can you help me find the answer to this equation"
# found on
# https://ringzer0ctf.com/challenges/32
# TODO : Make general, comment

from selenium import webdriver
import re

#Using Chrome to access web
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()

#Open the website
browser.get('https://ringzer0ctf.com/challenges/32')

#Checking if connection succeeded
assert 'RingZer0' in browser.title

#Entering username
login = browser.find_element_by_name('username')
login.send_keys('sampro')

#Entering password (DO NOT SHOW)
password = browser.find_element_by_name('password')
password.send_keys('56e2a989c155' + Keys.RETURN)

#Retrieving equation
message = browser.find_element_by_class_name('message').text.split('\n')

#Parsing and removing whitespace
equation = re.split(r'([\+\-\=])', message[1].replace(" ", ""))

#Get answer
answer = int(equation[0], 10) + int(equation[2], 16) - int(equation[4], 2)

#Send answer
browser.get('https://ringzer0ctf.com/challenges/32/'+str(answer))
