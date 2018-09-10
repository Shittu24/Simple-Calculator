import random

attempts = 5
secret_number = random.radint(1,100)

for attempt in range(attempt):
    guess = int(input("Take a guess: "))

    if(guess < secret_number):
        print("The number is too low")
    elif(guess > secret_number):
        print("The number is too high")
    else:
        print()
        print("You guessed it! The number was " ,secret_number)
        print("You guessed it in" ,attempts, "attempts")

        break

if(guess) != secret_number:
    print()
    print("Sorry, you have reached maximum number of tries")
    print("The secret number was" ,secret_number)
