import random
num: int = random.randint (1, 100);
count: int = 0
while True:
    Guess: int = int (input ("Please guess the number"));
    count = count + 1
    if Guess > num:
        print (f"You guessed the number {Guess}. Sadly, it's too big...")
    elif Guess <num:
        print (f"You guessed the number {Guess}. Sadly, it's too small...")
    else:
        print ("Bingo!");
    if Guess == num:
        break;
print(f"Congratulations! You guessed the correct number after {count} attempts!")





