#!/usr/bin/env python3
from calendar import monthrange

monthYear = input()
month, year = [ int(x) for x in monthYear.split() ]

( startDay, endDay ) = monthrange( year-543, month )
print( endDay )
