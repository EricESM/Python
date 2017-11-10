import csv
import numpy as np


'''Main'''
col = 0
row = 0
temp = 0
'''matrix = [col][row];'''

print("Enter the Size of the matrix: ")

col = input('col: ')
row = input('row: ')

print "Enter ",col * row," numbers for the matrix:"
'''print(col, row);'''

elements = []
elements.append([])
elements.append([])

for i in xrange(row):
	#print "row: ",i
	for j in xrange(col):
		#print "column: ",j
		print"Enter your [",i,j,"] number: "
		temp = raw_input()
		elements[i].append(temp)

for a in xrange(row):
	for b in xrange(col):
		print(elements[a][b])
	

#for i in xrange(col * row):
	'''temp[0] = input();'''
	'''array.append(array,temp);'''
	'''print(temp);'''
#	temp = raw_input()
#	elements.append(temp)	

#print(elements)

#print("Enter all the numbers you want to search in the matrix")