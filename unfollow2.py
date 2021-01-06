from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()

browser.get('https://www.instagram.com/accounts/login/')

sleep(3)
path_login = '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input'
path_senha = '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input'
path_submit = '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button'
path_unfollow = '/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button'
unfollow_class = '_5f5mN.-fzfL._6VtSN.yZn4P'
unfollow_confirmation_class = 'aOOlW.-Cab_'
login = browser.find_element_by_xpath(path_login)
senha = browser.find_element_by_xpath(path_senha)

login.send_keys("gordice.gourmet")
senha.send_keys("")

browser.find_element_by_xpath(path_submit).click()

sleep(5)
erros = []
list = []
with open('deseguir.txt') as fp:
    for line in fp:
        nome = line
        nome = nome.replace("\n", "")
        list.append(nome)

for usuario in list:
    try:
        browser.get('https://www.instagram.com/{}'.format(usuario))
        text = browser.find_element_by_class_name(unfollow_class).text
        if text == 'Following':
            browser.find_element_by_class_name(unfollow_class).click()
            sleep(1)
            browser.find_element_by_class_name(unfollow_confirmation_class).click()
        elif text == 'Follow':
            print('Não está seguindo {}'.format(usuario))
        else:
            print('algo errado não está certo')


    except:
        erros.append(usuario)

    print('unfollowing {} de {}'.format(list.index(usuario), len(list)))
    sleep(3)

print(erros)
