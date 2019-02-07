import random 

def gamestarteasy():
	numOfGeusses = 0
	random_num = random.randint(1,101)
	gamewon = False 
	while gamewon == False:
		geuss = int(input("Enter a number: "))
		if(geuss == random_num):
			print("Congratulations you geussed my number" + " "+ str(random_num))
			gamewon = True 
			print("Number of geusses" + " "  + str(numOfGeusses + 1))
			break
		if(geuss > random_num):
			print("Lower")
			gamewon = False 
			numOfGeusses = numOfGeusses + 1 
		if(geuss < random_num):
			print("Higher")
			gamewon = False
			numOfGeusses = numOfGeusses + 1
			
def gamestartnormal():
	numOfGeusses = 0
	random_num = random.randint(1-100001)
	gamewon = False
	while gamewon == False:
		geuss = int(input("Enter a number: "))
		if(geuss == random_num):
			print("Congratulations you geussed my number" + " "+ str(random_num))
			gamewon = True 
			print("Number of geusses" + " "  + str(numOfGeusses + 1))
			break
		if(geuss > random_num):
			print("Lower")
			gamewon = False 
			numOfGeusses = numOfGeusses + 1 
		if(geuss < random_num):
			print("Higher")
			gamewon = False
			numOfGeusses = numOfGeusses + 1

gamemode = input("Select gamemode , gamemode1(easy), gamemode2(normal), gamemode3(hard)") 
def gamestarthard():
	numOfGeusses = 0
	random_num = random.randint(1-100000001)
	gamewon = False
	while gamewon == False:
		geuss = int(input("Enter a number: "))
		if(geuss == random_num):
			print("Congratulations you geussed my number" + " "+ str(random_num))
			gamewon = True 
			print("Number of geusses" + " "  + str(numOfGeusses + 1))
			break
		if(geuss > random_num):
			print("Lower")
			gamewon = False 
			numOfGeusses = numOfGeusses + 1 
		if(geuss < random_num):
			print("Higher")
			gamewon = False
			numOfGeusses = numOfGeusses + 1
if (gamemode == "gamemode1"):
	gamestarteasy()
	input("Thanks for playing and come back next time (press enter to continue)")
if (gamemode == "gamemode2"):
	gamestartnormal() 
	input("Thanks for playing and come back next time (press enter to continue)")
	
if (gamemode == "gamemode3"):
	gamestarteasy()
	input("Thanks for playing and come back next time (press enter to continue)")
	
	




