"""
This script takes a csv file and generates a line for each column, checking if it is
* a string 
* a number (int / float)
* a boolean

It checks the limits for int
"""

import pandas as pd
import numpy as np
import re

csv_file = '/tmp/cars.csv' # https://corgis-edu.github.io/corgis/datasets/csv/cars/cars.csv

# read the csv
df = pd.read_csv(csv_file)

# iterate over all columns, get max length of entry, and check for types in column
for col in df.columns:
    arr = df[col]
    size = 0
    value = ''
    types = []
    min_value = None
    max_value = None
    field_type = None
    blank = False
    
    # check all values in column
    for ar in arr:
        # save the length 
        if len(str(ar)) > size:
            size = len(str(ar))
        # check the type
        if (type(ar) not in types):
            types.append(type(ar))
        # check min and max for estimation on needed field type
        if ( type(ar) in (float, int) ):
            # how to handle NaN  (not a number)
            if (ar is np.nan):
                blank = True
            # initialize min_value, max_value on first occurence
            if min_value is None:
                min_value = ar
            if max_value is None:
                max_value = ar
            # check of less than min_value
            if ar < min_value:
                min_value = ar
            # check if larger than max_value
            if ar > max_value:
                max_value = ar

    # make a stub out of column name
    name = col.lower()
    # replace all non-alphanumeric values
    name = re.sub('[^0-9a-zA-Z]+', '_', name)

    # order of precedence
    #1 string catches (almost) everything
    #2 float
    #3 int
    #4 bool
    
    if str in types:
        print(name + ' = models.CharField("', col,'", max_length=', str(size+3), ')', sep='')
    elif float in types:
        print(name + ' = models.FloatField("', col,'")', sep='')
    elif int in types:
        # check if values exceed the limits
        # check if positive only
        if (min_value >= 0):
            # PositiveSmallIntegerField:  0 to 32767
            if (min_value <= 32767 and max_value <= 32767):
                field_type = 'PositiveSmallIntegerField'
            # PositiveIntegerField: 0 to 2147483647
            elif (min_value <= 2147483647 and max_value <= 2147483647):
                field_type = 'PositiveIntegerField'
            # PositiveBigIntegerField:  0 to 9223372036854775807
            elif (min_value <= 9223372036854775807 and max_value <= 9223372036854775807):
                field_type = 'PositiveBigIntegerField'
        # also negative numbers
        else:
            # IntField: -2147483648 to 2147483647
            if (min_value >= -2147483648 and max_value <= 2147483647):
                field_type = 'IntField'
            # BigIntegerField: -9223372036854775808 to 9223372036854775807
            elif (min_value >= -9223372036854775808 and max_value <= 9223372036854775807):
                field_type = 'BigIntegerField'

        print(name + ' = models.' + field_type + '("' + col + '"', end='')
        if blank:
            print(', blank=True', end = '') 
        print(')')
    elif bool in types:
        print(name + ' = models.BooleanField("', col,'")', sep='')
