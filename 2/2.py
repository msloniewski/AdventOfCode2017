#!/usr/bin/python3
checksum = 0

with open( 'input.txt', 'r' ) as fd:
    readLine = fd.readline()
    while ( readLine != ''):
        minimal = 99999
        maximal = 0
        for element in readLine.split('\t'):
            data = int( element )
            minimal = min( minimal, data )
            maximal = max( maximal, data )
        print( minimal , "  " , maximal)
        checksum += maximal - minimal
        readLine = fd.readline()
print( checksum )

