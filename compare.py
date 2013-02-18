#! /usr/bin/env python
import itertools

def compareTwoLanguages(l1, l2):
	count = 0;
	for index in range(0, LANGUAGE_LENGTH):
		if(l1[index] == l2[index]):
			count += 1;
	return (float(count)/LANGUAGE_LENGTH);

def buildLanguages():
	cartesian = itertools.product(CHARACTERS_IN_LANGUAGE, repeat=LANGUAGE_LENGTH)
	l = []
	for c in cartesian:
		l.append("".join(c))
	return l

LANGUAGE_LENGTH = 2;
CHARACTERS_IN_LANGUAGE = ['A', 'B'];
languages = buildLanguages(); #length of this list will be the CHARACTERS_IN_LANGUGE ^ LANGUAGE_LENGTH

for l in range(len(languages)):
	#l is the element we're testing
	#we want to get the rest of the elements in the array
	other_elements = languages[:];
	del other_elements[l];
	print('Comparing ' + languages[l]  + ' to other languages: ')
	coefficients = []
	sum = 0;
	for element in other_elements:
		tmp = compareTwoLanguages(languages[l], element)
		coefficients.append(tmp);
		sum += tmp
	print(coefficients);
	print sum




