#!/usr/bin/python3

regs = {}
maxVals = []
fd = open( 'input.txt', 'r' )
while 1 == 1:

    readLine = fd.readline()
    if readLine == '':
        break
    sides = readLine.split("if")

    ifSide = sides[1].strip()
    actionSide = sides[0].strip()

    ifSide = ifSide.split(" ")
    reg = ifSide[0] 
    operator = ifSide[1]
    condition = int(ifSide[2])

    actionSide = actionSide.split(" ")
    actionReg = actionSide[0]
    action = actionSide[1]
    actionVal = int(actionSide[2])


    if reg in regs:
        val = regs[reg]
    else:
        val = 0


    takeAction = 0
    if operator == "==":
        if val == condition:
            takeAction=1
    if operator == "!=":
        if val != condition:
            takeAction=1
    if operator == "<":
        if val < condition:
            takeAction=1
    if operator == "<=":
        if val <= condition:
            takeAction=1
    if operator == ">":
        if val > condition:
            takeAction=1
    if operator == ">=":
        if val >= condition:
            takeAction=1
    if takeAction == 1:
        if action == "dec":
            if actionReg in regs:
                regs[actionReg] -= actionVal
            else:
                regs[actionReg] = - actionVal
        if action == "inc":
            if actionReg in regs:
                regs[actionReg] += actionVal
            else:
                regs[actionReg] = actionVal
    maxVals.append(max(regs.values()))
print("All time highest:",max(maxVals))
print("In the end highest:",max(regs.values()))

