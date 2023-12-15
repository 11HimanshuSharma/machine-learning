import random
true_number = random.randint(1,100)
guess_number = int(input("enter your guess between 1 and 100: "))
while True:
  if guess_number == true_number:
    print('You are right! GOOD JOB')
    fruits = ['apple', 'banana', 'cherry']
    break
  elif guess_number < true_number:
    print("your number is too low, Please try again")
    guess_number = int(input("enter your guess between 1 and 100: "))
  elif guess_number > true_number:
    print("your guess is high, please try again")
    guess_number = int(input("Enter your guess between 1 and 100: "))
  