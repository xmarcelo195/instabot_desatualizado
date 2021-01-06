import random, os, shutil

plan = ['1_segunda', '2_terca', '3_quarta', '4_quinta', '5_sexta', '6_sabado', '7_domingo']
source = r"D:\Linux\pycharm\data\instabot\Posts\receitasdoces_deliciosas"
dest = r'D:\Linux\pycharm\data\instabot\Posts\planejamento'

list = os.listdir(source)

i = 1
for file in list:
    os.rename(source + '\\' + file, source + '\\' + 'post{}.txt'.format(i))
    i = i + 1
