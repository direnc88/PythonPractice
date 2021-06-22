#! python 3

#removeCsvHeader.py - Removes the header from all CSV files in the current
# working directory

import csv, os
os.makedirs('headerRemoved', exist_ok = True)

