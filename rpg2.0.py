# rpg Monster Game 
# this file should have all working parts of the game 

# totally working game
# still need to be able to save the changes to the db when a player quits and set up the FK so they can log back in with the same info

import random 
import sys
from rpg_view import View

from rpg_model import CharacterModel 
from rpg_model import MonsterModel 
from rpg_model import WeaponModel 

# Creating the character's characteristics from the user
class Character:
	life = 5

	# no init function, all the attributes are given using input statments     
	def start(self):
		View.rules ()
		View.sign_in()
		print (" ")
		name = View.information_name()
		gender = View.information_gender()
		self.fighter = View.information_fighter()
		age = View.information_age()
		self.life = 5
		username = View.information_username()
		password = View.information_password()

		# this puts all the users info in the database 
		CharacterModel.insert(self.life, name, gender, self.fighter, age, username, password)
		CharacterModel.print_info()
		View.summary(self.life, name, gender, self.fighter, age) 

	# method to take damage when they are fighting 
	def take_damage(self):
		View.getting_hit (self.fighter, self.life)
		self.life -= 1
		# make sure to upate the life in the database
		# CharacterModel.update_life(life)

character1 = Character()
character1.start()

# Creating the monsters with classes 
class Monster:
	limbs = 4
	def __init__(self, color, life, scare, kind, id_num):
		self.color = color
		self.life = life
		self.scare = scare
		self.kind = kind
		self.id_num = id_num

	def take_damage(self):
		View.getting_hit (self.kind, self.life)
		self.life -= 1

mike = Monster("Green", 2,8, "Mike Wazowski", 1)
boo = Monster("Human", 4,6, "Boo", 2)
james = Monster("Blue", 6,4, "James Sullivan", 3)
randall = Monster("Purple", 8,2, "Randall", 4)
ninja = Monster ("RED", 5,5, "Ginja Ninja", 5)

# function for the user to pick their monster 
def pick_monster (mike, boo, james, randall):
	choice = (View.choice_monster())

	if choice == "y" or choice == "Y":
		user_pick = (View.monster_pick()).lower()

		if user_pick == "1":
			View.print_monster_choice(mike.kind,mike.color, mike.scare)
			return mike
		elif user_pick == "2":
			View.print_monster_choice(boo.kind,boo.color, boo.scare)
			return boo
		elif user_pick == "3":
			View.print_monster_choice(james.kind, james.color, james.scare)
			return james
		elif user_pick == "4":
			View.print_monster_choice(randall.kind, randall.color, randall.scare)
			return randall
		elif user_pick == "5":
			View.print_monster_choice(ninja.kind, ninja.color, ninja.scare)
			return ninja
		else:
			View.pick_monster_again()
			sys.exit()
	else:
		View.end_game()
		sys.exit ()

user_monster = pick_monster (mike, boo, james, randall)
# save the monster pick to the db
MonsterModel.insert(user_monster.color, user_monster.life, user_monster.scare, user_monster.kind, user_monster.id_num)
MonsterModel.print_info()
MonsterModel.update_monster(user_monster.id_num)

# create weapon categories with classes 
class Knives:
	def __init__(self, color, description, harm, kind, id_num):
		self.color = color
		self.description = description
		self.harm = harm 
		self.kind = kind
		self.id_num = id_num
	def hit(self):
		View.hit (self.color, self.kind, self.harm)

dagger = Knives("Black", "Sharp", 1, "Dagger",1)
sword = Knives("Black", "Sharp", 2, "Sword",2)

class Weapons:
	def __init__(self, color, description, harm, kind, id_num):
		self.color = color
		self.kind = kind
		self.harm = harm
		self.description = description
		self.id_num = id_num
	def hit(self):
		View.hit (self.color, self.kind, self.harm)

sling_shot = Weapons("Brown", "Harmfull", 1, "Sling Shot", 3)
bow_arrow = Weapons("Brown", "Harmfull", 2, "Bow and Arrow", 4)


# function for the player to pick weappon class then randomly get assigned a weapon 
def pick_weapon (dagger, sword, sling_shot, bow_arrow):
	choice = (View.choice_fight())
	roll = random.random()

	if choice == "knife":
		if roll >= .5:
			View.print_knife_choice (dagger.color, dagger.description, dagger.harm, dagger.kind)
			return dagger
		else:
			View.print_knife_choice (sword.color, sword.description, sword.harm, sword.kind)
			return sword
	elif choice == "weapon":
		if roll >= .5:
			View.print_weapon_choice (sling_shot.color, sling_shot.description, sling_shot.harm, sling_shot.kind)
			return sling_shot
		else:
			View.print_weapon_choice (bow_arrow.color, bow_arrow.description, bow_arrow.harm, bow_arrow.kind)
			return bow_arrow
	else:
		View.pick_weapon_again()
		user_weapon = pick_weapon (dagger, sword,sling_shot, bow_arrow)
		return user_weapon

user_weapon = pick_weapon (dagger, sword,sling_shot, bow_arrow)
# save the weapon pick to the db
WeaponModel.insert(user_weapon.color, user_weapon.kind, user_weapon.harm, user_weapon.description, user_weapon.id_num)
WeaponModel.print_info()
WeaponModel.update_weapon(user_weapon.id_num)
# print (user_weapon.id_num)

