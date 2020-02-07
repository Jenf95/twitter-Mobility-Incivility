import pandas as pd
import csv
import numpy as np
import os
import glob
import random
import tweepy

path_merge='C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/Bernie_Biden_Warren_aug_sep.csv'
input_path = 'C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/Raw Data'
path_sample='C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/100_sample_Bernie_Biden_Warren_aug_sep.csv'
path_sample_1000 = 'C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/1000_sample_Bernie_Biden_Warren_aug_sep.csv'
path_sample_10000 = 'C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/10000_sample_Bernie_Biden_Warren_aug_sep.csv'
Bernie_ = 'C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/Raw Data/Bernie'
Biden_ = 'C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/Raw Data/Biden'
Warren_ = 'C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/Raw Data/Warren'
out_ = 'C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM797 Network Anlysis/final project/network_2.csv'
Bernie = 'C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/Raw Data/bernie.csv'
Biden = 'C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/Raw Data/biden.csv'
Warren = 'C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/Raw Data/warren.csv'

def concatenate(indir=Warren_, outfile=Warren):
    os.chdir(indir)
    dfList = [pd.read_csv(filename,skiprows=0, engine='c') for filename in glob.glob('*.csv')]
    concateDF = pd.concat(dfList, axis=0, sort=False)
    concateDF.columns = ['id','time','created_at','from_user_name','text','filter_level','possibly_sensitive','withheld_copyright','withheld_scope', \
    	'truncated','retweet_count','favorite_count','lang','to_user_name','in_reply_to_status_id','quoted_status_id','source','location','lat','lng',\
    	'from_user_id','from_user_realname','from_user_verified','from_user_description','from_user_url','from_user_profile_image_url','from_user_utcoffset',
    	'from_user_timezone','from_user_lang','from_user_tweetcount','from_user_followercount','from_user_friendcount','from_user_favourites_count',
    	'from_user_listed','from_user_withheld_scope','from_user_created_at']
    print(concateDF.shape[0])
    concateDF.to_csv(Warren, mode ='w', sep = ',',index=False)
    print('data ready')

concatenate()

def shape(file):
	df = pd.read_csv(file)
	print(type(df))
	print(df.shape[0])
	df['date'] =pd.to_datetime(df.created_at)
	df.sort_values(by=['date'],inplace=True)
	print(type(df))
	df = df.iloc[0:50000]
	print(df.shape[0])
	df.to_csv(out_, mode = 'w', sep = ',', index = False)
	return

#shape(out_)

'''
#COUNT THE ENTRIES: 18,237,296 rows * 36 columns
reader = pd.read_csv(path_merge, iterator=True) 
col=['id','time','created_at','from_user_name','text','filter_level','possibly_sensitive','withheld_copyright','withheld_scope', \
    	'truncated','retweet_count','favorite_count','lang','to_user_name','in_reply_to_status_id','quoted_status_id','source','location','lat','lng',\
    	'from_user_id','from_user_realname','from_user_verified','from_user_description','from_user_url','from_user_profile_image_url','from_user_utcoffset',
    	'from_user_timezone','from_user_lang','from_user_tweetcount','from_user_followercount','from_user_friendcount','from_user_favourites_count',
    	'from_user_listed','from_user_withheld_scope','from_user_created_at']
count=0
for i in range(10000):
	try: 
	    chunk=reader.get_chunk(10000)
	    count+=chunk.shape[0]
	    print(count)
	except:
		StopIterations


#select 100 samples
n = 18237296
s = 100
skip = sorted(random.sample(range(1,n),n-s))
df=pd.read_csv(path_merge, skiprows=skip)

df.to_csv(path_sample, mode='w',index=False)


#select 1000 samples
n = 18237296
s = 1000
skip = sorted(random.sample(range(1,n),n-s))
df = pd.read_csv(path_merge, skiprows = skip)

df.to_csv(path_sample_1000, mode = 'w', index=False)

#select 10000 samples
n = 18237296
s = 10000
skip = sorted(random.sample(range(1,n),n-s))
df = pd.read_csv(path_merge, skiprows = skip)
df.to_csv(path_sample_10000, mode = 'w', index = False)


def select_samples(file,sample_size, path):
	n = 18237296
	skip = sorted(random.sample(range(1,n),n-sample_size))
	df = pd.read_csv(file, skiprows = skip)
	return df.to_csv(path, mode = 'w', index = False)
	#... 
	#finish this later
'''

