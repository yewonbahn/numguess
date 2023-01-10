from random import randint
from time import sleep

answer=randint(1,100)
print(answer)

username = input("enter your name: ")
print(f"Hi,{username}, Welcome to my game. Guess the number from 1 to 100.")
guess = int(input("guess number: "))
print(f"your number is {guess}")
print(f"is it same number? {answer==guess}")


#Compare answer with user's guess
if guess==answer:
    print("*********************************")
    sleep(1)
    print("*********************************")
    sleep(1)
    print("*********************************")
    sleep(1)
    print(f"You got it right! The answer is {answer}.")
elif guess>answer:
    print(f"Keep going,man ~ That was too high,{username}..")
elif guess<answer:
    print(f"Keep going,man ~ That was too low,{username}..")    
