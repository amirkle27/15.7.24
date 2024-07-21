LastPositive: int = None
LastNegative: int = None
positiveCount: int = 0
negativeCount: int = 0
zeroCount : int = 0
SevenDivCount: int = 0
for i in range (1, 11):
    num: int = int (input ("Please enter a number!!"));
    if num == -9999:
        break;
    if -1000 > num > 1000:
        continue;
    if num > 0:
        positiveCount += 1
        LastPositive = int (num)

    if num < 0:
        negativeCount += 1
        LastNegative = int (num)
    if num == 0:
        zeroCount += 1
    if num % 7 == 0:
        SevenDivCount +=1
else:
    print (f"You have entered {positiveCount} positive numbers. \nYou hane entered\
 {negativeCount} negative numbers. \nYou have entered the number Zero {zeroCount} times.\n\
You have entered {SevenDivCount} numbers that divide by 7. \nThe last \
positive number you entered was {LastPositive}, \nAnd the last negative number you entered was {LastNegative}")



