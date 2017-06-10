from random import randint


goalScore = input("Please enter the score you would like to count up to: ")


def game(goalScore):
	p1turnScore = []
	p1totalScore = []
	p2turnScore = []
	p2totalScore = []
	p1totalScore.append(turn(input("It's player 1's turn. Please type 'r' to roll or 'b' to bank: ")))
	print(p1totalScore)

def turn(choice):
	turnOn = True
	while turnOn == True:
		turnscore = [0]
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

				else:
					print("You rolled: ", dice)
					dicesum = sum(dice)
					turnscore.append(dicesum)
					notEnd = False
		print("The turn score is: ", dicesum)
		if choice == "b":
			turnOn = False
	return sum(turnscore)






game(goalScore)
