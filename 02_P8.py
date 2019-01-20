#!/usr/bin/env python
import datetime


day = int( input() )
month = int( input() )
year = int( input() )

x = datetime.date( year - 543, month, day )
print( x.timetuple().tm_yday )
