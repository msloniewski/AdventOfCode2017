#!/usr/bin/python3
checksum = 0

with open( 'input.txt', 'r' ) as fd:
    readLine = fd.readline()
    while ( readLine != ''):
        data = []
        for element in readLine.split('\t'):
            data.append(  int( element ) )
        print( data )
        for element in data:
            for element2 in data:
                if element > element2:
                    if ( element % element2) == 0:
                        print (element , element2)
                        checksum += element / element2
        readLine = fd.readline()
print ( checksum )

