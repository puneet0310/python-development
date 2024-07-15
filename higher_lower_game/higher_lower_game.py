#display the art on the screen 
from art import logo,vs
from game_data import data
import random as random

game_continue=True
score = 0
account_B=random.choice(data)
while game_continue:

    #import the game data into the game 
    

    #generate random account fromt the data pool
    
    account_A=account_B
    account_B=random.choice(data)
    
    if account_A==account_B:
        account_B=random.choice(data)


    #printable format
    print(logo)
    account_name=account_A["name"]
    account_des=account_A["description"]
    account_country=account_A["country"]
    print(f"{account_name},a {account_des},from {account_country}")
    #printing vs logo 
    print(vs)
    #printing second canditate
    account_name=account_B["name"]
    account_des=account_B["description"]
    account_country=account_B["country"]
    print(f"{account_name},a {account_des},from {account_country}")
    #getting the input
    guess= input("who has more followers? 'A' or 'B':").lower

    #get the followers count
    A_follwer_count=account_A["follower_count"]
    B_follwer_count=account_B["follower_count"]
    guess_iscorrect=False
    if A_follwer_count >B_follwer_count:
        guess =="a"
        print("True")
        guess_iscorrect=True
    elif A_follwer_count <B_follwer_count:
        guess =="a"
        print("False")
    elif A_follwer_count >B_follwer_count:
        guess =="b"
        print("false")
    elif A_follwer_count <B_follwer_count:
        guess =="b"
        print("True")
        guess_iscorrect=True
    else:
        print("invalid text")
    
    if guess_iscorrect==True:
        score+=1
        print("YOU ARE RIGHT YOUR SCORE IS :",score)
    else:
        game_continue=False
        print("YOUR WRONG YOUR SCORE IS :",score)