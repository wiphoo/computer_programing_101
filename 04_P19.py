#!/usr/bin/env python3

inputStr = input()
map1Str = input()
map2Str = input()

outputStr = ''
for i in inputStr:
	
	match = False
	for mapCharIndex, mapChar in enumerate( map1Str ):
		if i == mapChar:
			outputStr += map2Str[mapCharIndex]
			match = True
			break
			
	for mapCharIndex, mapChar in enumerate( map2Str ):
		if i == mapChar:
			outputStr += map1Str[mapCharIndex]
			match = True
			break
			
	if not match:
		outputStr += i

print( '{}'.format( outputStr ) )
	
		 
