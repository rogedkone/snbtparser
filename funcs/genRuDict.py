def genRuDict():
    arr = []
    with open("./__temp__/rus.txt", encoding="utf-8") as ruDict:
        lines = ruDict.readlines()
        for line in lines:
            arr.append(line.replace('\n', ''))
    return arr