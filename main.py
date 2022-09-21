from funcs.genEngTxt import genEngTxt
from funcs.mergeRusDict import mergeRusDict
from funcs.simple import *
from funcs.genEngTxt import *
from funcs.genEngDicts import *
from funcs.createRusDict import *
from funcs.genRuDict import *
from funcs.mergeRusDict import *

clearFolder("./__temp__")
clearFolder("./__output__")
engDict = genEngTxt()
genEngDicts(engDict)
createRusDict()
input("Для продолжения, необходимо добавить русский текст в файл rus_1 \nпо завершению, нажи ENTER ")
rusDict = genRuDict()
mergeRusDict(rusDict, engDict)