
def standing_stones():
	print "After walking a ways, you come into a mysitcal circle of standing stones."
	print "They're creeping you out."
	print "You feel a strange power."
	print "Should you leave, or go approach the stones?"
	circle = raw_input("> ")

	if circle == "leave":
		copse()
	else:
		dead("The stones got you, you travel through time but are ripped apart in the processs.")

def faerie_riddle():
	print "The faeries are impressed you stayed, and they give you a riddle."
	print "A house has 4 walls that all point south, \nthere is a bear circling the house, \n what color is the bear?"
	print "A: Black \nB: White \nC: Brown \nD: Blue"
	bear_color = raw_input("> ")
	if bear_color == "B" or bear_color == "b":
		print "You black out."
		start()
	else:
		dead("Whoops, you were wrong. You died.")

def copse():
	print "After some trekking, you walk into a beautiful copse."
	print "Suddenly, some faeries appear."
	print "They give you a chance to leave or stay. Which do you choose?"
	choice = raw_input("> ")

	if choice == "stay":
		faerie_riddle()
	elif choice == "leave":
		dead("The faeries attack and kill you. Who knew such creatures were so violent?")
	else:
		dead("Your silence enrages the faeries, who then kill you.")

def kicked_out():
	print "The wife kicks you out. Looks like you're walking again."
	print "Which way do you go?"
	direction2 = raw_input("Left or right? \n> ")

	if direction2 == "Left" or direction2 == "left":
		copse()
	elif direction2 == "Right" or direction2 == "right":
		standing_stones()
	else:
		dead("You're too indecisive. You starve.")

def wife_question():
	print "The woman looks at you funny."
	print "She asks \"Are you waiting for something?\""
	answer = raw_input("Y/N/IDK \n> ")

	if answer == "Y" or answer == "y":
		dead("You see the fear in her eyes before she smacks you with a pan.")
	elif answer == "N" or answer == "n":
		kicked_out()
	else:
		"She eyes you suspiciously, and says \"Then you've got no business being here!\""
		kicked_out()

def sheep_shack():
	print "You knock on the door, and a woman answers."
	print "She's suspicous, but she lets you insdie."
	print "What do you do when you get in?"

	inside = raw_input("Check out the stove, or sit at the table? \n > ")

	if inside == "stove":
		dead("The farmers wife checks you over the head with a frying pan when you're not looking.")
	elif inside == "table":
		wife_question()
	else:
		dead("You die while you wait to decide. The farmer's wife dies, too. Rats.")

def sheep_farm():
	print "You walk for awhile, and you come upon a sheep farm."
	print "Should you knock on the door (A) or go pet the sheep (B)?"

	decision = raw_input("> ")

	if decision == "A" or decision == "a":
		sheep_shack()
	elif decision == "B" or decision == "b":
		dead("The farmer found you, and thought you were stealing his sheep. He shoots you. Bummer.")
	else:
		print "Pick something!"
		sheep_farm()

def dead(why):
	print why, "\nThe end."
	exit(0)

def start():
	print "You wake up on a foggy Scottish moor."
	print "Isn't this a nice chage from always waking up in a dungeon?"
	print "Anyway."
	print "It's really foggy out. Scotland, amirite?"
	print "Which way do you want to go? Left, right, or forward?"

	direction = raw_input("> ")

	if direction == "left":
		sheep_farm()
	elif direction == "right":
		standing_stones()
	elif direction == "forward":
		copse()
	else:
		print "Go somewhere, forreal."
		start()

start()	
