#!/usr/bin/env python3
from calendar import monthrange

year = int( input() )
( startDay, endDay ) = monthrange( year-543, 2 )
print( endDay )
