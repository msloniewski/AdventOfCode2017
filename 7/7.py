#!/usr/bin/python3

vals = {}
tree = []
with open( 'input.txt', 'r' ) as fd:
    readLine = fd.readline()
    while (readLine != '') :
        splited = readLine.split('(')
        name = splited[0]
        name = name.strip()

        splited = splited[1].split(')')
        val = int(splited[0])
        vals[name] = val

        splited = splited[1].split("->") 
        leaves = []
        if (len(splited)>1):
            splited = splited[1].split(",")
            for element in splited:
                element = element.strip()
                leaves.append(element)
        tree.append([name, leaves[:]])
        readLine = fd.readline()
#print (tree)

for element in tree:
    found = ''
    if len(element[1]) == 0:
        found = element[0]
        break
flag = 1
while flag == 1:
    flag = 0
    for el in tree:
        if found in el[1]:
            flag = 1
            found = el[0]
print (found)
