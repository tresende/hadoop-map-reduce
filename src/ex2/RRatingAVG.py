#!/usr/bin/env python
"""reducer.py"""

# reducer to read and process the data
 
import sys

# initialize and define the variables
current_rating = 0
current_name = ''
name = ''
current_count = 1
rating = 0

# input comes from STDIN (standard input)
for line in sys.stdin:

# remove any spaces or blanks
    line = line.strip()
   
# read the rating and count delimited by tab
    rating, name = line.split(",")
    rating = float(rating)

# Check if the rating has changed in the sorted stream of data
    if current_name == name:
        current_rating += rating
        current_count += 1
        
    else:
        if current_rating:
            print "{0:.2f}".format(round(current_rating/current_count,2)), current_name
        current_name = name
        current_rating = rating
        current_count = 1

# print the last rating count
if current_name == name:
     print "{0:.2f}".format(round(current_rating/current_count,2)), current_name
