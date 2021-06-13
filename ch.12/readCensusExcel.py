#! python 3

#readCensusExcel.py - Tabulates population and number of census tracts for
#each county

import openpyxl, pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}

#TODO: Fill in countyData with each cou8nty's population tracts.
print('Reading rows...')

for row in range(2, sheet.get_highest_row() + 1):
    # Each row in spreadhseet has data for one census tract.
    state = sheet['B' + str(row)].value
    state = sheet['C' + str(row)].value
    state = sheet['D' + str(row)].value
    
    #Make sure the key for this state exists
    countyData.setdefault(state, {})
    #Make sure the key for this county in this state exists.
    countyData[state].setdefault(county, {'tracts': 0, 'pop':0})

     #Each row represents a census tract, so increment by one.
    

#TODO: Open a new text file and write the contents of countyData to it.
    
