#!/usr/bin/env python3

xList = [ int( x ) for x in input().split() ]

xList = sorted( xList )

medianIndex = len( xList ) // 2
if len( xList ) % 2 == 0:
	print( ( xList[medianIndex-1] + xList[medianIndex] ) / 2. )
else:
	print( float( xList[ medianIndex ] ) )
