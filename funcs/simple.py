import os

def clearFolder(path):
    files = os.listdir(path)
    for file in files:
        os.remove(path + "/" + file)

def isTitle(line):
    return line.find('title:') != -1
def isSubTitle(line):
    return line.find('subtitle:') != -1
def isSingleDesc(line):
    return line.find('description: [') != -1 and line.find(']') != -1
def isMultiDescStart(line):
    return line.find('description: [') != -1 and line.find(']') == -1
def isMultiDescEnd(line):
    return line.find(']') != -1
def isMultiDesc(line):
    return line.find('""') == -1

def textFromLine(line):
    return line[line.find('"') + 1:line.rfind('"')]