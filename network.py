"""
"""

# std lib
import csv
import pandas as pd
import re

def retweet_handle():
	file = "C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM797 Network Anlysis/final project/network_2.csv"
	#path_output = "C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM797 Network Anlysis/final project/network.csv"
	df = pd.read_csv(file)
	def find_handle(row):
		text = str(row['text'])
		if text[:2] == 'RT':
			row['retweetee'] = (text.split('@'))[1].split(':')[0]
		else:
			row['retweetee'] = ''
		#print(row['retweetee'])
		return row
	df = df.apply(find_handle, axis = 1)
	#print(df['retweetee'][3:10])
	return df.to_csv(file, mode = 'w', sep = ',', index=False)


retweet_handle()

