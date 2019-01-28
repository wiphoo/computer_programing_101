#!/usr/bin/env python3
import math
import sys

isDone = False
x = int( input() )
for a in range( 1, x ):
	for b in range( 1, x ):
#		print( 'a = {}, b = {}'.format( a, b ) )
		
		c = math.sqrt( a*a + b*b )
		if abs( round( c ) - c ) > 1e-12:
			continue
#		print( 'c = {}'.format( c ) )
		
		if a + b + int( c ) == x:
			#	done
			print( int( c ) )
			isDone = True
			break
	
	if isDone:
		break

