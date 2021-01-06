from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
browser = webdriver.Firefox()
browser.get('https://www.instagram.com/accounts/login/?next=/gordice.gourmet/')

#login
sleep(4)
path_login = '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input'
path_senha = '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input'
path_submit = '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button'
login = browser.find_element_by_xpath(path_login)
senha = browser.find_element_by_xpath(path_senha)

login.send_keys("gordice.gourmet")
senha.send_keys("")

browser.find_element_by_xpath(path_submit).click()

sleep(5)

#
''' path follow
/html/body/div[4]/div/div[2]/ul/div/li[212]/div/div[2]/button
/html/body/div[4]/div/div[2]/ul/div/li[2]/div/div[2]/button
/html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[3]/button
'''
path_following = '/html/body/div[1]/section/main/div/header/section/ul/li[3]/a'
rep = browser.find_element_by_xpath(path_following).text
rep = rep.replace(' following', '')
rep = int(rep)
browser.find_element_by_xpath(path_following).click()

i = 1
sleep(2)
popup = browser.find_element_by_class_name('isgrP')

while i < rep:
    try:
        status = browser.find_element_by_xpath(
        '/html/body/div[4]/div/div[2]/ul/div/li[{}]/div/div[3]/button'.format(i)).text
        if status == 'Following':
            sleep((randint(100, 500))/100)
            browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li[{}]/div/div[3]/button'.format(i)).click()
            sleep((randint(100, 500)) / 100)
            browser.find_element_by_class_name('aOOlW.-Cab_').click()
            sleep((randint(100, 500)) / 100)
            popup.send_keys(Keys.ARROW_DOWN)
            sleep((randint(100, 500)) / 100)

    except:
        try:
            popup.send_keys(Keys.ARROW_UP)
            if status == 'Following':
                sleep((randint(100, 500)) / 100)
                browser.find_element_by_xpath(
                    '/html/body/div[4]/div/div[2]/ul/div/li[{}]/div/div[3]/button'.format(i)).click()
                sleep((randint(100, 500)) / 100)
                browser.find_element_by_class_name('aOOlW.-Cab_').click()
                sleep((randint(100, 500)) / 100)
                popup.send_keys(Keys.ARROW_DOWN)
                sleep((randint(100, 500)) / 100)
        except:
            browser.get('https://www.instagram.com/gordice.gourmet/')
            sleep(3.5)
            rep = browser.find_element_by_xpath(path_following).text
            rep = rep.replace(' following', '')
            rep = int(rep)
            browser.find_element_by_xpath(path_following).click()
            sleep((randint(100, 500)) / 100)
            i = 0
            popup = browser.find_element_by_class_name('isgrP')
    i = i + 1


