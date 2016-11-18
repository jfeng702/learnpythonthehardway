def girl():
    print " you saved the girl"
    print "what do you do?"
    choice = raw_input("> ")

    if "marry" in choice:
        print "You marry her and win"
    else:
        print "You suck"

def godzilla():
    print "You come across Godzilla"
    print "What do you do?"
    choice = raw_input("> ")

    if choice == "fight":
        girl()
    elif choice == "run":
        print "you run away but die anyway"
    else:
        print "You die"

def start():
    print "You come across three doors"
    print "Which one do you choose?"
    choice = raw_input("> ")

    if choice == "1":
        godzilla()
    elif choice == "2":
        print "You die"
    else:
        print "You die"

start()
