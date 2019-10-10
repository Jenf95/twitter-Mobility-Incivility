import pandas as pd
import csv
import numpy as np
import os
import glob

path_merge='C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/Bernie_Biden_Warren_aug_sep.csv'
input_path = 'C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/Raw Data'
path_sample='C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/100_sample_Bernie_Biden_Warren_aug_sep.csv'

def concatenate(indir=input_path, outfile=path_merge):
    dfList =[] 
    os.chdir(indir)  
    fileList = glob.glob('*.csv')  
        print(filename)
        df=pd.read_csv(filename, skiprows=0)
        dfList.append(df)
    concateDF = pd.concat(dfList, axis=0, sort=False)
    concateDF.columns = ['id','time','created_at','from_user_name','text','filter_level','possibly_sensitive','withheld_copyright','withheld_scope', \
    	'truncated','retweet_count','favorite_count','lang','to_user_name','in_reply_to_status_id','quoted_status_id','source','location','lat','lng',\
    	'from_user_id','from_user_realname','from_user_verified','from_user_description','from_user_url','from_user_profile_image_url','from_user_utcoffset',
    	'from_user_timezone','from_user_lang','from_user_tweetcount','from_user_followercount','from_user_friendcount','from_user_favourites_count',
    	'from_user_listed','from_user_withheld_scope','from_user_created_at']
    concateDF.to_csv(path_merge, mode ='w', sep = ',',index=False)

concatenate()

'''COUNT THE ENTRIES: 18,237,296 rows * 36 columns
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
'''

#select 100 samples
n = 18237296
s = 100
skip = sorted(random.sample(range(1,n),n-s))
df=pd.read_csv(path_merge, skiprows=skip)

df.to_csv(path_sample, mode='w',index=False)