stars: int = int (input ("how many stars?"))
spaces: int = stars // 2
for i in range(1, stars + 1, 2):
    print(spaces * " ", end="")
    for j in range(1, i + 1):
        print("*", end="")
    print()
    spaces -= 1





