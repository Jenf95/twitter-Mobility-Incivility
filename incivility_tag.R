install.packages('data.table')
install.packages('stringr')

library(data.table)
library(stringr)
library(tidyverse)
library(tm)
library(SparseM)
library(SnowballC)

tbl = fread("C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/10000_sample_Bernie_Biden_Warren_aug_sep.csv")
tbl = tbl[, c('id', 'time', 'created_at','from_user_name','text','filter_level','lang','to_user_name','in_reply_to_status_id','quoted_status_id','source','location','from_user_id','from_user_realname','from_user_verified','from_user_description','from_user_url','from_user_profile_image_url','from_user_tweetcount','from_user_followercount','from_user_friendcount','from_user_favourites_count','from_user_listed'), with = F]

uncivil_words <- readChar("C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/words.txt", nchars = 1e6)
#words <- 
tbl$incivility <- ifelse(grepl(uncivil_words,tbl$text),'1','0')
fwrite(tbl, 'C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/10000_sample_Bernie_Biden_Warren_aug_sep_tagged.csv')
summary(tbl)


