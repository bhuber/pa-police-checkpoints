#!/usr/bin/python

import pandas as pd
import numpy as np
import statsmodels
import tables
import scipy


def make_address(row):
    num = row['street_number']
    name = row['street_name']
    cross = row['cross_street']
    #rel = row['relation']
    #dist = row['distance_offset']
    town = row['town']
    borough = row['borough']
    township = row['township']
    county = row['county']
    state = 'Pennsylvania'

    result = ''
    bad = lambda x: pd.isnull(x) or x == ''

    def clean(s):
        return '' if bad(s) else str(s).lower().strip()

    def append(s, suffix):
        s = s.replace(suffix, '').strip()
        if s:
            s += ' ' + suffix

        return s

    num = clean(num)
    name = clean(name)
    cross = clean(cross)
    town = clean(town).replace('town', '').strip()
    borough = append(clean(borough), 'borough')
    township = append(clean(township), 'township')
    county = append(clean(county), 'county')

    # use cross street if street is missing
    if bad(name) and not bad(cross):
        name = cross
        cross = None

    if not bad(name): 
        if not bad(num):
            result += num + ' ' + name
        elif not bad(cross):
            result += name + ' and ' + cross
        else:
            result += name

    if result != '':
        result += ', '

    st = town or borough
    lt = county or township
    if st:
        result += st + ', '
    if lt:
        result += lt + ', '

    return result + state if result else ''


def add_address(df, col_name='std_address'):
    if not col_name in df:
        df[col_name] = ''

    def aa(row):
        row[col_name] = make_address(row)
        return row

    return df.apply(aa, axis=1)


def scrub_csv(filename=None):
    filename = filename or '../data/2013_01_30_PaTrafficStops.csv'
    outfile = '../data/all_good.csv'
    tdf = pd.read_csv('filename')
    a = add_address(tdf)
    va = a[a['std_address'] != '']
    a.to_csv(outfile, index=False)

