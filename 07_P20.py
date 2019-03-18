#!/usr/bin/env python3

infile = open("hotels.txt", "r")
hotels = []
for line in infile:
	[hotel, stars, review] = line.split(";")
	hotels.append([hotel, int(stars), float(review)])
infile.close()
#print(hotels)
star = int(input())
found_hotels = []
for h in hotels:
	if h[1] >= star: 
		found_hotels.append(h)   

found_hotels.sort( key = lambda k: k[2], reverse=True )
if len(found_hotels) == 0:
	print("Not Found")
else:
	print( '\n'.join( '{} {} {}'.format( h[0], h[1], h[2] )
						for h in found_hotels ) )
