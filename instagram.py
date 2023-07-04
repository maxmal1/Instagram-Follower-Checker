import time
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

print("Script using selenium to find who does not follow you back on Instagram")
username = input("Please enter your instagram username: ")
password = input("Please enter your instagram password: ")
view = input("Would you like to watch the process? (Y/N): ")
 
 #Option to allow the user to watch the bot scrape data

options = wd.ChromeOptions()
if view == "N":
    options.add_argument("--headless")
driver = wd.Chrome(options=options)
driver.get("https://www.instagram.com/")

time.sleep(3) #waiting for instagram to respond

#login

elem = driver.find_element(By.NAME, "username")

elem.send_keys(username)

elem = driver.find_element(By.NAME, "password")
print(elem)
elem.send_keys(password)
elem.send_keys("\ue007") #selenium "enter" to login

time.sleep(5)

#users profile

driver.get("https://www.instagram.com/"+username+"/following/")

time.sleep(5)


##Getting following list

#scrolling to load the users in the following and followers
#the bot scrolls, collects the names found, then scrolls again
iframe = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
scroll_origin = ScrollOrigin.from_element(iframe)
ActionChains(driver)\
    .scroll_from_origin(scroll_origin, 0, 1000)\
    .perform()

time.sleep(5) #5 seconds is long,could be shortened

following_list = []

i = 1

XPATH_string = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div['+ str(i) +']/div/div/div/div[2]/div/div/span[1]/span/div/div/div/a/span/div'
login_form = True

while login_form:
    XPATH_string = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div['+ str(i) +']/div/div/div/div[2]/div/div/span[1]/span/div/div/div/a/span/div'
    try:
        login_form = driver.find_element(By.XPATH, XPATH_string)
    except:
        login_form = False
        break
    following_list.append(login_form.text)
    if i%10 == 0:
        scroll_origin = ScrollOrigin.from_element(iframe)
        ActionChains(driver)\
            .scroll_from_origin(scroll_origin, 0, 1000)\
            .perform()
        time.sleep(2)
    i+=1

time.sleep(5)

driver.get("https://www.instagram.com/"+username+"/followers/")

time.sleep(10)


iframe = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
scroll_origin = ScrollOrigin.from_element(iframe)
ActionChains(driver)\
    .scroll_from_origin(scroll_origin, 0, 1000)\
    .perform()

time.sleep(5)

followers_list = []

i = 1
XPATH_string = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div['+str(i)+']/div/div/div/div[2]/div/div/span[1]/span/div/div/div/a/span/div'
login_form = True

while login_form:
    XPATH_string = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div['+str(i)+']/div/div/div/div[2]/div/div/span[1]/span/div/div/div/a/span/div'
    try:
        login_form = driver.find_element(By.XPATH, XPATH_string)
    except:
        login_form = False
        break
    followers_list.append(login_form.text)
    if i%10 == 0:
        scroll_origin = ScrollOrigin.from_element(iframe)
        ActionChains(driver)\
            .scroll_from_origin(scroll_origin, 0, 1000)\
            .perform()
        time.sleep(2)
    i+=1

print("These users do not follow you back:")

for i in following_list:
    if i not in followers_list:
        print(i)
