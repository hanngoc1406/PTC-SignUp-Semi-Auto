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
    web = webdriver.Chrome()
    web.get('https://club.pokemon.com/us/pokemon-trainer-club/sign-up/')
    time.sleep(2)

    # Accept Cookies
    acp = web.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]')
    acp.click()

    # Set DOB
    dob = web.find_element_by_xpath('//*[@id="sign-up-theme"]/section/div/div/div[1]/form/div[1]/input[2]')
    web.execute_script("arguments[0].value='1996-01-10';", dob)

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

    info = open('Info.txt', 'w')
    info.write(userName + index + ':' + password + ':' + userName + index + mail + '\n')
    info.close()

    while (True):
        time.sleep(10)
        try:
            Finish = web.find_element_by_css_selector('#sign-up-theme > section > div > div > div.form-wrapper.color-block.color-block-lightgray.dog-ear-tl.match > h3')
            web.quit()
            break
        except:
            continue
    t -= 1

