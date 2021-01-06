def likar():
    with open('likar.txt', 'r', encoding="utf8") as f:
        data = f.readlines()
        data = list(data)
    likar = []
    for name in data:
        likar.append(name[0:-1])
    return likar