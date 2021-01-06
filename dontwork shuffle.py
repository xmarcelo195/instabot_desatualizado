import random, os, shutil

plan = ['1_segunda', '2_terca', '3_quarta', '4_quinta', '5_sexta', '6_sabado', '7_domingo']
source = '/home/marcelo/PycharmProjects/Data/instabot/Posts/_receitasdoces_/'
dest = '/home/marcelo/PycharmProjects/Data/instabot/Posts/planejamento/'



for dia in plan:
    list = os.listdir('/home/marcelo/PycharmProjects/Data/instabot/Posts/planejamento/{}'.format(dia))
    for valor in list:
        shutil.move(dest + dia + '/' + valor, source)

