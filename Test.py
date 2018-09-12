#Date: 05-09-18
#Author: A. Suraj Kumar
#Python Test
#Read the ‘phones.txt’ file and extract the phone numbers and email ids. Extracted information need to be stored in ‘info.txt’.   

import re
import sys

f_read=open('phones.txt','r')
#f_read=sys.argv[1]
#pattern1 = sys.argv[1]
#fname=open(f_read,'r')
#pattern2=re.compile
def phone():
	for i in f_read:
		pattern1=re.findall(r'\w+@\W+',i)
		pattern2=re.findall(r'\d{2}-\d{4}-{8}',i)
		pattern3=re.findall(r'\d{2} \d{4} {8}',i)	
		pattern4=re.findall(r'(\d{2})(\d{4})({8})',i)
		f=open('info.txt','w+')
		f.write('The Extracted phone numbers: '+i)
		f.close()
	print('Information has been stored to File')

phone()
