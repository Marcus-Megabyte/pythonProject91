# Greet the user and provide instructions
print(f"Greeting audiences! I want to tell you a story about a dog going vacation. ")
print(f"Before we start the story I want to let you know that you are in control of the outcome of the story.   ")
print(f"After answering the question, make sure that you press the  press the enter key.  ")
print(f"This dog is a family type he like doing fun things with the kids and sleep in the parents bed at night. ")
print(f"The family dog had been working around the clock to to make sure that the owners and kids are safe from danger")
print(f"One day the dog over heard the parents was planning to go a vacation next week for spring break with the kids.")
print(f"At first the dog was over joy to hear that they was going on a trip. ")
print(f"But sadly the parents chose not to take the dog with them. ")
print(f"This left a hugh hole in the dog heart while the dog was going back to it bed. ")
print(f"The dog thought of an idea of how to change the owner mind of bring it along.")
print(f"The dog walk in the owner room to sit in front of them and beg to go on the trip. ")
print(f"The owners look confuse on the dog is asking for. ")
print(f"They assume that the dog want to go outside but that wasn't it. ")
print(f"They thought the dog was hungry but that wasn't it either. ")
print(f"The dog was trying to see how to tell them he want to go on the trip. ")
print(f"The dog went to their suitcase to show the owner what he really want. ")
print(f"After hours of thinking over the owner knew just what the dog wanted to get their attention for all along.")
print(f"The man call the dog over and say sure buddy you can come with us on the trip. ")
print(f"The day had come for the family to go on their long awaited spring break vacation. ")
input(f"\nPress enter to continue...")

