from random import randint

answer=randint(1,100)
print(answer)

username = input("enter your name: ")
print(f"Hi,{username}, Welcome to my game. Guess the number from 1 to 100.")
guess = int(input("guess number"))
print(f"your number is {guess}")
