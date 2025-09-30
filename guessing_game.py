def guessing_game():
    # TODO create guessing game function
    # HINT: Target number should be 15
    # HINT: Return message should be "Congratulations! You guessed it!"
    # HINT: Use input("Enter your guess: ") for user input
    # HINT: Print "Too low! Try again." for low guesses
    # HINT: Print "Too high! Try again." for high guesses
    num = 15
    guess = 0
    while guess != 15:
        guess = int(input("Guess:  "))
        if guess > num:
            print("Too high! Try again.")
        elif guess < num:
            ("Too low! Try again.")
    return ("Congratulations! You guessed it!")
    pass

if __name__ == "__main__":
    # create guessing game below this
    pass
