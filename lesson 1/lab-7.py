from random import randint
from time import sleep
money=int(input("insert how much money you have : "))
print("the game costs 3 NIS .")
turns=money//3
print(turns)
if turns != 0:
     print("your change is : " + str(money%3) + "\nyou have " + str(money//3) + " rounds")

else:
     print("you gave the currect count of money." + "\nyou  have " + str(money//3) + " rounds")

num=0
for y in range(turns):
      print("round number " +str(y+1) + ":")
      cube1=randint(1,6)
      cube2=randint(1,6)
      print("cube1 :" + str(cube1) + " cube2 :" + str(cube2))
      if cube1 == cube2 and cube1 != 6:
          print("you won 100 NIS.")
          num=num+100
      elif cube1 == cube2 and cube1 == 6:
          print(("you won 1000 NIS"))
          num=num+1000
      elif cube2 == 2:
          print("you won 40 NIS ")
          num = num + 40
      elif cube1 == 1:
          print("you won 20 NIS ")
          num = num + 20
      else:
          print("you don't won nothing ")
print(num)
