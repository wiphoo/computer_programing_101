#!/usr/bin/env python3

numRows = int( input() )
numColumns = int( input() )

rowList = []
matchRowIndexTuple = None
for rowIndex in range( numRows ):
	thisRow = input()

	#	check for matching
	for existingRowIndex, existingRowVal in enumerate( rowList ):
#		print( 'thisRow = {}'.format( thisRow ) )
#		print( 'existingRowVal = {}'.format( existingRowVal ) )
		#	found
		if thisRow == existingRowVal:
			matchRowIndexTuple = ( existingRowIndex, rowIndex )
	
	rowList.append( thisRow )

print( matchRowIndexTuple[0]+1 )
print( rowList[matchRowIndexTuple[0]] )
print( matchRowIndexTuple[1]+1 )
print( rowList[matchRowIndexTuple[1]] )
