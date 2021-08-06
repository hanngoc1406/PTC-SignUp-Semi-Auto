from typing import Optional
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from functools import total_ordering
import time

f = open("index.txt", "r")
index = f.read()
f.close()
userName = input('Username: ')
password = input('Password: ')
mail = input('Duoi mail (bat dau bang @): ')
n = input('Nhap so tai khoan muon tao: ')

t = int(n)
i = int(index)


while(t != 0):

    # Call webdriver
    option = webdriver.ChromeOptions()
    option.add_argument("--start-maximized")
    web = webdriver.Chrome(chrome_options=option)
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

    # Choose 1996 as the year of birth
    
    scrollToYear = web.find_element_by_xpath('//*[@id="id_dob_root"]/div/div/div/div/div[1]/div[1]/div/div/div/ul/li[26]')
    time.sleep(2)
    scrollToYear.location_once_scrolled_into_view
    scrollToYear.click()

    # Confirm DOB
    confirmDOB = web.find_element_by_xpath('//*[@id="id_dob_root"]/div/div/div/div/div[2]/button')
    confirmDOB.click()

    # Continue to SignUp
    continueToReg = web.find_element_by_xpath('//*[@id="sign-up-theme"]/section/div/div/div[1]/form/input[2]')
    continueToReg.click()

    # auto-fill every field
    userN = web.find_element_by_xpath('//*[@id="id_username"]')
    finalUser = userName + str(i)
    userN.send_keys(finalUser)

    # Password and confirm password
    passW = web.find_element_by_xpath('//*[@id="id_password"]')
    passW.send_keys(password)
    passW_cf = web.find_element_by_xpath('//*[@id="id_confirm_password"]')
    passW_cf.send_keys(password)

    # Email and confirm email
    email = web.find_element_by_xpath('//*[@id="id_email"]')
    email.send_keys(finalUser + mail)
    email = web.find_element_by_xpath('//*[@id="id_confirm_email"]')
    email.send_keys(finalUser + mail)

    # Accept the Pokemon.com Terms of Use.
    acceptTerm = web.find_element_by_xpath('//*[@id="id_terms"]')
    acceptTerm.click()


    i += 1
    f = open('index.txt','w')
    f.write(str(i))
    f.close()

    while (True):
        time.sleep(10)
        try:
            Finish = web.find_element_by_css_selector('#sign-up-theme > section > div > div > div.form-wrapper.color-block.color-block-lightgray.dog-ear-tl.match > h3')
            web.quit()
            break
        except:
            continue
    t -= 1

f = open('Info.txt', 'w')
f.write(userName + index + ':' + password + ':' + userName + index + mail + '\n')
f.close()