#!/usr/bin/env python3

numInputs = int( input() )

inputList = []
for i in range( numInputs ):
	inputList.append( int( input() ) )

inputList.sort()

print( '\n'.join( [ str( i ) for i in inputList ] ) ) 
