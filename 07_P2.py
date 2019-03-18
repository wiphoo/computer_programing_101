#!/usr/bin/env python3

x = input()

resultDict = { '0':0, '1':0, '2':0, '3':0, '4':0,
				'5':0, '6':0, '7':0, '8':0, '9':0 }
for i in x:
	resultDict[i] += 1
	
print( '\n'.join( [ str( val ) 
					for key, val in resultDict.items() ] ) )
