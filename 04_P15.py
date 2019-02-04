#!/usr/bin/env python3

s = input()

preC = s[0]
numContiguousChars = 1
maxNumContiguousChars = 1

for c in s[1:]:
	
	if c.lower() == preC.lower():
	#	increae count
		numContiguousChars += 1
	
	else:
	# 	found new char
		if maxNumContiguousChars < numContiguousChars:
		#	found new max contiguous
			maxNumContiguousChars = numContiguousChars
		
		#	new char
		preC = c
		numContiguousChars = 1

if maxNumContiguousChars < numContiguousChars:
	#	found new max contiguous
	maxNumContiguousChars = numContiguousChars
			
print( '{}'.format( maxNumContiguousChars ) )
