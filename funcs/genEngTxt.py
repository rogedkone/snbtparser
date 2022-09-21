import os
from funcs.simple import *

def genEngTxt():
    arr = []
    snbtin = "./__fixtures__/" + os.listdir("./__fixtures__")[0]
    with open(snbtin, encoding="utf-8") as snbt:
        lines = snbt.readlines()
        inDesc = False
        for line in lines:
            if isTitle(line) or isSubTitle(line) or isSingleDesc(line):
                arr.append(textFromLine(line))
            elif isMultiDescStart(line):
                inDesc = True
            elif inDesc:
                if isMultiDescEnd(line):
                    inDesc = False
                if inDesc and isMultiDesc(line):
                    arr.append(textFromLine(line))
    return arr