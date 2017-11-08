#! python3
# coding: utf-8
#interface for combining scripts

import os
#temp solution to find necessary combiner module
#find dynamic solution for sharing
fudge = r'c:\python\merger'
os.chdir(fudge)
import combiner

# take input to fill path to files, header row & sheetname
print('Enter file location path')
path = input()

print('Enter number of row for headers in files...')
rowNum = int(input())

print('Please enter name of sheet in files...') #update to take sheet location in addition to name
sheet = input()

combiner.excel_mix(pathVar = path,startrow = rowNum,sheet = sheet)
