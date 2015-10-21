#!/usr/bin/env python

import csv
import sys
import operator
from   helpers import split_row, map_house

HOUSES = {}

source = open(sys.argv[1], 'rU')
target = open(sys.argv[2], 'wt')
header = open('headers.csv', 'rU')

# read file
try:
    reader = csv.reader(source)
    sorted_list = sorted(reader, key=operator.itemgetter(1))

    for row in sorted_list:
        name = row[1]
        if name == 'Last Name':
            continue

        if name not in HOUSES:
            HOUSES[row[1]] = { 'rows' : [split_row(row)]}
        else:
            # if house numbers don't match
            while name in HOUSES and row[4].split(' ')[0] != HOUSES[name]['rows'][0][4].split(' ')[0]:
                name += ' '
            else:
                # new house
                if name not in HOUSES:
                    HOUSES[name] = { 'rows' : [split_row(row)]}
                # found matching address
                else:
                    HOUSES[name]['rows'].append(split_row(row))

finally:
    source.close()


# write file
try:
    writer = csv.writer(target)
    reader = csv.reader(header)
    
    writer.writerow(next(reader))

    for house in HOUSES:
        writer.writerow(map_house(house, HOUSES[house]))
finally:
    target.close()
