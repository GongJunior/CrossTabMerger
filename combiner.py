#make better notes
#add help notes
#future - add function for worksheet

def excel_mix(pathVar,startrow,sheet): #function for excel workbooks
	import pandas as pd
	import os

	#variables to take from user input
	#pathVar = r'' #path to file(s)
	#extVar = '.xls'#update to all crosstab variations
	#startrow = 10 #what row to start collecting data, 0 is default
	#sheet = 'Compensation Data' #0 = default
	resultFile = 'result.xlsx' #name of file to be created
	

	#build list of files to combine
	print('Gathering files...')
	fileList = []
	for filename in os.listdir(pathVar):
		if filename.lower().endswith('.xlsx') or filename.lower().endswith('.xls'):
			fileList.append(filename)
			print('%s added to list' %(filename))
			option = 'excel'
		elif filename.lower().endswith('.csv'):
			fileList.append(filename)
			print('%s added to list' %(filename))
			option ='csv'
	#print error if result.xlsx already exists in fileList
	
	#create data frame for each file
	#combine dataframes into one
	start = startrow -1
	if option == 'excel':
		frames = [ pd.read_excel(os.path.join(pathVar,f),skiprows=start,sheetname=sheet) for f in fileList ]
	elif option == 'csv':
		frames = [ pd.read_csv(os.path.join(pathVar,f),encoding='cp1252') for f in fileList ]
	else:
		print('Invalid file type!')
	
	number = len(fileList)
	print('Combining %s files, please be patient :)' %(number))
	result = pd.concat(frames)
	del frames
	#print combined dataframes into one exceel sheet
	result.to_excel(os.path.join(pathVar,resultFile),sheet_name='ALLINFO',index=False)
	del result
	print('Done!')

