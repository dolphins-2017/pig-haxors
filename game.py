from random import randint


goalScore = int(input("Please enter the score you would like to count up to: "))
player = "player1"
turnscore = 0
p1totalScore = 0
p2totalScore = 0


def game(goalScore, player, turnscore,p1totalScore,p2totalScore):
	if player == "player1":
		if turnscore == "SNAKE EYES":
			p1totalScore = 0
			turnscore = 0
			player = "player2"
			return (game(goalScore, player, turnscore, p1totalScore, p2totalScore))
		elif turnscore == "ONE 1":
			turnscore = 0
			p1totalScore += turnscore
			player = "player2"
			return (game(goalScore, player, turnscore, p1totalScore, p2totalScore))
		elif turnscore == 0:
			choice = input("It's player 1's turn. Please type 'r' to roll or 'b' to bank: " )
			return turn(player, choice, turnscore, p1totalScore, p2totalScore)
		else:
			p1totalScore += turnscore
			if p1totalScore >= goalScore:
				return ("Player 1 has won the game with a score of " + str(p1totalScore))
			else: 
				turnscore = 0
				player = "player2"
				return (game(goalScore, player, turnscore, p1totalScore, p2totalScore))
	elif player == "player2":
		if turnscore == "SNAKE EYES":
			p2totalScore = 0
			turnscore = 0
			player = "player1"
			return (game(goalScore, player, turnscore, p1totalScore, p2totalScore))
		elif turnscore == "ONE 1":
			turnscore = 0
			p2totalScore += turnscore
			player = "player1"
			return (game(goalScore, player, turnscore, p1totalScore, p2totalScore))
		elif turnscore == 0:
			choice = input("It's player 2's turn. Please type 'r' to roll or 'b' to bank: ")
			return turn(player, choice, turnscore, p1totalScore, p2totalScore)
		else:
			p2totalScore += turnscore
			if p2totalScore >= goalScore:
				return ("Player 2 has won the game with a score of " + str(p2totalScore))
			else: 
				turnscore = 0
				player = "player1"
				return (game(goalScore, player, turnscore, p1totalScore, p2totalScore))

def turn(player, choice, turnscore, p1totalScore, p2totalscore):

	dice = []
	dicesum = 0
	if choice  == "r":
		randNum1 = randint(1,6)
		randNum2 = randint(1,6)
		dice.append(randNum2)
		dice.append(randNum1)
		if (randNum1+randNum2) == 2:
			print("Snake eyes!! ", dice)
			print ("Your total score will be reset to 0 and your turn is over.")
			turnscore = "SNAKE EYES"
			return (game(goalScore, player, turnscore, p1totalScore, p2totalScore))
		elif randNum1 == 1 or randNum2 == 1:
			print ("You rolled: ", dice)
			print ("Your score for this turn is 0 and your turn is over.")
			turnscore = "ONE 1"
			return (game(goalScore, player, turnscore, p1totalScore, p2totalScore))
			
		elif randNum1 == randNum2:
			print ("You rolled: ", dice)
			dicesum = sum(dice)
			print ("Since you rolled 2 of the same number, " + str(dicesum) + " will be added to your score for this turn and you have to roll again.")
			turnscore += dicesum
			return (turn (player, (input("Please type r to roll again: ")), turnscore, p1totalScore, p2totalScore))

		else:
			print("You rolled: ", dice)
			dicesum = sum(dice)
			turnscore += dicesum
			print ("The score for your turn is now " + str(turnscore))
			return (turn (player, (input("Type r to roll again or b to bank: ")), turnscore, p1totalScore, p2totalScore))
	else:
		turnscore += dicesum
		return (game(goalScore, player, turnscore, p1totalScore, p2totalScore))






game(goalScore, player, turnscore, p1totalScore, p2totalScore)
