#!/usr/bin/env python3

input1 = input()
input2 = input()

isAnagram = True
for c1 in input1:
	
	if c1.isalpha():
		numC1 = input1.lower().count( c1.lower() )
		numC1inInput2 = input2.lower().count( c1.lower() )
		
		if numC1 != numC1inInput2:
			isAnagram = False

if isAnagram:
	print( '{}'.format( input1 ) )
else:
	print( '{} {}'.format( input1, input2 ) )
	
	
	
