


def genEngDicts(lines):
    arrs = []
    count = 0
    buff = 0
    for line in lines:
        if buff == 0:
            arrs.append([])
        if buff + len(line) >= 9500:
            count += 1
            buff = 1
            arrs.append([])
        arrs[count].append(line)
        buff += len(line)
    count = 1
    for arr in arrs:
        with open(f"./__temp__/eng_{count}.txt", "w+", encoding="utf-8") as engDict:
            for line in arr:
                engDict.write(line + "\n")
        count += 1