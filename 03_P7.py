#!/usr/bin/env python3

def factorial( x ):
	if x == 0:
		return 1
	result = x
	for i in range( x-1, 0, -1 ):
		result *= i
	return result

def f( k, x ):
#	print( 'f( k = {}, x = {} )'.format( k, x ) )
	numerator = ((-1)**k)*(x**(2*k))
	denominator = factorial(2*k)
#	print( 'numerator = {}, denominator = {}'.format( 
#						numerator, denominator ) )
	return numerator / denominator
	

x = float( input() )

k = 0
result = 0
while True:
	
	thisVal = f( k, x )
#	print( 'k = {}, thisVal = {}'.format( k, thisVal ) )
	if abs( thisVal ) < 1e-8:
	#	done
		break
	
	result += thisVal
	k += 1
	
#	print( 'result = {}'.format( result ) )
	
	
print( result, k-1 )
	
	
