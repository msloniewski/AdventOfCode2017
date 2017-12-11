#!/usr/bin/python3

def weight( name ):
    ret = vals[name]
    for el in tree[name]:
        ret += weight( el )
    return ret
def weight_without( name ):
    ret = 0
    for el in tree[name]:
        ret += weight( el )
    return ret

vals = {}
tree = {}
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
        tree[name] =leaves[:]
        readLine = fd.readline()
#print (tree)

for element in tree:
    found = ''
    if len(tree[element]) == 0:
        found = element
        break
flag = 1
while flag == 1:
    flag = 0
    for el in tree:
        if found in tree[el]:
            flag = 1
            found = el
print (found)

flag = 1
shouldBe = 0
while flag == 1:
    if len(tree[found]) == 0:
        break
    i = 0
    diffVal = weight(tree[found][0])
    diffVal2=0
    for el in tree[found]:
        if weight(el) !=  diffVal:
            diffVal2 = weight(el)
            break
        print (weight(el),"asd")
        i+=1
        #print (weight(el])
    if i == len (tree[found]):
        break
    print (tree[found])
    print (i)
    print (diffVal, diffVal2)
    if i == 1:
        print (weight(tree[found][2]), diffVal2)
        if weight(tree[found][2]) != diffVal2:
            shouldBe = diffVal
            found = tree[found][i]
        else:
            shouldBe=diffVal2
            found = tree[found][0]
    else:
        if weight(tree[found][1]) != diffVal2:
            shouldBe = diffVal
            found = tree[found][i]
        else:
            shouldBe=diffVal2
            found = tree[found][0]

    print ("sh be ",shouldBe)


print(shouldBe - weight_without(found) )
   
