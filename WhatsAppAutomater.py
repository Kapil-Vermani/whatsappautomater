from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
name = 'ABC' # put the name  of person to whom you want to send message
msg = [ '1','2','3','4'] # dummy message list that you want to send
raw_input('Enter anything after scanning QR code')
user = driver.find_elements_by_xpath('//span[@title = 'ABC']') #Replace ABC with name of person to whom you want to send message
print user
user[0].click()
msgbox = driver.find_elements_by_class_name('pluggable-input-compose')
print msgbox
while True:
    for elem in msg :
        msgbox[0].send_keys(elem)
        msgbox[0].send_keys(u'\ue007')
    time.sleep(300) # wait for 5 mins before sending messages
