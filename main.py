###start up
from random import randint
print("Welcome to O's and X's :)")
turn = 1
####


###board stuff
game_incomplete = False
#each row starts with extra 3 spaces to compensate for size of x when it appears on the board
boardheader = ["-","-","-","-","-","-","-"]
boardfooter = ["-","-","-","-","-","-","-"]
board1 = ["|"," "," "," "," "," ","|"]
board2 = ["|"," "," "," "," "," ","|"]
board3 = ["|"," "," "," "," "," ","|"]


#print board function
def print_board():
	print("".join(boardheader))
	print("".join(board1))
	print("".join(board2))
	print("".join(board3))
	print("".join(boardfooter))
print_board()   
####


###turns                
def player_turn():
	global turn
	print("turn %s.."%turn)                      
	row_choice = int(input("Row: "))            #inputs
	column_choice = int(input("Column: ")) 		#inputs
	if column_choice == 2:				#set column choices to actual positions
		column_choice = 3
	elif column_choice == 3:
		column_choice = 5
	
	#identify which board variables to edit
	if row_choice == 1:                      
		if board1[column_choice] == " ":		#statement to stop computer overiding already taken space
			board1.pop(column_choice)           #remove space from index where we want the x
			board1.insert(column_choice,"x")	#insert game piece
			print_board()
			turn = turn + 1
		else:
			print("Space already taken, try again.")
			player_turn()		       
	elif row_choice == 2:
		if board2[column_choice] == " ":		#statement to stop computer overiding already taken space
			board2.pop(column_choice)           #remove space from index where we want the x
			board2.insert(column_choice,"x")
			print_board()
			turn = turn + 1
		else:
			print("Space already taken, try again.")
			player_turn()
        
	elif row_choice == 3:
		if board3[column_choice] == " ":		#statement to stop computer overiding already taken space
			board3.pop(column_choice)           #remove space from index where we want the x
			board3.insert(column_choice,"x")
			print_board()
			turn = turn + 1
		else:
			print("Space already taken, try again.")
			player_turn()
        
	else:
		"Please enter a row and column 1, 2 or 3."
		turn()  

def computer_turn():
	global turn
	row_comp = randint(1,3)				#randomly choose row and column numbers
	column_comp = randint(1,3)
	if column_comp == 2:				#set column choices to actual positions
		column_comp = 3
	elif column_comp == 3:
		column_comp = 5
	if row_comp == 1:
		if board1[column_comp] == " ":		#statement to stop computer overiding already taken space
			board1.pop(column_comp)           #remove space from index where we want the x
			board1.insert(column_comp,"o")
			print_board()
		else:
			computer_turn()			#recalculate row and oclumn if position taken

	elif row_comp == 2:
		if board2[column_comp] == " ":
			board2.pop(column_comp)           #remove space from index where we want the x
			board2.insert(column_comp,"o")
			print_board()
		else:
			computer_turn()

	elif row_comp == 3:
		if board3[column_comp] == " ":
			board3.pop(column_comp)           #remove space from index where we want the x
			board3.insert(column_comp,"o")
			print_board()
		else:
			computer_turn()
###

###check for win

def check_for_win():
	global board1
	global board2
	global board3
	#horizontal wins
	if (board1[1] == board1[3] and board1[3] == board1[5]) and (board1[1] == "x" or board1[1] == "o"):
		print("%s wins!"%board1[1])
		exit()
	if (board2[1] == board2[3] and board2[3] == board2[5]) and (board2[1] == "x" or board2[1] == "o"):
		print("%s wins!"%board2[1])
		exit()
	if (board3[1] == board3[3] and board3[3] == board3[5]) and (board3[1] == "x" or board3[1] == "o"):
		print("%s wins!"%board3[1])
		exit()
	#vertical wins
	if (board1[1] == board2[1] and board2[1] == board3[1]) and (board1[1] == "x" or board1[1] == "o"):
		print("%s wins!"%board1[1])
		exit()
	if (board1[3] == board2[3] and board2[3] == board3[3]) and (board1[3] == "x" or board1[3] == "o"):
		print("%s wins!"%board1[3])
		exit()
	if (board1[5] == board2[5] and board2[5] == board3[5]) and (board1[5] == "x" or board1[5] == "o"):
		print("%s wins!"%board1[5])
		exit()
	#diagonal wins
	if (board1[1] == board2[3] and board2[3] == board3[5]) and (board1[1] == "x" or board1[1] == "o"):
		print("%s wins!"%board1[1])
		exit()
	if (board3[1] == board2[3] and board2[3] == board1[5]) and (board3[1] == "x" or board3[1] == "o"):
		print("%s wins!"%board3[1])
		exit()
###		

###Go counter thing

for x in range(4):
	#player turn
	player_turn()
	check_for_win()
	print("The computer is taking its turn.")
	print("hit enter when ready.")
	input()
	#computer turn
	computer_turn()
	check_for_win()

	x = x + 1
	
###


	
	
