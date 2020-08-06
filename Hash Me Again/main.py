# Program intended to solve the Challenge "Hash me again"
# found on
# https://ringzer0ctf.com/challenges/14

from selenium import webdriver
import hashlib

#Function to convert from Binary to String
#Ref : https://stackoverflow.com/questions/37590412/converting-binary-to-ascii-and-ascii-to-binary
def toString(binaryString):
    return "".join([chr(int(binaryString[i:i+8],2)) for i in range(0,len(binaryString),8)])

#Using Chrome to access web
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()

#Open the website
browser.get('https://ringzer0ctf.com/challenges/14')

#Checking if connection succeeded
assert 'RingZer0' in browser.title

#Entering username
login = browser.find_element_by_name('username')
login.send_keys('YOUR_USER_NAME')

#Entering password (DO NOT SHOW)
password = browser.find_element_by_name('password')
password.send_keys('YOUR_PASSWORD' + Keys.RETURN)

#Retrieving hashkey
message = browser.find_element_by_class_name('message').text.split('\n')
print(message)

#Hashing the message
hash = hashlib.sha512(toString(message[1]).encode()).hexdigest()

#Sending back the answer
browser.get('https://ringzer0ctf.com/challenges/14/'+hash)
