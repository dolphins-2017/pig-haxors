from random import randint


goalScore = input("Please enter the score you would like to count up to: ")


def game(goalScore):
	p1turnScore = []
	p1totalScore = []
	p2turnScore = []
	p2totalScore = []
	turn(input("It's player 1's turn. Please type 'r' to roll or 'b' to bank: "))

def turn(choice):
	dice = []
	if choice  == "r":
		randNum1 = randint(1,6)
		randNum2 = randint(1,6)
		dice.append(randNum2)
		dice.append(randNum1)
		if (randNum1+randNum2) == 2:
			print("snake eyes!!")
		else:
			print("You rolled: ", dice)
	dicesum = sum(dice)
	print("The turn score is: ", dicesum, "enter 'r' to reroll or 'b' to bank!")
	return dicesum


game(goalScore)
