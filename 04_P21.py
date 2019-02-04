#!/usr/bin/env python3

n = int( input() )
inputList = []
for i in range( n ):
	inputList.append( input() )
	
minLenght = min( [ len( x ) for x in inputList ] )


isPrefixDone = False
isSuffixDone = False
prefix = ''
suffix = ''
for i in range( minLenght ):
	
	prefixS = inputList[0][i]
	suffixS = inputList[0][len(inputList[0])-i-1]
#	print( 'prefixS = {}'.format( prefixS ) )
#	print( 'suffixS = {}'.format( suffixS ) )
	
	samePrefix = True
	sameSuffix = True
	for inputIndex in range( 1, n ):
		
		thisInputPrefix = inputList[inputIndex][i]
		thisInputSuffix = inputList[inputIndex][len(inputList[inputIndex])-i-1]
		
#		print( '  input index {}'.format( inputIndex ) )
#		print( '     thisInputPrefix = {}'.format( thisInputPrefix ) )
#		print( '     thisInputSuffix = {}'.format( thisInputSuffix ) )
				
		if prefixS != thisInputPrefix:
			samePrefix = False
		if suffixS != thisInputSuffix:
			sameSuffix = False
	
#	print( '   samePrefix = {}'.format( samePrefix ) )
#	print( '   sameSuffix = {}'.format( sameSuffix ) )
		
	#	check same prefix or suffix
	if samePrefix and not isPrefixDone:
		prefix += prefixS
	else:
		isPrefixDone = True
	
	if sameSuffix and not isSuffixDone:
		suffix += suffixS
	else:
		isSuffixDone = True
	
#	print( '{}'.format( prefix ) )
#	print( '{}'.format( suffix ) )	

print( '{}'.format( prefix if len( prefix ) != 0 else 'NO COMMON PREFIX' ) )
print( '{}'.format( suffix[::-1] if len( suffix ) != 0 else 'NO COMMON SUFFIX' ) )	
