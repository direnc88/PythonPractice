#! python 3

#removeCsvHeader.py - Removes the header from all CSV files in the current
# working directory

import csv, os
os.makedirs('headerRemoved', exist_ok = True)

#Loop thorugh every file in the current working directory.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        countinue #skip non-csv files


    print('Removing header from ' + csvFilename + '...')

    #TODO: Read the CSV file in (skipping first row).

    #TODO: Write out the CSV file.

    
