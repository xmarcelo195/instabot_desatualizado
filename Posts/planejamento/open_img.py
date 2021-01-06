from selenium import webdriver
import os, urllib

plan = ['1_segunda', '2_terca', '3_quarta', '4_quinta', '5_sexta', '6_sabado', '7_domingo']
path = '/home/marcelo/PycharmProjects/Data/instabot/Posts/planejamento/'

tabs = []

dia = int(input('Dia = '))
list = os.listdir(path + plan[dia-1])
list.sort()
print(list)
for file in list:
    with open('/home/marcelo/PycharmProjects/Data/instabot/Posts/planejamento/{}/{}'.format(plan[dia-1], file), 'r') as f:
        data = f.read()
        a = data.index('\n')
        new = data[7:(a)]
        tabs.append(new)

for site in tabs:
    print(site)

browser = webdriver.Firefox()
i = 2
for site in tabs:
    control_string = "window.open('{0}')".format(site)
    browser.execute_script(control_string)
