#!/usr/bin/env python3

inputList = input()
abcList = sorted( [ int( x ) for x in inputList.split() ] )
print( 'abcList = {}'.format( abcList ) )

print( 'YES' if abcList[0] + abcList[1] > abcList[2] else 'NO' )
