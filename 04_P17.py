#!/usr/bin/env python3

s = input()

removeCToAppearDict = {}
output = ''
for c in s:
	
	numC = s.count( c )
	if numC == 1:
		output += c
	else:
	#	store as a remove char
		if c not in removeCToAppearDict.keys():
		#	store this char
			removeCToAppearDict[c] = 0
		elif removeCToAppearDict[c] == 1:
		#	add to output
			output += c
		
		#	count
		removeCToAppearDict[c] += 1

print( '{}'.format( output ) )
