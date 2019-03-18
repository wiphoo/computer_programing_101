#!/usr/bin/env python3

from itertools import groupby

numInputs = int( input() )

inputList = []
for i in range( numInputs ):
	inputList.append( int( input() ) )

inputList.sort()
inputToNumDuplicatedList = [ (key, len(list(group))) for key, group in groupby( inputList )]
inputToNumDuplicatedList.sort( key=lambda x: x[1], reverse=True )
#print( 'inputToNumDuplicatedList = {}'.format( inputToNumDuplicatedList ) )
print( '{} {} {}'.format( sum( inputList ) / float( numInputs ),
							inputList[ numInputs // 2 ] if numInputs % 2 != 0
										else ( inputList[ numInputs // 2 - 1 ] 
												+ inputList[ numInputs // 2 ] ) / 2.,
							inputToNumDuplicatedList[0][0] ) )