# for testing
# CharacterModel.print_keys()


# create if statments for the battle, create random rolls, add if statmentd for shield
# use the take dammage and scare values for stats 
# function to play the game, you hit monster then monster hits you
def play_game_monster (user_weapon, user_monster, Monster, Character, character1):
	roll = random.random()

	while user_monster.life > 0:
		if user_weapon.harm == 1:
			if roll > .5:
				View.used_shield (user_monster.kind)
			else:
				user_monster.take_damage()
				View.take_hit (user_monster.kind, user_weapon.harm)
		elif user_weapon.harm == 2:
			if roll > .5:
				View.used_shield (user_monster.kind)
			else:
				user_monster.take_damage()
				user_monster.take_damage()
				View.take_hit (user_monster.kind, user_weapon.harm)

		play_game_character (user_weapon, user_monster, Monster, Character, character1)
	else:
		View.user_wins(user_monster.kind)
		sys.exit()

# choose the next move that you make to the monster
def next_move():
	choice = View.next_choice()
	roll = random.random()

	if choice == "1":
		View.print_choice_recharge ()
		if roll > .5:
			View.print_recharged()
			# add a life to the character
		else:
			View.print_recharging_hit()
			character1.take_damage()
			View.me_take_hit (character1.fighter, user_monster.scare)
	elif choice == "2":
		View.print_choice_shield()
		next_move ()
	elif choice == "3":
		View.print_choice_attack()
		play_game_monster (user_weapon, user_monster, Monster, Character, character1)
	elif choice == "Q" or choice == "q":
		View.print_quit()
		# need to update all the data and save it
		sys.exit()

	play_game_character (user_weapon, user_monster, Monster, Character, character1)

# Monsters with fewer lives have higher scare values, higher scare values give them higher chances to hit you
def play_game_character (user_weapon, user_monster, Monster, Character, character1):
	roll = random.random()

	while character1.life > 0:
		if user_monster.scare == 2:
			if roll > .3:
				View.miss_hit (user_monster.kind)
			else:
				character1.take_damage()
				View.me_take_hit (character1.fighter, user_monster.scare)
		if user_monster.scare == 4:
			if roll > .4:
				View.miss_hit (user_monster.kind)
			else:
				character1.take_damage()
				View.me_take_hit (character1.fighter, user_monster.scare)
		if user_monster.scare == 6:
			if roll > .6:
				View.miss_hit (user_monster.kind)
			else:
				character1.take_damage()
				View.me_take_hit (character1.fighter, user_monster.scare)
		if user_monster.scare == 8:
			if roll > .7:
				View.miss_hit (user_monster.kind)
			else:
				character1.take_damage()
				View.me_take_hit (character1.fighter, user_monster.scare)

		next_move ()
		# play_game_monster (user_weapon, user_monster, Monster, Character, character1)
	else:
		View.monster_wins (character1.fighter)    
		sys.exit()

# funtion to initiate the other play functions 
def play ():
	choice = (View.choice())

	if choice == "yes":
		next_move ()
		# play_game_monster (user_weapon, user_monster, Monster, Character, character1)
	elif choice == "no":
		View.start_anyway()
		next_move()
		# play_game_monster (user_weapon, user_monster, Monster, Character, character1)
	else:
		View.try_again()
		play ()

play ()













