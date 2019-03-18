#!/usr/bin/env python3

inputFileName = input()

#	read input file 
with open( inputFileName, 'r' ) as inputFile:
	inputList = [ line.split() for line in inputFile.readlines() ]
	
#print('inputList = {}'.format( inputList ) )

fruitNameToPersonsListDict = {}
for fruitName, person in inputList:
	
	personList = fruitNameToPersonsListDict.get( fruitName, None )
	if personList == None:
		fruitNameToPersonsListDict[fruitName] = [ person ]
	else:
		fruitNameToPersonsListDict[fruitName].append( person )
		
		
maxFaveriteFruit = -1
maxFaveriteFruitName = None
outputStr = '['
for index, ( fruitName, personsList ) in enumerate( fruitNameToPersonsListDict.items() ):
	if maxFaveriteFruit < len( personsList ):
		maxFaveriteFruit = len( personsList )
		maxFaveriteFruitName = fruitName
	
	outputStr += '[\'{}\', {}]'.format( fruitName, personsList )
	if index < len( fruitNameToPersonsListDict ) - 1:
		outputStr += ', '
outputStr += ']'

print( ' fruitNameToPersonsListDict = {}'.format( fruitNameToPersonsListDict ) )
print( '{}'.format( outputStr ) )
print( 'The most favorite fruit is a {}'.format( maxFaveriteFruitName ) )
