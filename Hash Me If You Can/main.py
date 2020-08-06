# Program intended to solve the Challenge "Hash Me If You Can"
# found on
# https://ringzer0ctf.com/challenges/13

from selenium import webdriver
import hashlib

#Using Chrome to access web
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()

#Open the website
browser.get('https://ringzer0ctf.com/challenges/13')

#Checking if connection succeeded
assert 'RingZer0' in browser.title

#Entering username
login = browser.find_element_by_name('username')
login.send_keys('YOUR_USERNAME')

#Entering password (DO NOT SHOW)
password = browser.find_element_by_name('password')
password.send_keys('YOUR_PASSWORD' + Keys.RETURN)

#Retrieving hashkey
message = browser.find_element_by_class_name('message').text.split('\n')

#Hashing the message
hash = hashlib.sha512(message[1].encode()).hexdigest()

#Sending back the answer
browser.get('https://ringzer0ctf.com/challenges/13/'+hash)