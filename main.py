# Greet the user and provide instructions
print(f"Greeting audiences! I want to share with you all a story about a man preparing for his blind date.")
print(f"Before we start with the story, I want to ask some few questions to help the man be ready and on time for the his date.  ")
print(f"After answering the question, make sure that you press the  press the enter key.  ")
input(f"\nPress enter to continue...")

keepPlaying = "yes"
while keepPlaying.lower() == "yes":

    # First Questions Before we start story
    name = input(f"\nWhat is the man name:  ")
    while len(name) == 0:
        name = input(f"please enter a name:  ")
    # Second Questions
    city = input(f"\nWhere does this story that place:  ")
    while len(city) == 0:
        city = input(f"please enter a city:  ")
    # Third Question
    state = input(f"\nWhat state does {name} from:  ")
    while len(state) == 0:
        state = input(f"please enter a state:  ")
    # Forth Question
    restaurant = input(f'What restaurant is he meeting his blind date:  ')
    while len(restaurant) == 0:
        place = input(f"Please enter a place: ")
    # Fifth Question
    outfit = input(f"\nWhat should he wear on his date: ")
    while len(outfit) == 0:
        outfit = input(f"please enter a outfit:  ")
    # Sixth Question
    transport = input(f"\nWhat type of transport should z {name} take to arrive for his date:  ")
    while len(transport) == 0:
        transport = input(f"please enter a transport:  ")
    # Seventh Question
    time = input(f"fWhat time should {name} need to arrive at the restaurant:  ")
    while len(time) == 0:
        time = input(f"please enter a time:   ")
    # Eighth Question
    route = input(f"\nWhat route should {name} take to make it to the restaurant:  ")
    while len(route) == 0:
        route = input(f"please enter a route:  ")
    # Ninth Question
    dateName = input(f"\nWhat is the name of {name} blind date:  ")
    while len(dateName) == 0:
        dateName = input(f"please enter a name:    ")
    # Tenth Question
    conversation = input(f"\nHow should {name} start off a conversation with {dateName} to break the ice:   ")
    while len(conversation) == 0:
        conversation = input(f"please enter a conversation:   ")

    # Story begins
    print(f"\nThe story starts with a man name {name} who live in {city}.  ")
    print(f"\nHe is a grad student from {state}  university and major in Computer Science.  ")
    print(f"\n{name} has been in bad relationship in back in his colleges year.   ")
    print(f"\nOn saturday night {name} was hanging out with his old friends from college at a bowling alley.  ")
    print(f"\nOne of his friend suggested he should get back in dating scene by signing him up on a blind dating app.  ")
    print(f"\nAt first {name} didn't want to get wrap into the blind dating but he gave it a try at least.")
    print(f"\nBecause he was tired of being the third wheel on his friends dates.  ")
    print(f"\nNext morning {name} recieved a message on the dating app from a mysterious user.   ")
    print(f"\nThe message starts off with a greeting to {name} and asking him if they can meet face to face at a restaurant ")
    print(f"\nThe restaurant {name} had suggested they can meet at is {restaurant} at seven tonight.  ")
    print(f"\nThey both agree to the time and place for they date tonight.  ")
    print(f"\n{name} has start to get to get ready for his blind date by deciding on what to wear.  ")
    print(f"\nHe was trying to see what kind of outfit will make good impression.  ")
    print(f"\nAfter spending four hours on deciding what to wear {name} has pick the {outfit} for tonight.  ")
    print(f"\nHe look at his watch to see what time is it was one hour until his date start.   ")
    print(f"\n{name} is trying to see which transportion he should take to get to his date.  ")

    # Decision 1
    GoingToTheRestaurant = input(f"\nShould {name} take his blue cars to for his date?  Type yes or no:  ")
    while GoingToTheRestaurant.lower() != "yes" and GoingToTheRestaurant.lower() != "no":
        GoingToTheRestaurant = input("Please type yes or no:  ")

    if GoingToTheRestaurant == "yes":
        print(f"\n{name} took the blue car to get to the restaurant on for his date.  ")
        print(f"\nHe was almost arriving  at the restaurant thirty minutes early when he saw one side of street is close. ")
        print(f"\n{name} is try to see which route should he take to get to restaurant on time. ")
        print(f"\nHe saw the one short cut back up on traffic and the other one was had fewer cars in it.  ")
        print(f"\nBut if he took the second short cut he be two minute late.  ")
        print(f"\nWhen he got to {restaurant} {name} was looking for a parking space where all almost full. ")
        print(f"\nLucky {name} found a open spot in front of the restaurant.  ")

    else:
        print(f"\n{name} did not take the blue car but instead the red motor bike.  ")
        print(f"\nHe was riding down the street where he saw a sharp items ahead.   ")
        print(f"\n{name} quickly change lines to avoid going though the sharp items.  ")
        print(f"\nAt the traffic light {name} look at his phone to see how much time he had left to make to his date. ")
        print(f"\nOnly to see that he was not running late but making it early.  ")
        print(f"\nWhile he was on his way he saw the street used to take to get to the restaurant was close due blockage  ")
        print(f"\nHe took the different route to get to {restaurant} lucky he made it there five minute early.  ")
        print(f"\n{name} park his red motor bike on the side walk by {restaurant}.   ")


    #Decision 2
    BlindDateNight = input(f"\nShould {name} call or text his date to let her know he made it to restaurant? Type yes or no:  ")
    while BlindDateNight.lower() != "yes" and BlindDateNight.lower() != "no":
        BlindDateNight = input(f"please type yes or no:  ")

    if BlindDateNight == "yes":
        print(f"\n{name} was waiting outside {restaurant} to meet his blind date before they go in the restaurant. ")
        print(f"Five minute later and no sign of the mystery date in sight. ")
        print(f"{name} started to get nervous and wondering if she gotten lost or didn't know where they can meet up.  ")
        print(f"\nHe thought about calling her to see if she made it to the restaurant safely and ask can she see him by the door.  ")
        print(f"When {name} call her she answer and ask if he already made to {restaurant}.  ")

    else:
        print(f"\n{name} decided to not call her and assume that she might change her mind on the date:  ")
        print(f"He start to go get his motor bike to go home where he see video game store had a discount on new games. ")
        print(f"{name} went in the game store to find the one on discount display  ")
        print(f"\nHe saw this woman by the action game section and see her pick the same game he was getting.  ")
        print(f"\nThe woman also notices the man with the game in the check out line.  ")
        print(f"\nThey stated talking and getting to know each other then the woman ask if he want to play together sometime.  ")
        print(f"\nHe said sure and exchange numbers to keep in contact with each other.  ")
        print(f"\n{name} ask the woman what was her name is before she go and she told him that is Sarah.  ")

    #ALternate Endings
    if GoingToTheRestaurant == "yes" and BlindDateNight == "yes":
        print(f"\nThey gotten to know each other and she told him her favorite hobbies in video games and coding.  ")
        print(f"\n{name} and {dateName} has found that they have more things in common after four hour has past.  ")
        print(f"\nAnd they had spend the whole night talking about their dream careers and goals.  ")
        print(f"\nAfter spending the night at  {restaurant},  {name} had a blast on his blind date.  ")
        print(f"He hope to go on another date with {dateName} again soon so he can show some of his coding project off to her.  ")
    elif GoingToTheRestaurant == "no" and BlindDateNight == "no":
        print(f"After not getting to meet his blind date but got his unlucky night turn around  ")
        print(f"\nHe got a change to get his favorite video game and got to meet a women with the same hobbies as him.  ")
        print(f"\n{name} got sarah number to call her sometime to hangout and wonder if he should ask her out next saturday.  ")
        print(f"\nHe texted her to see if she is busy saturday night which sarah replied she is free on saturday.  ")
        print(f"\nwhere both agree to they will go out next weekend and {name} had a good day  after all to make up from earlier. ")

    else:
        print(f"\nAfter spending a the night in {restaurant}, {name} blue car was out of gas and forgot to refill it before he left. ")
        print(f"{dateName} happen to see {name} is having trouble with car and offer to give him a ride to the nearest gas station. ")
        print(f"He happyly accepted the offer and they drove to the gas station up the street to get gas for {name} car. ")
        print(f"After coming back from the gas station and restuarant {name} made it home where {dateName} text him to let him know she had a get time tonight. ")
    print(f"\nThe End")

    keepPlaying = input(f"\nDo you want to play again? Enter yes or no:  ")
    while keepPlaying.lower() != "yes" and keepPlaying.lower() != "no":
        keepPlaying = input(f"Please type yes or no:  ")







