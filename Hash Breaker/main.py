# Program intended to solve the Challenge "Hash me again"
# found on
# https://ringzer0ctf.com/challenges/56

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from hashlib import sha1

#Using Chrome to access web
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(ChromeDriverManager().install())

#Open the website
browser.get('https://ringzer0ctf.com/challenges/56')

#Checking if connection succeeded
assert 'RingZer0' in browser.title

#Entering username ---You need to fill in your own username for the program to work---
login = browser.find_element_by_name('username')
login.send_keys('sampro')

#Entering password ---You need to fill in your own password for the program to work---
password = browser.find_element_by_name('password')
password.send_keys('56e2a989c155' + Keys.RETURN)

#Retrieving hashkey
message = browser.find_element_by_class_name('message').text.split('\n')[1]

#Hashing the message
key = 0
calculated_hash = ''
while calculated_hash != message:
    calculated_hash =sha1(str(key).encode('utf-8')).hexdigest()
    print("%s = %s" % (calculated_hash, message))
    key += 1

#Sending back the answer
browser.get('https://ringzer0ctf.com/challenges/56/' + str(key-1))
