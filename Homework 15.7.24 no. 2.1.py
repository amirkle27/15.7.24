import random
num: int = random.randint (1, 100);
ans: str = "yes"
ans: str = str(input("Hi, wanna have a go at our game?"))
while True:
    count: int = 0
    if ans == "no" or ans == "n":
        print ("Goodbye, Have a wonderful day!")
        break;
    else:
        while True:
            Guess: int = int(input("Please guess the number"));
            count = count + 1
            if Guess > num:
                print (f"You guessed the number {Guess}. Sadly, it's too big...")
            elif Guess < num:
                print (f"You guessed the number {Guess}. Sadly, it's too small...")
            else:
                print ("Bingo!");
            if Guess == num:
                print (f"Congratulations! You guessed the correct number after {count} attempts!")
                ans: str = str(input("Do you want to play again?"))
                break;
