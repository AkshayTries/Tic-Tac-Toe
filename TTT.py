#importing the random module to generate a random number, and time module for watiing
import random, time,os


#these are the global variables
holes = ['Q','W','E','A','S','D','Z','X','C']
magic = {"q":2,"w":7,"e":6,"a":9,"s":5,"d":1,"z":4,"x":3,"c":8}
coordinate = {"q":0,"w":1,"e":2,"a":3,"s":4,"d":5,"z":6,"x":7,"c":8}
rev_coordinate = {0:"q",1:"w",2:"e",3:"a",4:"s",5:"d",6:"z",7:"x",8:"c"}
done = list(range(0,9))	#list of numbers from 0 to 8(inclusive)
human = []
computer = []


def congrats_human():
	time.sleep(1)
	print("\n\n\nYou have won the game. You may proceed to celebrate.")
	time.sleep(2)
	print("\nThanks for playing")	
	time.sleep(2)
	exit()
def congrats_computer():
	time.sleep(1)
	print("\n\n\nThe computer has won the game. Better luck next time")
	time.sleep(2)
	print("\nThanks for playing")
	time.sleep(2)
	exit()


def comp_win_check(computer):
	if all(i in computer for i in [0,1,2]):
		congrats_computer()

	elif all(i in computer for i in [0,3,6]):
		congrats_computer()

	elif all(i in computer for i in [0,4,8]):
		congrats_computer()

	elif all(i in computer for i in [3,4,5]):
		congrats_computer()

	elif all(i in computer for i in [1,4,7]):
		congrats_computer()

	elif all(i in computer for i in [2,4,6]):
		congrats_computer()

	elif all(i in computer for i in [6,7,8]):
		congrats_computer()

	elif all(i in computer for i in [2,5,8]):
		congrats_computer()


def human_win_check(human):
	if all(i in human for i in [0,1,2]):
		congrats_human()

	elif all(i in human for i in [0,3,6]):
		congrats_human()

	elif all(i in human for i in [0,4,8]):
		congrats_human()

	elif all(i in human for i in [3,4,5]):
		congrats_human()

	elif all(i in human for i in [1,4,7]):
		congrats_human()

	elif all(i in human for i in [2,4,6]):
		congrats_human()

	elif all(i in human for i in [6,7,8]):
		congrats_human()

	elif all(i in human for i in [2,5,8]):
		congrats_human()
	

#function for computer to make move
def comp_move(human,computer):
	#os.system("clear")
	rand = random.choice(done)
	computer.append(rand)
	done.remove(rand)
	holes[rand]="O"
	print("\n")
	time.sleep(1.5)
	print("The computer is thinking")
	time.sleep(1)

	for i in range(1,11):
		time.sleep(0.4)
		m = 10*i
		print(m,"%","."*i,end="\r")

	print("\nThe computer has played\n\n")
	time.sleep(0.8)
	board(holes)
	comp_win_check(computer)
	time.sleep(0.8)
	move(human,computer)


#function for player to make move
def move(human,computer):
	m = input("\n\nMake your move: ")
	os.system("clear")
	print("\n")
	holes[coordinate[m.lower()]]="X"
	human.append(coordinate[m.lower()])
	done.remove(coordinate[m.lower()])
	board(holes)
	human_win_check(human)
	comp_move(human,computer)


#function to print the board
def board(holes):
	for i,c in enumerate(holes):
		print(c,end="")
		if i==2 or i==5:
			print("\n-----")
		elif i==8:
			print("")

		else:
			print("|",end="")

time.sleep(1)
print("Let's play Tic Tac Toe")
time.sleep(2.5)
print("\nHere is the board.\n")
board(holes)
time.sleep(2.5)
print("\nPress the corresponding keys on your keyboard to make your move")
holes = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
time.sleep(1)
move(human,computer)






