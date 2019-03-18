#!/usr/bin/env python3

inputList = []
inputValToCountDict = {}
while( True ):
	inputVal = int( input() )
	if( inputVal == -1 ):
		break
	
	inputList.append( inputVal )
	
	count = inputValToCountDict.get( inputVal, 0 )
	inputValToCountDict[inputVal] = count + 1

sortedInputValToCountList = sorted( inputValToCountDict.items(), key=lambda kv: kv[1], reverse=True )
	
print( 'sortedInputValToCountList = {}'.format( sortedInputValToCountList ) )
if sortedInputValToCountList[0][1] > ( len( inputList ) / 2. ):
	print( sortedInputValToCountList[0][0] )

else:
	print( 'Not found' )
