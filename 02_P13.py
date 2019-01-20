#!/usr/bin/env python3

import datetime
import math

startHours, startMins = int( input() ), int( input() )
endHours, endMins = int( input() ), int( input() )

startTime = datetime.timedelta( hours = startHours,
								minutes = startMins )

endTime = datetime.timedelta( hours = endHours,
								minutes = endMins )
								
delta = endTime - startTime
total_mins = delta.total_seconds() / 60.
print( '   total_mins = {}'.format( total_mins ) )

total_pay = 0
if total_mins <= 15:
	print( 0 )
elif total_mins <= 180:
	print( math.ceil( total_mins / 60. ) * 10 )
elif total_mins <= 360:
	print( 30 + math.ceil( ( total_mins - 180. ) / 60. ) * 20 )
else:
	print( 200 )
