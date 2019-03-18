#!/usr/bin/env python3
import sys

numInputs = int( input() )
if numInputs == 0:
	print( 0 )
	print( 0 )
	sys.exit( 0 )
	
inputList = []
for i in range( numInputs ):
	inputs = set( input().split() )
	print( 'inputs[{}] = {}'.format( i, inputs ) )
	inputList.append( inputs )

union = set( inputList[0] )
intersect = set( inputList[0] )	
for inputs in inputList[1:]:
	union = union.union( inputs )
	intersect = intersect.intersection( inputs )
	
print( len( union ) )
print( len( intersect ) )
