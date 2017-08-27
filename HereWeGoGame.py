#define the way the game ends
def death(why):
    print why, "\nNow what? \n1. Continue \n2. Start over \n3.Exit"
    decision = raw_input("> ")
    decision = decision.strip()

    if decision == "1":

    elif decision == "2":
        start()
    elif decision == "3":
        print "Thanks for playing. \nGoodbye."
    else:
        print "I didn't get that."
        death("So, you've just died.")

#----------------------------------------------------#

def defense():
    print "yay"

def strength():
    print "To start, what is your strength?"
    strength = raw_input("> ")
    strength = int(strength)

    if strength <= 2 and pick == "sword":
        print "You can't even hold your sword up, doofus. \nTry again."
        strength()
    elif strength <=2 and pick == "shield":
        print "Shields are heavy. You might want to be stronger. \nTry again."
        strength()
    elif strength > 2:
        print "Nice."
        defense()
    else:
        print "Nope, sorry, didn't get that."
        strength()

def stats_intro():
    print "Now let's pick some stats, like any good ~realistic~ game."
    print "Stats are out of 10."
    print "You have 10 points to give."
    strength()

def question():
    print "%s, what would you like first, a shield or a sword?" % name
    pick = raw_input("> ")
    pick = pick.lower()
    pick = pick.strip()

    if pick == "sword":
        print "Good, then you shall have your sword."
        stats_intro()
    elif pick == "shield":
        print "You're wise to defend yourself."
        stats_intro()
    elif pick == "sheild":
        print "You're wise to defend yourself."
        stats_intro()
    else:
        print "Don't be silly, that's not an option."
        question()

def castle_arrival():


def dialogue2():
    print "'Are you a loyal son of the empire? Or a true patriot?'"
    print "1. Empire \n2. Patriot"
    side = raw_input("> ")

    if side == "1":
        print "'Nevermind, you scum.' \nHe spits on your boots. \nRude."
        castle_arrival()
    elif side == "2":
        print "'A true patriot. You will find glory in afterlife, my friend.'"
        castle_arrival()
    else:
        print "'What was that?'"
        dialogue2()

def dialogue1():
    print "You decide to talk to this dude."
    print "You greet him."
    print "'So we're all going to our deaths together. Very poetic.'"
    dialogue2()

def akward():
    print "You side eye him."
    print "He approaches you anyway. \nRude."
    dialogue2()


###GAME START
def start():
    print "Greetings, friend. \nWe have much to discuss. \nBut first,"
    print "what is your name?"
    name = raw_input("> ")
    name = name.strip()
    print "...%s \n...interesting." % name

    print "Well %s you're on your way to be executed by the Empire" % name
    print "Doesn't look very good for you."
    print "You're being transported, and another prisoner approaches you."
    print "'Hey,'"
    print "Do you want to talk to him? \nY/N"
    talk = raw_input("> ")
    talk.upper()
    if talk == "Y":
        dialogue1()
    elif talk == "N":
        awkward()
    else:
        print "No, really, you have to make a decision here."
        print "He's really eyeing you up."


# okay I can't seem to make funcitons that don't call on functions that I can only define later
# how do I get around this ...
