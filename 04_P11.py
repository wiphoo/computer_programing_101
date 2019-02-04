#!/usr/bin/env python3

s = input()

num1Bits = s.count( '1' )

if num1Bits % 2 == 0:
	print( '{}{}'.format( s, 0 ) )
else:
	print( '{}{}'.format( s, 1 ) )
