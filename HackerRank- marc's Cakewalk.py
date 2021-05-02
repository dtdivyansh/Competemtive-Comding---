def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    c = 0
    for i in range(len(calorie)):
        c = c + math.pow(2,i)*calorie[i]
    return int(c)
