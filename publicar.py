from instabot import Bot
from time import sleep
import os
import datetime

bot = Bot()

bot.login(username="gordice.gourmet", password="")

plan = ['1_segunda', '2_terca', '3_quarta', '4_quinta', '5_sexta', '6_sabado', '7_domingo']
path = "D:\\Linux\\pycharm\\data\\instabot\\Posts\\planejamento\\"

sleep(5)
dia = int(input('Dia = '))
lista = os.listdir(path + plan[dia-1])
qt_post = int(len(lista)/2)

d = datetime.datetime.now().day
mes = datetime.datetime.now().month

# FAZER = baixar e usar o schedule pra rodar o bot a cada 1hr
                                # ano, mes ,d ,hr ,min,seg, milsg
horarios_pub = [#datetime.datetime(2020, mes, d, 12, 0, 0, 0), #0
                #datetime.datetime(2020, mes, d, 13, 0, 0, 0), #1
                datetime.datetime(2020, mes, d, 14, 0, 0, 0), #2
                datetime.datetime(2020, mes, d, 15, 0, 0, 0), #3
                datetime.datetime(2020, mes, d, 16, 0, 0, 0), #4
                datetime.datetime(2020, mes, d, 17, 0, 0, 0), #5
                datetime.datetime(2020, mes, d, 18, 0, 0, 0), #6
                datetime.datetime(2020, mes, d, 19, 0, 0, 0), #7
                datetime.datetime(2020, mes, d, 20, 0, 0, 0), #8
                datetime.datetime(2020, mes, d, 21, 0, 0, 0)] #9

hashtags = '\n#receitas #bolo #torta #gordice #gordices #food #chocolate #doce #doces #gourmet #receita #sobremesa #cozinhar #cozinheira #cozinheiro'

i = 0
for item in lista:
    if item[-3:] == 'txt':
        i = int(item[0])
        print(item)
        with open(r"D:\Linux\pycharm\data\instabot\Posts\planejamento\{}\{}.txt".format(plan[dia - 1], i), "r",
                  encoding="utf8") as f:
            text = f.read()

        text = text.split('\n', maxsplit=1)
        text = text[1][9:]

        while horarios_pub[i] > datetime.datetime.now():
            print('Esperando... agr :{}  prox: {}'.format(datetime.datetime.now(), horarios_pub[i]))
            sleep(300)

        bot.upload_photo(r"D:\Linux\pycharm\data\instabot\Posts\planejamento\{}\{}.jpg".format(plan[dia-1], i),
                         caption=(text+hashtags))

        i = i+1
    else:
        print(item[-3:], 'não é txt')


# bot.upload_photo(r"D:\Linux\pycharm\data\instabot\Posts\planejamento\1_segunda\1.jpg", caption=text)
# date1 = datetime.datetime.now().time()

