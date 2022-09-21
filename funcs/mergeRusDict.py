import os

def mergeRusDict(rusDict, engDict):
    filename = os.listdir("./__fixtures__/")[0]
    with open(f"./__fixtures__/{filename}", encoding="utf-8") as orig, open(f"./__output__/{filename}", "w+", encoding="utf-8") as merged:
        lines = orig.readlines()
        count = 0
        for line in lines:
            if count != len(engDict):
                if line.find(engDict[count]) != -1:
                    line = line.replace(engDict[count], rusDict[count])
                    count += 1
            merged.write(line)