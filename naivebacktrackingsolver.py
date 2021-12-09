board=[]
inputfile = open('sudokuinput.txt','r')
count=0
flag=0
import time

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

def isValid(board,row,col,value):    # Function to check for unique values in rows and columns
	for i in range(9):
		if board[i][col] == value:    
			return False
		if board[row][i] == value:    
			return False
	row_start = (row/3) * 3
	col_start = (col/3) * 3
	for i in range(row_start,row_start+3):
		for j in range(col_start,col_start+3):     # Check for the values in the sub-box(smaller 3*3 one)
			if board[i][j] == value:
				return False
	return True



def solveSudoku(board,row,col):                     # Function to understand the basic backtracking
	if row>n-1:								# If solution is found that follows all the sudoku rules
		return True
	if board[row][col]!=0:
		if col==n-1:						# Filling the space with valid values
			if solveSudoku(board,row+1,0):
				return True
		else:
			if solveSudoku(board,row,col+1):   # To check if the next recursion is not the end of row and not a variable(already filled by user)
				return True
	else:
		for value in range(1,10):			
			if isValid(board,row,col,value):      # If the value is valid then assign the value to the open space
				board[row][col] = value

				if col==n-1:	# if its the end of column then call the recursive function on the next row else call recursive function on same row and next column
					if solveSudoku(board,row+1,0):
						return True
				else:									
					if solveSudoku(board,row,col+1):
						return True
				global countBT
				countBT+=1
				board[row][col] = 0	
	
	return False	


start = "\033[1m"
end = "\033[0;0m"


# For printing solution

countBT=0

if solveSudoku(board,0,0):
	print "Below is the sudoku after solving\n"
	for i in range(9):
		if(i%3==0):
			print start + '=====' * 8 + end
		else:
			print '-----' * 8
		print start+"||"+end,
		for j in range(8):
			if j==2 or j==5:
				print str(board[i][j])+start+ " ||"+end,
			else:
				print board[i][j], "|",
		print board[i][8],
		print start+"||"+end
	print start+'=====' * 8+end
else:
	print "Can not be solved\n"

print "Number of backtrackings using naive backtracking algorithm: ",countBT

time_end = time.clock()
print "Total time taken to solve sudoku puzzle in seconds: "+str(time_end - time_start)
