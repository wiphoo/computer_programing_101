#!/usr/bin/env python3

vowels = 'aeiou'

s = input()

numGroups = 0
consecutive = False
for c in s:

	isVowel = False
	for vowel in vowels:
		if c.count( vowel ) > 0:
			isVowel = True
			break
	
#	print( '{} is vowel = {}'.format( c, isVowel ) )
	
	if isVowel:			
		if not consecutive:
		#	new group found
			consecutive = True
			numGroups += 1
		else:
		#	same group
			pass
			
	else:
	#	done this group
		consecutive = False

		
print( '{}'.format( numGroups ) )
