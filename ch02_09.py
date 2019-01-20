#!/usr/bin/python3

eq1 = input()
eq2 = input()

print( 'eq1 = {}' )
a1, b1, c1 = [ float( x ) for x in eq1.split() ]
print( '   a1 = {}, b1 = {}, c1 = {}'.format( a1, b1, c1 ) )
a2, b2, c2 = [ float( x ) for x in eq2.split() ]
print( '   a2 = {}, b2 = {}, c2 = {}'.format( a2, b2, c2 ) )

#	helper functions
def gcd( a, b ):
	''' return a greatest common divisor between a and b
			if a is zero, then gcd( a, b ) is b
			if b is zero, then gcd( a, b ) is a
			a = b * q + r
			gcd( a, b ) = gcd( b, r )
	'''
	print( 'calling gcd( {}, {} )'.format( a, b ) )
	
	#	check a and b are zero or not?
	if a == 0:
	#	the gcd is b
		return b
	if b == 0:
	#	the gcd is a
		return a
	
	#	using long division to find a/b = q and a%b = r
	q = a // b
	r = a % b
	print( ' q = {}, r = {}'.format( q, r ) )
	assert( a == ( b * q ) + r )
	
	#	recursive call gcd of b and r
	return gcd( b, r )

#	number of solutions
#		1. same slope not solution
#		2. difference slope one solution
#		3. same equation multiple slopes

#	check for the same equation
#		find GCD of all coefficient
#	gcd( a, b, c ) = gcd( a, gcd( b, c ) )
gcdA1B1C1 = gcd( a1, gcd( b1, c1 ) )
gcdA2B2C2 = gcd( a2, gcd( b2, c2 ) )
print( 'gcdA1B1C1 = {}'.format( gcdA1B1C1 ) )
print( 'gcdA2B2C2 = {}'.format( gcdA2B2C2 ) )

