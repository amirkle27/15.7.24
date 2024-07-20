movies: list [str] = ["Terminator", "Back to the Future", "Heat"];
movies.append ("Die Hard");
movies.insert (5, "Once Upon a Time in America" );
print (len (movies));



import random;
numbers: list [int] = []
for i in range (1, 11):
    num: int = random.randint(1, 100);
    numbers.append(num);
print (numbers);




import random;
statements: list [bool] = []
for i in range (1, 11):
    bools: bool = random.choice ([True,False]);
    statements.append(bools)
print (statements)



import random;
random_words: list [str]
words: list [str] = []
answer: str = str (input ("Hello, do you wish to generate a new random word?"));
while answer == "yes" or answer == "y":
    word: str = ("")
    length: str = random.randint(5, 20)
    newword = word+word
    for j in range (1,length+1):
        letters: str = random.choice (["a","b", "c"])
        newword = word + letters
        word = newword
    word = newword
    words.append(word)
    print (words)
    answer: str = str(input("Hello, do you wish to generate a new random word?"));
random_words = random.randint(10,20)
for k in range (random_words):
    random_words = random.choice (words)
    print (random_words);