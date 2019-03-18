#!/usr/bin/env python3

idToScoreDict = {}
inputId = None
while( True ):
	idAndScore = input().split()
	if( len( idAndScore ) == 1 ):
		inputId = int( idAndScore[0] )
		break
	
	idToScoreDict[int(idAndScore[0])] = float( idAndScore[1] )
	
sortedIdAndScoreList = sorted( idToScoreDict.items(), 
								key=lambda kv: (kv[1], -kv[0]), 
								reverse=True )
sortedIdList = [ id for id, score in sortedIdAndScoreList ]
#print( ' sortedIdList = {}'.format( sortedIdList ) )	
if inputId in idToScoreDict:
	print( sortedIdList.index( inputId ) + 1 )

else:
	print( 'Not Found' )
