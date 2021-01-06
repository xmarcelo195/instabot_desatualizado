from selenium import webdriver
import os
import urllib.request
from time import sleep

plan = ['1_segunda', '2_terca', '3_quarta', '4_quinta', '5_sexta', '6_sabado', '7_domingo']
path = "D:\\Linux\\pycharm\\data\\instabot\\Posts\\planejamento\\"

tabs = []

dia = int(input('Dia = '))
list = os.listdir(path + plan[dia-1])
list.sort()
print(list)
for file in list:
    with open(r'D:\Linux\pycharm\data\instabot\Posts\planejamento\{}\{}'.format(plan[dia-1], file), 'r', encoding="utf8") as f:
        data = f.read()
        a = data.index('\n')
        new = data[7:(a)]
        tabs.append(new)

for site in tabs:
    print(site)

browser = webdriver.Firefox()
i = 2
for site in tabs:
    browser.get(site)
    sleep(1)
    urllib.request.urlretrieve(site, path + plan[dia-1]+ '\\' + "{}.jpg".format((tabs.index(site))+0))
