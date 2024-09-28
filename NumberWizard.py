#played among 2 people
chosen_number = input("Please enter a number between 1 and 30: ")
chosen_number = int(chosen_number)

# repeats until chosen_number is between 1 and 30
while chosen_number < 1 or chosen_number > 30:
    chosen_number = input("Invalid number. Please enter a number between 1 and 30: ")
    chosen_number = int(chosen_number)

print ("Welcome to Number Wizard!")
tries = 0
guess = int(input("Guess the number!: \n"))


#will repeat and count tries when the guessed number doesn't equal the chosen number
while guess != chosen_number: 
    if chosen_number < guess:
        print ("Sorry, guess lower!")
        tries = (tries + 1)
    elif chosen_number > guess:
        print("Sorry, guess higher!")
        tries = (tries + 1)
    guess = int(input("Guess the number!: \n"))

#if user gets the number correct,
if guess == chosen_number:
    tries = str(tries)
    print("Congrats! You've guessed the number in " + tries + " tries!")
