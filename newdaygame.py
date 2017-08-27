print "Good morning! How would you like to start your day?"
print "Go to the kitchen (1) or go to the bathroom (2)?"

first = raw_input("> ")

if first == "1":
	print "Yum, you're making breakfast!"
	print "What would you like to make first?"
	print "1. Coffee."
	print "2. Toast."
	print "3. Eggs."
	breakfast = raw_input("> ")
	if breakfast == "1":
		print "Good choice. Everyone needs some Joe."
		print "Now what would you like to do?"
		print "Go to the bathroom (1) or keep making breakfast (2)?"
		next = raw_input("> ")
		if next == "1":
			print "You walk over to the bathroom but your cat trips you."
			print "You fall to your death."
			print "Damn cat."
		elif next == "2":
			print "What would you like to make next?"
			print "1. Toast."
			print "2. Eggs."
			food = raw_input("> ")
			if food == "1":
				print "You pop the toast in the toaster, but you electrocute yourself."
				print "That was clumsy."
			elif food == "2":
				print "Look at you, getting your protein."
				print "How do you like your eggs?"
				print "1. Scrambled"
				print "2. Fried"
				egg = raw_input("> ")
				if egg == "1":
					print "You don't have any cheese. That's a bummer."
					print "You starve."
				elif egg == "2":
					print "Fried eggs are bad for you."
					print "Your cholesterol is too high. You die."
				else:
					print "That's disgusting!"
			else:
				print "That's disgusting!"
		else:
			print "You walked outside in your underwear. Bad call."
	elif breakfast == "2":
		print "You pop the toast in the toaster, but you electrocute yourself."
		print "That sucks."
	elif breakfast == "3":
		print "Look at you getting your protein."
		print "How do you like your eggs?"
		print "1. Scrambled"
		print "2. Fried"
		egg1 = raw_input("> ")
		if egg1 == "1":
			print "You don't have any cheese. That's a bummer."
			print "Guess you'll have to starve."
		elif egg1 == "2":
			print "Fried is bad for you."
			print "Your cholesterol is too high. You die."
		else:
			print "That's disgusting!"
	else:
		print "That's disgusting!"
elif first == "2":
	print "You walk down the hall to the bathroom."
	print "You cat appears out of nowhere."
	print "Do you:"
	print "1. Keep walking"
	print "2. Pet her"
	response = raw_input("> ")
	if response == "1":
		print "You trip over her and break your neck."
		print "That's what you get for being so rude."
	elif response == "2":
		print "She purrs while you pet her (this is an ideal world after all)."
		print "She moves around a little, do you follow her?"
		print "Y/N"
		follow = raw_input("> ")
		if follow == "Y":
			print "You follow her into your room."
			print "It's a trap. Why would you ever trust a cat."
		elif follow == "N":
			print "She'll figure herself out."
			print "You continue into the bathroom."
			print "What do you want to do here?"
			print "1. Shower 2. Brush your teeth 3. Admire yourself in the mirror"
			bathroom = raw_input("> ")
			if bathroom == "1":
				print "You slip on the tub and fall to your death. Bummer."
			elif bathroom == "2":
				print "You're out of toothpaste."
				print "How did you manage that?"
				print "What do you want to do instead?"
				print "1. Leave bathroom 2. Brush anyway"
				teeth = raw_input("> ")
				if teeth == "1":
					print "You trip over the cat, who was walking in the hall."
					print "You fall to your death. Bummer."
				elif teeth == "2":
					print "That's disgusting. You get a gum infection and die."
				else:
					print "That's disgusting."
			elif bathroom == "3":
				print "You're such a narcicist. Disgusting."
				print "The mirror shatters and you die."
			else:
				print "That's disgusting. Go home."
else:
	print "That's not an option. You failed."
