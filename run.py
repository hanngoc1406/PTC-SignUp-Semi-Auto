from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from functools import total_ordering
import time

web = webdriver.Chrome()
web.get('https://club.pokemon.com/us/pokemon-trainer-club/sign-up/')
time.sleep(2)


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

# Choose 1996 as year of birth
time.sleep(2)
scrollToYear = web.find_element_by_xpath('//*[@id="id_dob_root"]/div/div/div/div/div[1]/div[1]/div/div/div/ul/li[26]')
scrollToYear.location_once_scrolled_into_view
scrollToYear.click()

# Confirm DOB
confirmDOB = web.find_element_by_xpath('//*[@id="id_dob_root"]/div/div/div/div/div[2]/button')
confirmDOB.click()

# Continue to Register
continueToReg = web.find_element_by_xpath('//*[@id="sign-up-theme"]/section/div/div/div[1]/form/input[2]')
continueToReg.click()



