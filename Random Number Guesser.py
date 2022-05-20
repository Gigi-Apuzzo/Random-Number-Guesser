import random
guesses = 0

try:
    num = random.randint(1,20)
    print("Im thinking of a number between 1 and 20")

    while guesses < 6:
        guess = int(input("Take a guess: "))
        guesses = guesses + 1

        if guess < num:
            print("Your guess is too low!")

        if guess > num:
            print("Your guess is too high")
        
        if guess == num:
            break
    if guess == num:
        print("Well done! You guessed the number in", guesses,"guesses!")
    if guess != num:
        print("You didnt guess it. The number I was thinking of was", num)
except:
    print("An error has occured, try restarting the code.")