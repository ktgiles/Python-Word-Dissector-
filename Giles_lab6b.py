#Giles_6b.py
#Created by Kaitlin Giles, 10/13/2021
#Write a program that reads a word, and prints the number of letters in the word, the number of vowels in the word, 
#and the percentage of vowels 

vowel = 0.0
count = 0.0
test = raw_input('Enter a word:')
for element in test: 
	if(element=='a' or element=='A' or element=='e' or element=='E' or element=='i' or element=='I' 
		or element =='o' or element=='O' or element=='u' or element=='U'):
			vowel += 1
	count += 1
percentage = vowel/count * 100
print 'Letters: ', int(count)
print 'Vowels: ', int(vowel)
format_perc = "{:.2f}".format(percentage)
print 'Percentage of vowels: ', format_perc	
