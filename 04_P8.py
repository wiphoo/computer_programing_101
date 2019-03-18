#!/usr/bin/env python3

string = input()
startIndex, endIndex = [ int( i ) for i in input().split() ]

#print( 'startIndex = {}'.format( startIndex ) )
#print( 'endIndex = {}'.format( endIndex ) )

numChars = len( string )
#print( '   string[:startIndex] = {}'.format( string[:startIndex] ) )
#print( '   string[::-1][numChars-endIndex-1:numChars-startIndex] = {}'.format( string[::-1][numChars-endIndex-1:numChars-startIndex] ) )
#print( '   string[endIndex:]  = {}'.format( string[endIndex:]  ) )

print( '{}{}{}'.format( string[:startIndex], 
						string[::-1][numChars-endIndex-1:numChars-startIndex],
						string[endIndex+1:] ) )
