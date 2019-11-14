import random
def display_board(board):
	print("   |   |   ")
	print(" " + board[0] + " | " + board[1] + " | " + board[2])
	print("---|---|---")
	print(" " + board[3] + " | " + board[4] + " | " + board[5])
	print("---|---|---")
	print(" " + board[6] + " | " + board[7] + " | " + board[8])
	print("   |   |   ")


def player_input():
	choice = input("Enter your choice X or O: ")

	while choice != "X" and choice != "O":
		choice = input("Wrong input! Please Enter your choice as X or O: ")
	return choice


def place_choice(choice, position, board):
	board[position-1] = choice


def win_check(board,choice):
	if choice == "X":
		if board[0]+board[4]+board[8] == "XXX":
			return True
		elif board[2]+board[4]+board[6] == "XXX":
			return True
		elif board[0]+board[1]+board[2] == "XXX":
			return True
		elif board[3]+board[4]+board[5] == "XXX":
			return True
		elif board[6]+board[7]+board[8] == "XXX":
			return True
		elif board[0]+board[3]+board[6] == "XXX":
			return True
		elif board[1]+board[4]+board[7] == "XXX":
			return True
		elif board[2]+board[5]+board[8] == "XXX":
			return True
		else:
			return False

	else:
		if board[0]+board[4]+board[8] == "OOO":
			return True
		elif board[2]+board[4]+board[6] == "OOO":
			return True
		elif board[0]+board[1]+board[2] == "OOO":
			return True
		elif board[3]+board[4]+board[5] == "OOO":
			return True
		elif board[6]+board[7]+board[8] == "OOO":
			return True
		elif board[0]+board[3]+board[6] == "OOO":
			return True
		elif board[1]+board[4]+board[7] == "OOO":
			return True
		elif board[2]+board[5]+board[8] == "OOO":
			return True
		else:
			return False


def full_board_check(board):
	if " " in board:
		return False
	else:
		return True


def first_go():
	if random.randint(1,2) == 1:
		return "player1"
	else:
		return "player2"


def space_check(board,position):
	if board[position-1] == " ":
		return True
	else:
		return False


def player_position_choice(board):
	position = input("Enter your next position between (1-9): ")

	while position not in ["1","2","3","4","5","6","7","8","9"]:
		position = input("Wrong position input! Please Enter your next position between (1-9): ")
	position = int(position)
	while not space_check(board,position):
		position = input("Your choosen position is not empty! Please Enter another position: ")
		while position not in ["1","2","3","4","5","6","7","8","9"]:
			position = input("Wrong position input! Please Enter your next position between (1-9): ")
		position = int(position)
	return position


def replay():
	a = input("Do you want to play again? Enter Yes or No : ")
	while a != "Yes" or a != "No":
		if a == "Yes":
			return True
		elif a == "No":
			return False
		else:
			a = input("Do you want to play again? Please! Enter Yes or No : ")




print("Welcome to Tic Tac Toe!")

game_on = True

while game_on:
	board = [" "," "," "," "," "," "," "," "," "]
	display_board(board)
	player1 = player_input()
	if player1 == "X":
		player2 = "O"
	else:
		player2 = "X"

	f = first_go()
	if f == "player1":
		print("Player 1 will go first!")
	else:
		print("Player 2 will go first!")

	while True:
		position = player_position_choice(board)
		place_choice(player1, position, board)
		display_board(board)
		if win_check(board, player1):
			print("Player 1 Wins!")
			break
		elif full_board_check(board):
			print("Board is Full!")
			break
		position = player_position_choice(board)
		place_choice(player2, position, board)
		display_board(board)
		if win_check(board, player2):
			print("Player 2 Wins!")
			break
		elif full_board_check(board):
			print("Board is Full!")
			break


	game_on = replay()

