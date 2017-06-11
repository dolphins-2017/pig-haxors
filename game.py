from random import randint


goalScore = input("Please enter the score you would like to count up to: ")
player = player1

def game(goalScore, player, turnscore):
	if player == player1:
		turnscore = 0
		turnscore = turn(player, input("It's player 1's turn. Please type 'r' to roll or 'b' to bank: ", turnscore))
		p1totalScore += turnscore
		if p1totalScore >= goalScore:
			return ("Player 1 has won the game with a score of " + str(p1totalScore))
		else:
			player = player2
			return (game(goalScore, player))
	else:
		turnscore = turn(input("It's player 2's turn. Please type 'r' to roll or 'b' to bank: "))
		p2totalScore += turnscore
		if p2totalScore >= goalScore:
			return ("Player 2 has won the game with a score of " + str(p1totalScore))
		else:
			player = player1
			return (game(goalScore, player))

#after each roll prompt user to roll  or bank again
def turn(player, choice, turnscore):
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
			turnscore = "RESET"
			return (game(goalScore, player, turnscore))
		elif randNum1 == 1 or randNum2 == 1:
			print ("You rolled: ", dice)
			print ("Your score for this turn is 0 and your turn is over.")
			turnscore = 0
			return (game(goalScore, player, turnscore))
			
		elif randNum1 == randNum2:
			print ("You rolled: ", dice)
			dicesum = sum(dice)
			print ("Since you rolled 2 of the same number, " + str(dicesum) + " will be added to your score for this turn and you have to roll again.")
			turnscore += dicesum
			return (turn (player, (input("Please type r to roll again: ")), turnscore))

		else:
			print("You rolled: ", dice)
			dicesum = sum(dice)
			turnscore += dicesum
			print ("The score for your turn is now " + str(turnscore))
			return (turn (player, (input("Type r to roll again or b to bank: ")), turnscore))
	else:
		turnscore += dicesum
		return (game(goalScore, player, turnscore))







game(goalScore, player)
