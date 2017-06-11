from random import randint


goalScore = input("Please enter the score you would like to count up to: ")
player = "player1"

def game(goalScore, player):
	if player == "player1":
		p1totalScore = 0
		turnscore = turn(input("It's player 1's turn. Please type 'r' to roll or 'b' to bank: "))
		p1totalScore += turnscore
		if p1totalScore >= int(goalScore):
			return ("Player 1 has won the game with a score of " + str(p1totalScore))
		else:
			return (game(goalScore, player2))
	else:
		p2totalScore = 0
		turnscore = turn(input("It's player 2's turn. Please type 'r' to roll or 'b' to bank: "))
		p2totalScore += turnscore
		if p2totalScore >= int(goalScore):
			return ("Player 2 has won the game with a score of " + str(p1totalScore))
		else:
			return (game(goalScore, player1))

#after each roll prompt user to roll  or bank again
def turn(choice):
	turnOn = True
	turnscore = 0
	dicesum = 0
	while turnOn == True:
		print(turnscore)
		dice = []
		print(dice, dicesum)
		prompt = input("r or b")
		if prompt  == "r":
			notEnd = True
			while notEnd == True:
				randNum1 = randint(1,6)
				randNum2 = randint(1,6)
				dice.append(randNum2)
				dice.append(randNum1)
				# if (randNum1+randNum2) == 2:
				# 	turnscore = 0
				# 	print("Snake eyes!! ", dice)
				# 	notEnd = False
				# 	turnOn = False
				# 	#somehow set total score = to 0
				# elif randNum1 == 1 or randNum2 == 1:
				# 	print("You roled a 1, so your turn is over :( ")
				# 	notEnd = False
				# 	turnOn = False
				# elif randNum1 == randNum2:
				# 	print(dice, "You rolled 2 of the same number, press r to toll again!")
				# 	notEnd = False
				# else:

				print("You rolled: ", dice)
				dicesum = sum(dice)
				turnscore += dicesum
				del dice[:]
				notEnd = False
				
		
		print("The turn score is: ", turnscore)
		dicesum = 0
		if choice == "b":
			turnscore += dicesum
			turnOn = False
	return turnscore








game(goalScore, player)
