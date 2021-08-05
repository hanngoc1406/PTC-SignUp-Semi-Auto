from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from functools import total_ordering
import time
from setup import userName, password

web = webdriver.Chrome()
web.get('https://club.pokemon.com/us/pokemon-trainer-club/sign-up/')
time.sleep(1)


# Accept Cookies
acp = web.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]')
acp.click()

# Set dob
# Open dob pop-up
dob = web.find_element_by_xpath('//*[@id="id_dob"]')
dob.click()


# Open year option
yearPressed = web.find_element_by_xpath('//*[@id="id_dob_root"]/div/div/div/div/div[1]/div[1]/div/label')
yearPressed.click()

# Choose 1996 as the year of birth
time.sleep(2)
scrollToYear = web.find_element_by_xpath('//*[@id="id_dob_root"]/div/div/div/div/div[1]/div[1]/div/div/div/ul/li[26]')
scrollToYear.location_once_scrolled_into_view
scrollToYear.click()

# Confirm DOB
confirmDOB = web.find_element_by_xpath('//*[@id="id_dob_root"]/div/div/div/div/div[2]/button')
confirmDOB.click()

# Continue to SignUp
continueToReg = web.find_element_by_xpath('//*[@id="sign-up-theme"]/section/div/div/div[1]/form/input[2]')
continueToReg.click()

# auto-fill every field
f = open("index.txt", "r")
index = f.read()
userN = web.find_element_by_xpath('//*[@id="id_username"]')
finalUser = userName + str(index)

# Return check = 1 
if(userN.send_keys(finalUser) == True):
    check = 0
else:
    check = 1

# Plus index plus 1
if(check == 1):
    f = open("index.txt", "w")
    intIndex = int(index)
    newIndex = intIndex + 1
    f.write(str(newIndex))

# Password and confirm password
passW = web.find_element_by_xpath('//*[@id="id_password"]')
passW.send_keys(password)
passW_cf = web.find_element_by_xpath('//*[@id="id_confirm_password"]')
passW_cf.send_keys(password)

# Email and confirm email
email = web.find_element_by_xpath('//*[@id="id_email"]')
email.send_keys(finalUser + '@hieucuoi.tech')
email = web.find_element_by_xpath('//*[@id="id_confirm_email"]')
email.send_keys(finalUser + '@hieucuoi.tech')

# Accept the Pokemon.com Terms of Use.
acceptTerm = web.find_element_by_xpath('//*[@id="id_terms"]')
acceptTerm.click()

while (True):
    time.sleep(10)
    try:
        Finish = web.find_element_by_css_selector('#sign-up-theme > section > div > div > div.form-wrapper.color-block.color-block-lightgray.dog-ear-tl.match > h3')
        web.quit()
        break
    except:
        continue

