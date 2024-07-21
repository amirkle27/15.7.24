num: int = int (input ("Good morning, please enter a number"))
for i in range (1, num+1):
    for j in range (1, i+1):
       print (j, end=" ")
    print ()
for i in range (num-1, 0, -1):
    for j in range (1, i +1):
        print(j, end=" ")
    print()







#num: int = int (input ("Good morning, please enter a number"))
#for i in range (1, num + 1):  # 1 2 3 4 5
   # for j in range (1, i + 1):  # 1..1 1..2 1..3 1..4 1..5
  #      print(j, end="")
 #   print()