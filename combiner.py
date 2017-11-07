#! python3
# coding: utf-8

# In[ ]:

import pandas as pd
import os

#update to take basic user input
pathVar = r'' #path to file(s)
extVar = '.xlsx'#update to all crosstab variations
resultFile = 'result.xlsx' #name of file to be created
startrow = 10 #what row to start collecting data, 0 is default
sheet = 'Compensation Data' #0 = default

#build list of files to combine
print('Gathering files...')
fileList = []
for filename in os.listdir(pathVar):
	if filename.endswith(extVar):
		fileList.append(filename)
		print('%s added to list' %(filename))


# In[ ]:

#create data framme for each file
#combine dataframes into one
start = startrow -1
frames = [ pd.read_excel(os.path.join(pathVar,f),skiprows=start,sheetname=sheet) for f in fileList ]
#frames = [ pd.read_csv(os.path.join(pathVar,f),encoding='cp1252') for f in fileList ]
number = len(fileList)


# In[ ]:

#print('Combining %s files, please be patient :)' %(number))
result = pd.concat(frames)
del frames
#print combined dataframes into one exceel sheet
result.to_excel(os.path.join(pathVar,resultFile),sheet_name='ALLINFO',index=False)
del result
print('Done!')
os.system("pause")

# futures update for taking worksheets as well as workbooks
# filename = '2017_July_GSS.xlsx'
# sheetList = ['IND Hyderabad','IND Bangalore','IND','IRL Dublin','IRL','DEU','DEU Dusseldorf','BRA','BRA Sao Paulo','AUS','AUS Sydney','CAN','CAN Toronto','JPN','JPN Tokyo','US, SW and Revenue Cut','US National','US Phoenix','US Seattle','US NY Metro','US SF Bay','US Austin','UK National'
# ]
# 
