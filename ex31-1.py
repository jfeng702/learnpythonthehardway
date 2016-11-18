print "You come to a clearing with 2 paths. Do you take path 1 or 2?"

choice = raw_input("> ")

if choice == "1":
    print "You take the left path and die"

elif choice == "2":
        print "you come across a bear. What do you do?"
        print "1. Bitch slap it across the face."
        print "2. Run away."

        bear = raw_input("> ")

        if bear == "1":
            print "You slap him and he runs away."
        elif bear == "2":
            print "He chases you down and eats you."
