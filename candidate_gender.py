"""
"""

# std lib
import csv
import pandas as pd
# third party lib

def importTweets(filepath, header = None):
	"""
	"""
	return pd.read_csv(filepath, header = header, encoding='unicode_escape')

def main():
	"""
	"""
	names = ('biden','warren','sanders')
	#tweet_path = 'C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/labeledTweets.csv'
	biden, warren, sanders = ['C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/{}_keywords.csv'.format(i) for i in names]
	
	#path_output = 'C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/genderedTweets.csv'

	path = 'C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/Manually_Coded_Data_1k.csv'


	coded = importTweets(path, header = 0)
	print('data ready')
	biden = importTweets(biden)
	#print(type(biden))
	biden = biden.dropna(axis='columns',thresh=2)
	biden = biden.dropna(axis='rows')
	#print(biden)
	warren = importTweets(warren)
	#print(warren)
	sanders = importTweets(sanders)
	#print(sanders)

	candidate = []
	def check_candidate (name,df,text):
		for n in df.iloc[:,0]:
			if str(n).lower() in str(text).lower():
				return name + ' '
		return ''

	for text in coded.iloc[:,6]:
		temp = ''
		temp+= check_candidate('biden', biden , text)
		temp+= check_candidate('warren', warren , text)
		temp+= check_candidate('sanders', sanders , text)
		candidate.append(temp)
	print(candidate)
	coded['candidate'] = candidate

	#bsep, wsep, ssep = [coded[coded['candidate'].str.match('{}'.format(i) for i in ['biden','warren','sanders'])]]
	bsep = coded[coded['candidate'].str.contains('biden')]
	wsep = coded[coded['candidate'].str.contains('warren')]
	ssep = coded[coded['candidate'].str.contains('sanders')]


	#tweets.to_csv(path, mode ='w', sep = ',',index=False) 
	#how do you export dataframes in batches
	#lists = [bsep, wsep, ssep]
	#for df in lists:
		#df.to_csv(('C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/{}_coded.csv'.format(i) for i in names), mode = 'w', sep = ',', index = False)
	bsep.to_csv('C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/biden_coded.csv', mode = 'w', sep = ',', index = False)		
	wsep.to_csv('C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/warren_coded.csv', mode = 'w', sep = ',', index = False)		
	ssep.to_csv('C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/sanders_coded.csv', mode = 'w', sep = ',', index = False)		

if __name__ == '__main__':
	main()