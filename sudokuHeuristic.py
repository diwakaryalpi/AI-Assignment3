import random
import math
import numpy as np
from copy import deepcopy
import time



board=[]
inputfile = open('sudokuinput.txt','r')
count=0
flag=0

# Reading input from file

for line in inputfile:
	line = line[:-1]
	if line[0]!='S':
		flag=1
	if flag==1 and count<9:
		temp = list(line)
		temp = [int(x) for x in temp]
		board.append(temp)
		count+=1

n=9
time_start = time.clock()
legalValues = deepcopy(board)


# Assigning initial values between 1 and 9 to all the empty spaces
for i in range(9):
	for j in range(9):
		if legalValues[i][j]==0:
			legalValues[i][j] = {'value':0, 'moves' :[1,2,3,4,5,6,7,8,9]}
		else:
			legalValues[i][j] = {'value':legalValues[i][j], 'moves': []}	

def nextVariable():       # Based on Minimum Remaining Values, writing a function to find the next variable position 
	minMRV = 11
	minMRV_row = -1
	minMRV_col = -1
	for i in range(9):
		for j in range(9):
			if legalValues[i][j]['value']==0 and len(legalValues[i][j]['moves'])<minMRV:
				minMRV = len(legalValues[i][j]['moves'])
				minMRV_row = i
				minMRV_col = j

	return minMRV_row,minMRV_col

def addConstraints(row,col,value):     # Function to add constraints when the empty space is assigned with a value
	
	removedValues = []
	for i in range(9):
		if legalValues[i][col]['value']==0:					# Adding constraints to the variables in the same row
			if value in legalValues[i][col]['moves']:
				legalValues[i][col]['moves'].remove(value)
				temp=[]
				temp.extend([i,col])
				removedValues.append(temp)
		if legalValues[row][i]['value']==0:
			if value in legalValues[row][i]['moves']:		# Adding constraints to the variables in the same column
				legalValues[row][i]['moves'].remove(value)
				temp=[]
				temp.extend([row,i])
				removedValues.append(temp)

	row_start = (row/3) * 3
	col_start = (col/3) * 3
	for i in range(row_start,row_start+3):
		for j in range(col_start,col_start+3):
			if legalValues[i][j]['value']==0:				# Adding constraints to the variables in the sub-box(smaller 3*3 one)
				if value in legalValues[i][j]['moves']:
					legalValues[i][j]['moves'].remove(value)
					temp=[]
					temp.extend([i,j])
					removedValues.append(temp)

	flag=0
	for position in removedValues:
		if len(legalValues[position[0]][position[1]]['moves'])==0:		
			flag=1			#This is for Forward Checking, understanding if any variable has zero legal moves after the constraints are added.
			break			
	removedValues.append(flag)

	return removedValues

def removeConstraints(row,col,value,removedValues):
	for position in removedValues:				# Removing the constraints on all the positions since the constraints are added when a value is re assigned to 0
		legalValues[position[0]][position[1]]['moves'].append(value)

def constraints():
	for i in range(9):								# Function to initialize the board with all the constraints.
		for j in range(9):							# Assigning unique values to the empty spaces
			if legalValues[i][j]['value']==0:
				for k in range(9):
					if legalValues[i][k]['value'] in legalValues[i][j]['moves']:
						legalValues[i][j]['moves'].remove(legalValues[i][k]['value'])

					if legalValues[k][j]['value'] in legalValues[i][j]['moves']:
						legalValues[i][j]['moves'].remove(legalValues[k][j]['value'])

				row_start = (i/3) * 3
				col_start = (j/3) * 3
				for k in range(row_start,row_start+3):
					for l in range(col_start,col_start+3):
						if legalValues[k][l]['value'] in legalValues[i][j]['moves']:
							legalValues[i][j]['moves'].remove(legalValues[k][l]['value'])						

count=0
def solveSudoku(row,col):

	if row==-1 and col==-1:
		return True

	legalMovesList = deepcopy(legalValues[row][col]['moves'])

	for value in legalMovesList:
		legalValues[row][col]['value'] = value 		
		removedPositions = addConstraints(row,col,value) # calling Add constraints function and get the list of positions changed check if something fails in forward checking
		if removedPositions[-1]==0:			# To check if the forward checking returns any error
			(nextRow,nextCol) = nextVariable()		# Get the position of next variable based on MRV
			if solveSudoku(nextRow,nextCol):		# Call the recursive function to next variable
				return True
		global count
		count+=1
		legalValues[row][col]['value'] = 0			# If recursive function returns False, reassign value as 0
		removeConstraints(row,col,value,removedPositions[:-1])    # Remove constraints imposed by above value
	return False									# If none of the legalMoves for this position returns True, return False



constraints()
(row,col) = nextVariable()


start = "\033[1m"
end = "\033[0;0m"



# For printing the final solution
if solveSudoku(row,col):
	print "Below is the sudoku after solving\n"
	for i in range(9):
		if(i%3==0):
			print start + '=====' * 8 + end
		else:
			print '-----' * 8
		print start+"||"+end,
		for j in range(8):
			if j==2 or j==5:
				print str(legalValues[i][j]['value'])+start+ " ||"+end,
			else:
				print legalValues[i][j]['value'], "|",
		print legalValues[i][8]['value'],
		print start+"||"+end
	print start+'=====' * 8+end
else:
	print "Can not be solved\n"

print "Number of backtrackings: ",count

time_end = time.clock()
print "Total time taken to solve sudoku puzzle in seconds: "+str(time_end - time_start)
