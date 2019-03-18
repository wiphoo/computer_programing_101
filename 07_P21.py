#!/usr/bin/env python

inputDueDate = int( input() )

bookIdMemberIdDueDateList = [ lineStr.split() 
								for lineStr in open( 'circulations.txt', 'r' ).readlines() ] 

#print( 'bookIdMemberIdDueDateList = {}'.format( bookIdMemberIdDueDateList ) )

overDueList = []
for bookId, memberId, dueDate in bookIdMemberIdDueDateList:
	
	if inputDueDate >= int( dueDate ): 
	#	store
		overDueList.append( ( bookId, memberId, dueDate ) )
	
#print( '   overDueList = {}'.format( overDueList ) )
overDueList.sort( key=lambda x: x[2] )
if len( overDueList ) == 0:
	print( 'Not Found' )
else:
	print( '\n'.join( '{} {} {}'.format( bookId, memberId, dueDate ) 
				for bookId, memberId, dueDate in  overDueList ) )
