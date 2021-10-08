import random
import time
import os

#sets the variable "var" to a number between 1 and 5000
var = random.randrange(1, 5000)

#intro
print("Welcome To The Random Number Game")
print("Pick A Number Between 1 And 5000")
print("Please wait 5 seconds while we get everything ready")

#progress (just for fun)
count = 0
while (count < 5):
	time.sleep(1)
	count = count + 1
	if count == 1:
		print("20%")
	if count == 2:
		print("40%")
	if count == 3:
		print("60%")
	if count == 4:
		print("80%")
	if count == 5:
		print("100% Have Fun Guessing")

#gets the user input and compares it to the variable "var" that we set earlier
while True:
	time.sleep(0.9)
	os.system("clear")
	ans = int(input("Whats Your Guess: "))

	if ans > var:
		print("Too High")

	if ans < var:
		print("Too Low")

	if ans == var:
		print("CONGRATULATIONS YOU WON")
		quit()
