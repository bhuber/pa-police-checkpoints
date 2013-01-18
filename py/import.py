#!/usr/bin/python

import csv

filename = '2012_01_15_PaTrafficStops.csv'

def ReadCsv(name):
    header = None
    rows = []
    with open(name, 'rb') as file:
        r = csv.reader(file)
        header = next(r)
        for row in r:
            rows.append(row)

    return (header, rows)



