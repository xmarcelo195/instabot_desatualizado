import random, os, shutil

plan = ['1_segunda', '2_terca', '3_quarta', '4_quinta', '5_sexta', '6_sabado', '7_domingo']
source = r'D:\Linux\pycharm\data\instabot\Posts\receitasdoces_deliciosas'
dest = r'D:\Linux\pycharm\data\instabot\Posts\planejamento'


for dia in plan:
    lista = os.listdir(source)
    res = random.sample(range(1, len(lista)), 10)
    for valor in res:
        os.rename(source + '\\' + lista[(valor-1)], dest + '\\' + dia + '\\' + "{}.txt".format(res.index(valor)))