keepPlaying = "yes"
while keepPlaying.lower() == "yes":

    # First Questions Before we start story
    breed = input(f"\nWhat kind of breed is the dog:  ")
    while len(breed) == 0:
        breed = input(f"please enter a breed:  ")
    # Second Questions
    name = input(f"What name is the {breed}:  ")
    while len(name) == 0:
        name = input(f"please enter a name:  ")
    # Third Question
    dadName = input(f"\nWhat is the dad name: ")
    while len(dadName) == 0:
        dadName = input(f"Please enter the dad name: ")
    # Forth Question
    momName = input(f"\nWhat is the mom name: ")
    while len(momName) == 0:
        momName = input(f"Please enter the mom name: ")
    # Fifth Question
    sonName = input(f"\nWhat is the son name: ")
    while len(sonName) == 0:
        sonName = input(f"Please enter son name: ")
    # Sixth Question
    daughterName = input(f"\nWhat is the daughter name: ")
    while len(daughterName) == 0:
        daughterName = input(f"Please enter daughter name: ")
    # Seventh Question
    familyName = input(f"\nWhat is the family last name:  ")
    while len(familyName) == 0:
        familyName = input(f"Please enter family name: ")
    #  Eighth Question
    city = input(f"What city does family and {name}live in:  ")
    while len(city) == 0:
        city = input(f"please enter a city:  ")
    # Ninth Question
    state = input(f"What state is {name} from:  ")
    while len(state) == 0:
        state = input(f"Please enter a state: ")
    # Tenth Question
    vacation = input(f"\nWhat kind of vacation is {name} going on: ")
    while len(vacation) == 0:
        vacation = input(f"please enter a vacation type:  ")
    # Eleventh Question
    transportation = input(f"\nWhat type of transportation does the family take to arrive for their {vacation}:  ")
    while len(transportation) == 0:
        transportation = input(f"please enter a transportation:  ")
    # Twelve Question
    place = input(f"fWhat place does the family staying at for spring break:  ")
    while len(place) == 0:
        place = input(f"please enter a place:   ")

    # Story begins
    print(f"After four hours passed the {familyName} and {name} had made it to there to their {vacation}.")
    print(f"{dadName} was bring the family bags and suitcases to their room. ")
    print(f"{name} was looking around the place to see what all is in there that he can get into. ")
    print(f"{sonName} and {daughterName} went to the video game arcade to see what all type of games. ")
    print(f"{momName} went to check out the spa section with {dadName} and told the kids to be back in three hours.")
    print(f"Which the only one was left inside the room is {name} but he was in the living room sleeping on the coach.")
    print(f"When {name} heard everyone leaving he started to walk around the place to see what he can explore. ")

    # Decision One
    VacationSpringBreak = input(f"\nShould {name} go to the bed room to mess it up the rooms?  Type yes or no:  ")
    while VacationSpringBreak.lower() != "yes" and VacationSpringBreak.lower() != "no":
        VacationSpringBreak = input("Please type yes or no:  ")

    if VacationSpringBreak == "yes":
        print(f"{name} jump on the bed and start ripping the sheets and pillows.  ")
        print(f"He than knock the lamp off the nightstand and run the telephone around the living room and kitchen.")
        print(f"{name} knock over the tv and flush one of this owner sock in the toilet causing a flood. ")
        print(f"The water started falling down the next guest room which causes damages all over the hotel. ")
        print(f"The guests are upset at the matter of their rooms being destroy along with their bags and electronic.")
        print(f"When the hotel manager sent the housekeepers to check out which room the water is coming from. ")
        print(f"Lucky one of the housekeepers had found the room the water coming from only found a dog in the room.")

    else:
        print(f"{name} did not go through the owners rooms.  ")
        print(f"Instead he went in the living room and lay in the doggy bed.   ")
        print(f"The dog was watching his favorite tv show Rick and Morty new season.  ")
        print(f"Then got up to go press a special button to let the owner know when it time to go outside. ")
        print(f"When {sonName} and {daughterName} came to the room {name} came out running to greet them.  ")
        print(f"As the kids took {name} outside they say a french poodles waking by when {name} saw they walk by.")
        print(f"{name} tried to get the twin girls poodles attention by walking pass them as a dog show winner.  ")
        print(f"{name} even tried to sniff them but as always it failed for {name} they growl and bark at {name}.   ")

    # Decision two
    DoggyVacationDay = input(f"\nShould {name} bark back at the twin french poodles?  Type yes or no:")
    while DoggyVacationDay.lower() != "yes" and DoggyVacationDay.lower() != "no":
        DoggyVacationDay = input(f"please type yes or no:  ")

    if DoggyVacationDay == "yes":
        print(f"\n{name} has stood his ground and bark at them as well. ")
        print(f"As he bark they ran off to get away from him because they thought he was crazy. ")
        print(f"{name} was sad that he didn't get his vacation blowout he wanted. ")
        print(f"The kids tried to cheer {name} up by giving him chicken from chick-fli-a.")
        print(f"This made {name} very happy that he forgot all about the french poodles.  ")
        print(f"When the parent came back to the room they saw the kids and {name} sleeping in the room.")

    else:
        print(f"\nAs the twin poodles bark at {name}  he started to get scared and ran away to the kids.  ")
        print(f"They took {name} to the park to cheer him up but it wasn't working as he lay in the grass looking sad.")
        print(f"{sonName} threw a ball to see if {name} would catch it but he didn't move at all.")
        print(f"As the kids went to get {name} a doggy treat from the snack hut a girl beagle walk pass him. ")
        print(f"{name} quickly look up and saw her ran to see who she is and get to know her.  ")
        print(f"He walk up to the girl beagle as she sniff his face and give him a kiss. ")
        print(f"When the kids came back from the snack hut to see {name} is up and happy again.  ")
        print(f"They let {name} have fun with his new girlfriend as they sit next to the girls dog owner's kids.  ")
        print(f"While they all sit back hangout and the dogs playing together.")

    # Alternate Endings
    if VacationSpringBreak == "yes" and DoggyVacationDay == "yes":
        print(f"\nThe hotel managers contacted the the parents to come to the office where they saw {name} in a cage. ")
        print(f"They both billed and kick out the hotel and was force to check in the morning.  ")
        print(f"The parents was upset but also was laughing at how {name} cause so much damages to a hotel.")
        print(f"Making this the best spring break vacation the most memory to last for the life time. ")
        print(f"When the kids came back to the room with {name} and all the family telling each other how their day.")
        print(f"And even if {name} ruining the trip he still has a time of his life.")
    elif VacationSpringBreak == "no" and DoggyVacationDay == "no":
        print(f"After coming back from hanging out with their new friends the family sat and eat dinner together. ")
        print(f"And talk about how they day went and the kids told their parents they made new friends.")
        print(f"They even told them about {name} girlfriend and the parent was shock and proud at the same time. ")
        print(f"As the {familyName} continue enjoying their stay it was time to go home and as the kids said goodbye.")
        print(f"To their new friends {name} gave a goodbye kiss and sniff to his girlfriend. ")

    else:
        print(f"\nAfter spending a week in {vacation} the {familyName} ask {name} did he had fun. ")
        print(f" As he look at them with a big smile on his face they knew he had a blast. ")
        print(f"When they got home and finished unpacking the family watch a movie as {name} in his bed sleeping ")
        print(f"After a few minute {momName} something smell funny and ask who farted.")
        print(f"Everyone look and said it wasn't them but when they look at {name} and find out it was him all along.")
        print(f"{name} look at them and smile as they smell his fart.")
    print(f"\nThe End")

    keepPlaying = input(f"\nDo you want to play again? Enter yes or no:  ")
    while keepPlaying.lower() != "yes" and keepPlaying.lower() != "no":
        keepPlaying = input(f"Please type yes or no:  ")
