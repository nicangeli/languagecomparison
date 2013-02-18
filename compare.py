#! /usr/bin/env python

LANGUAGE_LENGTH = 4;
languages = ["AAAB", "AABB", "AABC", "AHDD", "SIAD"];

def compareTwoLanguages(l1, l2):
	count = 0;
	for index in range(0, LANGUAGE_LENGTH):
		if(l1[index] == l2[index]):
			count += 1;
	return (float(count)/LANGUAGE_LENGTH);

for l in range(len(languages)):
	#l is the element we're testing
	#we want to get the rest of the elements in the array
	other_elements = languages[:];
	del other_elements[l];
	print('Comparing ' + languages[l]  + ' to other languages: ')
	coefficients = []
	for element in other_elements:
		coefficients.append(compareTwoLanguages(languages[l], element));
	print(coefficients);




