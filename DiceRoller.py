import random

min = 1
max = 6

rollAgain = "y" or "n"

while rollAgain == "y":
  print("You are rolling a d" + str(max))
  print("Rolling the dice...")
  print("The result is:")
  result = random.randint(min, max)
  print(result)
  
  rollAgain = input("Do you want to roll again? Type y(yes) or no(n).")
  print("----------------------------------------------------------------------")
  if rollAgain == "n":
    print("Okay, see you next time!")