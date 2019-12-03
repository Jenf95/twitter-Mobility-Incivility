import csv

# import tweet csv
tweetArray = []
with open('tweets.csv', 'rb') as csvfile:
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
	curse_words = []
	for curse in curseArray:
		if str(curse[0]) in tweet[4].split():
			print curse
			curse_words.append(str(curse[0]))
	if len(curse_words) > 0:
		labeledTweets[index][5] = 1
		labeledTweets[index][6] = ", ".join(curse_words)
	else:
		labeledTweets[index][5] = 0
		labeledTweets[index][6] = "n/a"

# write + export csv from labeledTweets list
with open('labeledTweets-2.csv', 'w') as writeFile:
	writer = csv.writer(writeFile)
	writer.writerows(labeledTweets)

print labeledTweets[9980][4]
print labeledTweets[9980][5]

writeFile.close()



		