'''
Jacks-MacBook-Pro-2:rpg_mVC JackAAnteby$ python3 rpg_controller.py 
Welcome to the RPG Monster Game!
Just to review these are the rules of the game.
First you will build a character, then pick a monster to fight against.
Each monster has a different number of lives and different scare value.
The fewer lives the monster has, the higher scare value he has and higher chance of hitting you back.
You will also be able to choose a weapon class and then you will randomly be assigned a specific weapon from that class
Lastly you will fight to the death!
Remember: there are last licks!
 
 
What is your name?jack
What is your gender? (M or F)m
What would you like to name your fighter?killer
How old are you?0
Must be 18 or older
How old are you?89
 
Hello there JACK
Thank you for approving that you are over 18. (Age:  89 )
Your fighter's name is:  killer
You currently have  5 lives left.
 
Do you want to fight a monster?! (Y or N)j
Must enter Y or N!
Do you want to fight a monster?! (Y or N)y
Pick your monster to fight against (1,2,3 or 4)8
Must enter a choice for a monster!
Pick your monster to fight against (1,2,3 or 4)3

You picked James Sullivan as your monster!
He is Blue and has a scare value of 4

How do you want to fight?! -- Pick a knife or a weapon.k
Must pick a knife or weapon to fight with!
How do you want to fight?! -- Pick a knife or a weapon.weapon

You got a Brown Harmfull Sling Shot !
Its has a harm value of 1

Do you want to fight now? (YES or NO)j
Please enter Yes or No
Do you want to fight now? (YES or NO)no
Too bad! Your monster is waiting for you and here comes the first shot!
Good try but James Sullivan used his shield!
James Sullivan tried to hit you but missed!
James Sullivan : OUCH! I'm hit!
James Sullivan has 6 lives left
Nice shot! You hit James Sullivan with a harm value of 1
killer : OUCH! I'm hit!
killer has 5 lives left
Oh Man! killer got hit with a scare value of 4
Good try but James Sullivan used his shield!
James Sullivan tried to hit you but missed!
Good try but James Sullivan used his shield!
killer : OUCH! I'm hit!
killer has 4 lives left
Oh Man! killer got hit with a scare value of 4
James Sullivan : OUCH! I'm hit!
James Sullivan has 5 lives left
Nice shot! You hit James Sullivan with a harm value of 1
James Sullivan tried to hit you but missed!
Good try but James Sullivan used his shield!
James Sullivan tried to hit you but missed!
Good try but James Sullivan used his shield!
killer : OUCH! I'm hit!
killer has 3 lives left
Oh Man! killer got hit with a scare value of 4
Good try but James Sullivan used his shield!
James Sullivan tried to hit you but missed!
Good try but James Sullivan used his shield!
James Sullivan tried to hit you but missed!
Good try but James Sullivan used his shield!
James Sullivan tried to hit you but missed!
James Sullivan : OUCH! I'm hit!
James Sullivan has 4 lives left
Nice shot! You hit James Sullivan with a harm value of 1
James Sullivan tried to hit you but missed!
James Sullivan : OUCH! I'm hit!
James Sullivan has 3 lives left
Nice shot! You hit James Sullivan with a harm value of 1
killer : OUCH! I'm hit!
killer has 2 lives left
Oh Man! killer got hit with a scare value of 4
Good try but James Sullivan used his shield!
James Sullivan tried to hit you but missed!
James Sullivan : OUCH! I'm hit!
James Sullivan has 2 lives left
Nice shot! You hit James Sullivan with a harm value of 1
killer : OUCH! I'm hit!
killer has 1 lives left
Oh Man! killer got hit with a scare value of 4
James Sullivan : OUCH! I'm hit!
James Sullivan has 1 lives left
Nice shot! You hit James Sullivan with a harm value of 1

killer has no lives left, YOU LOSE!
Jacks-MacBook-Pro-2:rpg_mVC JackAAnteby$ 
'''

'''
Jacks-MacBook-Pro-2:rpg_mVC JackAAnteby$ python3 rpg_controller.py 
Welcome to the RPG Monster Game!
Just to review these are the rules of the game.
First you will build a character, then pick a monster to fight against.
Each monster has a different number of lives and different scare value.
The fewer lives the monster has, the higher scare value he has and higher chance of hitting you back.
You will also be able to choose a weapon class and then you will randomly be assigned a specific weapon from that class
Lastly you will fight to the death!
Remember: there are last licks!
 
 
What is your name?emily
What is your gender? (M or F)f
What would you like to name your fighter?ginga ninja
How old are you?21
 
Hello there EMILY
Thank you for approving that you are over 18. (Age:  21 )
Your fighter's name is:  ginga ninja
You currently have  5 lives left.
 
Do you want to fight a monster?! (Y or N)yes
Must enter Y or N!
Do you want to fight a monster?! (Y or N)y
Pick your monster to fight against (1,2,3 or 4)3

You picked James Sullivan as your monster!
He is Blue and has a scare value of 4

How do you want to fight?! -- Pick a knife or a weapon.weapon

You got a Brown Harmfull Bow and Arrow !
Its has a harm value of 2

Do you want to fight now? (YES or NO)yes

What do you want to do next?!
Recharge [1], Shield [2], Attack [3]3
You have chosen to attack!!
James Sullivan : OUCH! I'm hit!
James Sullivan has 6 lives left
James Sullivan : OUCH! I'm hit!
James Sullivan has 5 lives left
Nice shot! You hit James Sullivan with a harm value of 2
ginga ninja : OUCH! I'm hit!
ginga ninja has 5 lives left
Oh Man! ginga ninja got hit with a scare value of 4

What do you want to do next?!
Recharge [1], Shield [2], Attack [3]3
You have chosen to attack!!
James Sullivan : OUCH! I'm hit!
James Sullivan has 4 lives left
James Sullivan : OUCH! I'm hit!
James Sullivan has 3 lives left
Nice shot! You hit James Sullivan with a harm value of 2
James Sullivan tried to hit you but missed!

What do you want to do next?!
Recharge [1], Shield [2], Attack [3]2
You have chosen to shield yourself, you are safe for now.

What do you want to do next?!
Recharge [1], Shield [2], Attack [3]3
You have chosen to attack!!
James Sullivan : OUCH! I'm hit!
James Sullivan has 2 lives left
James Sullivan : OUCH! I'm hit!
James Sullivan has 1 lives left
Nice shot! You hit James Sullivan with a harm value of 2
James Sullivan tried to hit you but missed!

What do you want to do next?!
Recharge [1], Shield [2], Attack [3]3
You have chosen to attack!!

James Sullivan has no lives left, YOU WIN!
Jacks-MacBook-Pro-2:rpg_mVC JackAAnteby$ 
'''