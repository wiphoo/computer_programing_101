#!/usr/bin/env python3

file = open("address.txt", "r")
addr = {}

for line in file:
	data = line.strip().split()
	addr[ ( data[0], data[1] ) ] = ( data[2], data[3] )
file.close()

while True :

	search = input().strip()
#	print( 'search = {}'.format( search ) )
	if search == "" :
		break
		
	name, surname = search.split()
	if (name, surname) in addr:
		phoneNumber, email = addr[( name, surname )]
		print( '{} {}'.format( phoneNumber, email ) )
	else:
		print("Not found")
