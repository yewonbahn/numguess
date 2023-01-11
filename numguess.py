from random import randint
from time import sleep

def opening():

    answer=randint(1,100)
    username = input("enter your name: ")
    print(f"Hi,{username}, Welcome to my game. Guess the number from 1 to 100.")
    return answer,username

def game(guess,username):
    #Compare answer with user's guess
    if guess==answer:
        print("*********************************")
        sleep(1)
        print("*********************************")
        sleep(1)
        print("*********************************")
        sleep(1)
        print(f"You got it right! The answer is {answer}.")
        return 1

    elif guess>answer:
        print(f"Keep going,man ~ That was too high,{username}..")
    elif guess<answer:
        print(f"Keep going,man ~ That was too low,{username}..") 

answer,username= opening()

for i in range(1,10+1):
    guess = int(input("guess number: "))
    value=game(guess,username)
    if value==1:
        break

