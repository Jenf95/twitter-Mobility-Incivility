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
	tweet_path = 'C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/labeledTweets.csv'
	biden = 'C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/biden_keywords.csv'
	warren = 'C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/warren_keywords.csv'
	sanders = 'C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/bernie_keywords.csv'
	path_output = 'C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/genderedTweets.csv'

	tweets = importTweets(tweet_path, header=0)

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

	for text in tweets.iloc[:,4]:
		temp = ''
		temp+= check_candidate('biden', biden , text)
		temp+= check_candidate('warren', warren , text)
		temp+= check_candidate('sanders', sanders , text)
		candidate.append(temp)
	#print(candidate)
	tweets['candidate'] = candidate

	tweets.to_csv(path_output, mode ='w', sep = ',',index=False) 

if __name__ == '__main__':
	main()