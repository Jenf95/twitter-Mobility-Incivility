import csv
import pandas as pd
import random

file_path = 'C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/Cursing_Lexicon_05.11.17.txt'
file_export = 'C:/Users/Jenny/Desktop/BU COM/Fall 2019/EM 855 Comp Assisted Text Analysis/Research Project/Data/Cursing_Lexicon_in_one_line.txt'

uncivil_dictionary = open(file_path, 'r')
dictionary = open(file_export, 'w+')
lines = uncivil_dictionary.readlines()
print(lines)
words =''
for word in lines:
	word = word [:-2] + '|'
	words+=word

dictionary.write(words)


