from random import randint


goalScore = input("Please enter the score you would like to count up to: ")
player = player1

def game(player):
	if player == player1:
		turnscore = turn(input("It's player 1's turn. Please type 'r' to roll or 'b' to bank: "))
		p1totalScore += turnscore
	else:
		turnscore = turn(input("It's player 2's turn. Please type 'r' to roll or 'b' to bank: "))
		p2totalScore += turnscore


	print(p1totalScore)

#after each roll prompt user to roll  or bank again
def turn(choice):
	turnOn = True
	while turnOn == True:
		turnscore = 0
		dice = []
		dicesum = 0
		if choice  == "r":
			notEnd = True
			while notEnd == True:
				randNum1 = randint(1,6)
				randNum2 = randint(1,6)
				dice.append(randNum2)
				dice.append(randNum1)
				if (randNum1+randNum2) == 2:
					notEnd = False
					print("Snake eyes!! ", dice)
					turnOn = False
					#somehow set total score = to 0
				elif randNum1 == 1 or randNum2 == 1:
					turnscore = 0
					notEnd = False
					turnOn = False
				elif randNum1 == randNum2:
					turnscore += dicesum
					#can't bank: print(You rolled 2 of the same number, press r to toll again!)

				else:
					print("You rolled: ", dice)
					dicesum = sum(dice)
					turnscore += dicesum
					notEnd = False
		print("The turn score is: ", dicesum)

		else:
			turnscore += dicesum
			turnOn = False
	return turnscore






game(goalScore)
