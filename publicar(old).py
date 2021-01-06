from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.firefox.options import Options
import os

#Código para publicar pelo creator studio - Não funciona
# TODOS OS XPATH ESTAO ERRADOS PORQ INSTAGRAM FICA MUDANDO
# LER https://developers.facebook.com/docs/instagram-api/guides/content-publishing/#publish-photos


browser = webdriver.Firefox()
site = 'https://www.facebook.com/login/?next=%2Fcreatorstudio%2F%3Freference%3Dvisit_from_seo'
browser.get(site)

sleep(3)
#paths login
id_new_post = 'js_r'
id_login = 'email'
id_pass = 'pass'
id_button = 'loginbutton'

#login
login = browser.find_element_by_id(id_login)
senha = browser.find_element_by_id(id_pass)

login.send_keys("")
senha.send_keys("")

browser.find_element_by_id(id_button).click()
sleep(3)

#ir para a controle do face
site_insta = 'https://business.facebook.com/creatorstudio/?tab=instagram_content_posts&mode=instagram&collection_id=all_pages&content_table=INSTAGRAM_POSTS'
browser.get(site_insta)
sleep(4)

#clicar criar novo post
class_new = '_271k._271l._271m._1qjd._1gwm'
browser.find_element_by_class_name(class_new).click()
sleep(4)

#clicar no botão de feed do insta
path_feed = '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/div/ul/li[1]'
browser.find_element_by_xpath(path_feed).click()
sleep(7)

# hashtags
hashtags = '#receitas #bolo #torta #gordice #gordices #food #chocolate #doce #doces #gourmet'

#adicionar texto
class_text = 'notranslate._5rpu'
with open('/home/marcelo/PycharmProjects/Data/instabot/Posts/planejamento/4_quinta/file032.txt') as f:
    text = f.readlines()
    text.append('\n')
    text.append(hashtags)
browser.find_element_by_class_name(class_text).send_keys(text)


#descer para adicionar foto
class_body = '_7-i-'
browser.find_element_by_class_name(class_body).send_keys(Keys.END)
sleep(1)

#botão que abre o popup
class_add_p = '_3-99'
browser.find_element_by_class_name(class_add_p).click()
sleep(2)

#input photo
class_input_photo = '_n._5f0v'
photo_test = '/home/marcelo/PycharmProjects/Data/instabot/Posts/planejamento/4_quinta/File032.jpg'
browser.find_element_by_class_name(class_input_photo).send_keys(photo_test)
sleep(4)

#botão triangulo para agendar
class_triagle_button = '_271k._271l._1o4e._271m._1qjd'
browser.find_element_by_class_name(class_triagle_button).click()
sleep(2)

#clicar em agendar
class_agendar = '_kx6._kxa._811d'
browser.find_element_by_class_name(class_agendar).click()
sleep(2)

#data e hora
path_data = '/html/body/div[7]/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/span/div/span/label/input'
browser.find_element_by_xpath(path_data).click()
browser.find_element_by_xpath(path_data).send_keys('02/20/2020')
sleep(1)

#clicar hora
class_click_h = '_4nx3._1jh3'
browser.find_element_by_class_name(class_click_h).click()
hora = 2
browser.find_element_by_xpath('//*[@id="js_u8"]').send_keys(hora)

#clicar minuto
path_click_m = '/html/body/div[11]/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/label'
browser.find_element_by_xpath(path_click_m).click()
minuto = 00
browser.find_element_by_id('js_335').send_keys(minuto)

#Am pm
path_click_ap = '/html/body/div[11]/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[3]/div/label'
browser.find_element_by_xpath(path_click_ap).click()
turno = 'pm'
browser.find_element_by_id('js_337').send_keys('p')

#botão agendar
class_botao_agendar = '_271k._271m._1qjd'
browser.find_element_by_class_name(class_botao_agendar).click()

