# this file should have everyhting the game shows the user

# function to print out the rules 
class View:

	def rules ():
		print ("Welcome to the RPG Monster Game!")
		print ("Just to review these are the rules of the game.")
		print ("First you will build a character, then pick a monster to fight against.")
		print ("Each monster has a different number of lives and different scare value.")
		print ("The fewer lives the monster has, the higher scare value he has and higher chance of hitting you back.")
		print ("You will also be able to choose a weapon class and then you will randomly be assigned a specific weapon from that class")
		print ("Lastly you will fight to the death!")
		print ("Remember: there are last licks!")

	def summary (life, name, gender, fighter, age):
		print (" ")
		print ("Hello there", name.upper())
		print ("Thank you for approving that you are over 18. (Age: ", age, ")")
		print ("Your fighter's name is: ", fighter)
		print ("You currently have ", life, "lives left.")
		print (" ")

	def print_monster_choice(kind, color, scare):
		print ("") 
		print ("You picked", kind, "as your monster!")
		print ("He is", color, "and has a scare value of", scare)
		print ("")

	def pick_monster_again():
		print ("You need to choose 1,2,3 or 4 to pick a monster")

	def end_game ():
		print ("Too bad, maybe next time you will gather enough courage!")

	def print_knife_choice(color, description, harm, kind):
		print ("") 
		print ("You got a",color, description, kind, "!")
		print ("Its has a harm value of", harm)
		print ("")

	def print_weapon_choice(color, description, harm, kind):
		print ("") 
		print ("You got a",color, description, kind, "!")
		print ("Its has a harm value of", harm)
		print ("")

	def pick_weapon_again ():
		print ("You need to pick how to fight your monster!")

	def used_shield(kind):
		print ("Good try but", kind, "used his shield!")

	def take_hit (kind, harm):
		print ("Nice shot! You hit", kind, "with a harm value of", harm)

	def me_take_hit (fighter, scare):
		print ("Oh Man!", fighter, "got hit with a scare value of", scare)
		
	def getting_hit (kind, life):
		print (kind, ": OUCH! I'm hit!")
		print (kind, "has", life, "lives left")

	def hit(color, kind, harm):
		print ("You just used your", color, kind, "Knive!")
		print ("Your Knive has", harm, "harm value")

	def user_wins (kind):
		print ("")
		print (kind, "has no lives left, YOU WIN!") 

	def miss_hit (kind):
		print (kind, "tried to hit you but missed!")

	def hit_char (kind, scare):
		print (kind, "hit you with a scare value of", scare)

	def monster_wins (fighter):
		print ("")
		print (fighter, "has no lives left, YOU LOSE!")

	def start_anyway ():
		print ("Too bad! Your monster is waiting for you and here comes the first shot!")
		print ("")

	def try_again():
		print ("Please enter Yes or No")

	def print_choice_recharge():
		print ("You have left yourself deffense-less and chosen to recharge.") 

	def print_choice_shield():
		print ("You have chosen to shield yourself, you are safe for now.")

	def print_choice_attack():
		print ("You have chosen to attack!!")

	def print_recharged():
		print ("Congradulations, you recharged and did not get hit")	

	def print_quit():
		print ("")
		print ("Quitig...")
		print ("Saving...")	
		print ("Your game has been saved! remmeber to sign in next time to continue your adventure!")

	def print_recharging_hit():
		print ("You got hit while recharging!")

	def information_name ():
		print (" ")
		name = input ("What is your name? ")
		return name
	
	def sign_in():
		while True:
			print (" ")
			sign_in = input ("Do you want to sign in to a previously saved game? (Y or N) ")
			if sign_in.isalpha() == True:
				break
			print ("Please enter Y or N")
		return sign_in

	def information_username():
		while True:
			print (" ")
			username = input ("Please set a username: ")
			if username.isalpha() == True:
				break
			print ("Please enter a word for your username")
		return username

	def information_password():
		while True:
			print (" ")
			password = input ("Please set a password: ")
			if password.isalpha() == True:
				break
			print ("Please enter a word for your password")
		return password

	def information_gender ():
		gender = input ("What is your gender? (M or F) ")
		return gender

	def information_fighter():
		fighter = input ("What would you like to name your fighter? ")
		return fighter

	def information_age ():
		while True:
			age = int(input ("How old are you? "))
			if age > 18:
				break
			print ("Must be 18 or older")
		return age

	def choice_fight ():
		while True:
			choice = input ("How do you want to fight?! -- Pick a knife or a weapon: ")
			choice = choice.lower()
			if choice == "knife" or choice == "weapon":
				break
			print ("Must pick a knife or weapon to fight with!")
		return choice

	def choice_monster ():
		while True:
			choice = input ("Do you want to fight a monster?! (Y or N) ")
			choice = choice.lower()
			if choice == "y" or choice == "n":
				break
			print ("Must enter Y or N!")
		return choice

	def monster_pick ():
		while True:
			user_pick = input("Pick your monster to fight against (1,2,3, 4 or 5) ")
			if user_pick == "1" or user_pick == "2" or user_pick == "3" or user_pick == "4" or user_pick == "5":
				break
			print ("Must enter a choice for a monster!")
		return user_pick

	def choice ():
		choice = input ("Do you want to fight now? (YES or NO) ")
		return choice

	def next_choice ():
		while True:
			print ("")
			print ("What do you want to do next?!")
			choice = input ("Recharge [1], Shield [2], Attack [3], Quit and Save [Q]")

			if choice == "1" or choice == "2" or choice == "3" or choice == "Q" or choice == "q":
				break
			print("You need to pick a next move!")
		return choice






