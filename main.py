from abc import ABC, abstractmethod

# This is the board the game is played on
boardMatrix = [
	[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]
]
print("*                             *")


print('A3 |  B3 *| C3', '___|______|_____        *', 'A2 |  B2  | C2                 *        *', '___|______|_____   *                               *', 'A1 |  B1 *| C1', '   |      |               *                               *', sep='\n') # Draw notation for convenience
print("    *               *                                   *")
print("*")
win = 0 # Lets win message only happen once
stage = 0 # Dictates when the game is in Tic-Tac-Toe stageof game or sliding stage of the game

player = 1 # Says whose turn it is

# For reference in code
notationMapper = {
		'A1' : boardMatrix[2][0],
		'A2' : boardMatrix[1][0],
		'A3' : boardMatrix[0][0],
		
		'B1' : boardMatrix[2][1],
		'B2' : boardMatrix[1][1],
		'B3' : boardMatrix[0][1],
		
		'C1' : boardMatrix[2][2],
		'C2' : boardMatrix[1][2],
		'C3' : boardMatrix[0][2]		
	}

# Draw the board 
def printBoard():
	print(boardMatrix[0])
	print(boardMatrix[1])
	print(boardMatrix[2])
	print('')
	print('')




# "Main" game loop
while True:

	#Dictionary for notation
	notationMapper = {
		'A1' : boardMatrix[2][0],
		'A2' : boardMatrix[1][0],
		'A3' : boardMatrix[0][0],
		
		'B1' : boardMatrix[2][1],
		'B2' : boardMatrix[1][1],
		'B3' : boardMatrix[0][1],
		
		'C1' : boardMatrix[2][2],
		'C2' : boardMatrix[1][2],
		'C3' : boardMatrix[0][2]		
	}

	# Start of the game, specifically stage 0
	if stage == 0:
		#Takes move input and skips turn if there isn't valid input
		try: 
			position = input("Where do you want to play Player " + str(player) + " from [A1 - C3]? " )
			if notationMapper[position] == 0:
				if position == 'A1':
					boardMatrix[2][0] += player
				if position == 'A2':
					boardMatrix[1][0] += player
				if position == 'A3':
					boardMatrix[0][0] += player
		
				if position == 'B1':
					boardMatrix[2][1] += player
				if position == 'B2':
					boardMatrix[1][1] += player
				if position == 'B3':
					boardMatrix[0][1] += player
		
				if position == 'C1':
					boardMatrix[2][2] += player
				if position == 'C2':
					boardMatrix[1][2] += player
				if position == 'C3':
					boardMatrix[0][2] += player
				printBoard()
			else:
				print("Your turn wll be skipped since you selected a score that is not open.")
				
				printBoard() 
		except KeyError:
			print("Try again next time with a valid input Player " + str(player) + ".")
			printBoard()
	
	
	
	
		#Check Tic-Tac-Toes
		
		for i in range(3):
			if abs(sum(boardMatrix[i])) == 3:
				print("Player " + str(int(sum(boardMatrix[i])/3)) + " is the winner! Run program again to play.")
				win+=1
				break
			elif abs(sum([val[i] for val in boardMatrix])) == 3:
				print("Player " + str(int(sum([val[i] for val in boardMatrix])/3)) + " is the winner! Run program again to play again.")
				win+=1
				break
	
		if win == 0:
			if abs(boardMatrix[0][0] + boardMatrix[1][1] + boardMatrix[2][2]) == 3:
				print("Player " + str(int((boardMatrix[0][0] + boardMatrix[1][1] + boardMatrix[2][2])/3)) + " is the winner! Run program to play again.")
				win+=1
			elif abs(boardMatrix[0][2] + boardMatrix[1][1] + boardMatrix[2][0]) == 3:
				print("Player " + str(int((boardMatrix[0][2] + boardMatrix[1][1] + boardMatrix[2][0])/3)) + " is the winner! Run program to play again.")
				win+=1
	
		if win != 0:
			break


		# Lets game proceed to stage 1
		if sum(x.count(0) for x in boardMatrix) == 1:
			stage = 1
			print("its slidin time")
			print('')
			print('Now, we have entered the sliding stage.')
			print('In this stage, you need to choose a node of yours that is connected to the 0 in the grid.')
			print('The center is conected to every other node and the peripheral nodes are connected to their orthogonal neighbors.')
			print('If a valid node is not chosen, the turn will be skipped.')
			print('')
			printBoard()

		player*=-1


	
	if stage == 1:
		

		slideMove = input('What piece do you want to slide Player ' + str(player) + ". ")

		# Checks if slideMove is valid; there is probably a better way to do this.
		if player == notationMapper[slideMove]:
			if slideMove == 'A1':
				if boardMatrix[1][0] == 0:
					boardMatrix[1][0] = player
					boardMatrix[2][0] = 0
					printBoard()

				elif boardMatrix[2][1] == 0:
					boardMatrix[2][1] = player
					boardMatrix[2][0] = 0
					printBoard()

				else:
					print('Next time enter a valid move please, your turn is skipped')
					printBoard()
					
				
			elif slideMove == 'A2':
				if boardMatrix[0][0] == 0:
					boardMatrix[0][0] = player
					boardMatrix[1][0] = 0
					printBoard()

				elif boardMatrix[1][1] == 0:
					boardMatrix[1][1] = player
					boardMatrix[1][0] = 0
					printBoard()

				elif boardMatrix[2][0] == 0:
					boardMatrix[2][0] = player
					boardMatrix[1][0] = 0
					printBoard()

				else:
					print('Next time enter a valid move please, your turn is skipped')
					printBoard()
					
			elif slideMove == 'A3':
				if boardMatrix[0][1] == 0:
					boardMatrix[0][1] = player
					boardMatrix[0][0] = 0
					printBoard()

				elif boardMatrix[1][0] == 0:
					boardMatrix[1][0] = player
					boardMatrix[0][0] = 0
					printBoard()

				else:
					print('Next time enter a valid move please, your turn is skipped')
					printBoard()

			elif slideMove == 'B1':
				if boardMatrix[2][0] == 0:
					boardMatrix[2][0] = player
					boardMatrix[2][1] = 0
					printBoard()

				elif boardMatrix[1][1] == 0:
					boardMatrix[1][1] = player
					boardMatrix[2][1] = 0
					printBoard()

				elif boardMatrix[2][2] == 0:
					boardMatrix[2][2] = player
					boardMatrix[2][1] = 0
					printBoard()

				else:
					print('Next time enter a valid move please, your turn is skipped')
					printBoard()
					
			elif slideMove == 'B2':
				if boardMatrix[2][0] == 0:
					boardMatrix[2][0] = player
					boardMatrix[1][1] = 0
					printBoard()

				elif boardMatrix[1][0] == 0:
					boardMatrix[1][0] = player
					boardMatrix[1][1] = 0
					printBoard()

				elif boardMatrix[0][0] == 0:
					boardMatrix[0][0] = player
					boardMatrix[1][1] = 0
					printBoard()

				elif boardMatrix[2][1] == 0:
					boardMatrix[2][1] = player
					boardMatrix[1][1] = 0
					printBoard()

				elif boardMatrix[0][1] == 0:
					boardMatrix[0][1] = player
					boardMatrix[1][1] = 0
					printBoard()

				elif boardMatrix[2][2] == 0:
					boardMatrix[2][2] = player
					boardMatrix[1][1] = 0
					printBoard()

				elif boardMatrix[1][2] == 0:
					boardMatrix[1][2] = player
					boardMatrix[1][1] = 0
					printBoard()

				elif boardMatrix[0][2] == 0:
					boardMatrix[0][2] = player
					boardMatrix[1][1] = 0
					printBoard()
				#There is no need for a else statement here since it will always find the valid square.
				
			elif slideMove == 'B3':
				if boardMatrix[0][0] == 0:
					boardMatrix[0][0] = player
					boardMatrix[0][1] = 0
					printBoard()

				elif boardMatrix[1][1] == 0:
					boardMatrix[1][1] = player
					boardMatrix[0][1] = 0
					printBoard()

				elif boardMatrix[0][2] == 0:
					boardMatrix[0][2] = player
					boardMatrix[0][1] = 0
					printBoard()

				else:
					print('Next time enter a valid move please, your turn is skipped')
					printBoard()
					

			elif slideMove == 'C1':
				if boardMatrix[2][1] == 0:
					boardMatrix[2][1] = player
					boardMatrix[2][2] = 0
					printBoard()

				elif boardMatrix[1][2] == 0:
					boardMatrix[1][2] = player
					boardMatrix[2][2] = 0
					printBoard()

				else:
					print('Next time enter a valid move please, your turn is skipped')
					printBoard()
					
			elif slideMove == 'C2':
				if boardMatrix[2][2] == 0:
					boardMatrix[2][2] = player
					boardMatrix[1][2] = 0
					printBoard()

				elif boardMatrix[1][1] == 0:
					boardMatrix[1][1] = player
					boardMatrix[1][2] = 0
					printBoard()

				elif boardMatrix[0][2] == 0:
					boardMatrix[0][2] = player
					boardMatrix[1][2] = 0
					printBoard()

				else:
					print('Next time enter a valid move please, your turn is skipped')
					printBoard()
					
			elif slideMove == 'C3':
				if boardMatrix[0][1] == 0:
					boardMatrix[0][1] = player
					boardMatrix[0][2] = 0
					printBoard()

				elif boardMatrix[1][2] == 0:
					boardMatrix[1][2] = player
					boardMatrix[0][2] = 0
					printBoard()

				else:
					print('Next time enter a valid move please, your turn is skipped')
					printBoard()
					
		else: 
			print('Next time enter a valid move please, your turn is skipped')
			printBoard()

		#Check for Tic-Tac-Toe
		for i in range(3):
			if abs(sum(boardMatrix[i])) == 3:
				print("Player " + str(int(sum(boardMatrix[i])/3)) + " is the winner! Run program again to play again.")
				win+=1
				break
			elif abs(sum([val[i] for val in boardMatrix])) == 3:
				print("Player " + str(int(sum([val[i] for val in boardMatrix])/3)) + " is the winner! Run program again to play again.")
				win+=1
				break
	
		if win == 0:
			if abs(boardMatrix[0][0] + boardMatrix[1][1] + boardMatrix[2][2]) == 3:
				print("Player " + str(int((boardMatrix[0][0] + boardMatrix[1][1] + boardMatrix[2][2])/3)) + " is the winner! Run program to play again.")
				win+=1
			elif abs(boardMatrix[0][2] + boardMatrix[1][1] + boardMatrix[2][0]) == 3:
				print("Player " + str(int((boardMatrix[0][2] + boardMatrix[1][1] + boardMatrix[2][0])/3)) + " is the winner! Run program to play again.")
				win+=1
	
		if win != 0:
			break
		
		player*=-1
	

class TicTacToeGames(ABC):
	
	def GeneralTTTInfo(self):
		print("Tic-Tac-Toe style games are games usually played on a square with alternating turns and a goal of getting k-in a row for some k.")
	
	@abstractmethod
	def Rules(self):
		print("Make 3 in a three after alternating turns")

class Achi(TicTacToeGames):
	def Rules(self):
		print("In Achi, there are two stages: the tic-tac-toe stage and the sliding stage. The tic-tac toe stages is just like regular tic-tac-toe. The sliding stage comes only after a drawed positions and involves sliding pieces around to the empty square to get three in a row.")
	
class UltimateTicTacToe(TicTacToeGames):
	def Rules(self):
		print("UltimateTicTacToe is essentially nested tic-tac-toes inside of a tic-tac-toe. This would have 3^4 = 81 square in the grid")


		



print("")
print("Here is some more info:")
achi = Achi()
ulti = UltimateTicTacToe()

achi.GeneralTTTInfo()
achi.Rules()
ulti.Rules()
