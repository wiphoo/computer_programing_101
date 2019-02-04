#!/usr/bin/env python3

s = input()

print( '{}'.format( 'yes' if s.lower().replace( ' ', '' ) == s.lower().replace( ' ', '' )[::-1] else 'no') )
