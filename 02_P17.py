#!/usr/bin/env python3

n = int(input()) 
if n < 0 or n > 80 : 
	print("Error : Out of range") 
else: 
	out = "" 
	reminder = n % 3
	out = '{}'.format( reminder ) + out
	n //= 3
	
	reminder = n % 3
	out = '{}'.format( reminder ) + out
	n //= 3
	
	reminder = n % 3
	out = '{}'.format( reminder ) + out
	n //= 3
	
	reminder = n % 3
	out = '{}'.format( reminder ) + out

	print(out) 
	
