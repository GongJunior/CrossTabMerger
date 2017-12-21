#! python3
# coding: utf-8
#interface for combining scripts

import os
#temp solution to find necessary combiner module
fudge = r'c:\python\merger'
os.chdir(fudge)
import combiner

# take input to fill path to files, header row & sheetname
print('Enter file location path')
path = input()

print('Enter number of row for headers in files...')
rowNum = int(input())

print('Are you combining sheets or workbooks?')
answer = input()
if answer.lower() == 'sheets':
	print('enter filename including .xlsx')
	file = input()
	allSheets = combiner.sheet_list(path,file)
	combiner.sheet_mix(path,file,rowNum,allSheets)
elif answer.lower() == 'workbooks':
	print('Please enter name of sheet in files...')
	sheet = input()
	if sheet == '0':
		sheet = 0

	combiner.excel_mix(pathVar = path,startrow = rowNum,sheet = sheet)
else:
	print('not an option, try again!')




#import combiner