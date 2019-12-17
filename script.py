import csv
tweets = 'C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/labeledTweets_Copy.csv'
# import tweet csv
tweetArray = []
with open(tweets, 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in reader:
		tweetArray.append(row)

# import curse csv
curseArray = []
with open('curse.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in reader:
		curseArray.append(row)

# create variable to hold *new* labeled tweet array
labeledTweets = []

# map tweets through curseword array
for index, tweet in enumerate(tweetArray):
	labeledTweets.append(tweet)
	# print index
	for curse in curseArray:
		if str(curse[0]) in tweet[4].split(): 
			print (curse)
			labeledTweets[index][5] = 1
			break
		elif index > 0:
			labeledTweets[index][5] = 0

# write + export csv from labeledTweets list
with open('labeledTweets.csv', 'w') as writeFile:
	writer = csv.writer(writeFile)
	writer.writerows(labeledTweets)

print labeledTweets[9980][4]
print labeledTweets[9980][5]

writeFile.close()



		