#!/usr/bin/env python3

idAndScoreList = [ lineStr.split() for lineStr in open( 'score.txt', 'r' ).readlines() ]

idAndScoreList.sort( key=lambda x: x[0], reverse=True )
print( 'idAndScoreList = {}'.format( idAndScoreList ) )

print( '\n'.join( [ str( idAndScore[0] ) 
		for idAndScore in idAndScoreList ] ) )


