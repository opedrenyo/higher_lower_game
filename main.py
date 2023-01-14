from data import data
import random
import art
import os

END_DATA_LIST = len(data) -1
FIRST_RANDOM_NUMBER = random.randint(0,END_DATA_LIST)
SECOND_RANDOM_NUMBER = random.randint(0,END_DATA_LIST)

while SECOND_RANDOM_NUMBER == FIRST_RANDOM_NUMBER:
    SECOND_RANDOM_NUMBER = random.randint(0,END_DATA_LIST-1)

SCORE = 0
ERROR = 0



def random_account_choice(random_number):
    '''Choose a random account from the data list base on the index given.'''
    name = data[random_number]["name"]
    description = data[random_number]["description"]
    country = data[random_number]["country"]
    followers = data[random_number]["follower_count"]

    return [name,description,country, followers]

def who_wins(celebrity1, celebrity2, guess):
    '''Compare followers from celebrity1 with celebrity2 based on the selected guess.'''
    conversor = 1    
    if guess == 'b':
        conversor *= -1
    if celebrity1[3] > celebrity2[3]*conversor:
        print("You're right!")
        return [SCORE + 1, ERROR]
    else:
        return [SCORE, ERROR + 1]


first_celebrity = random_account_choice(FIRST_RANDOM_NUMBER)
first_celebrity_name = first_celebrity[0] 
first_celebrity_description = first_celebrity[1]
first_celebrity_country = first_celebrity[2]
first_celebrity_followers = first_celebrity[3]

os.system('cls')

print(art.logo)

print(f"Score: {SCORE}")

print(f"\nCompare A: {first_celebrity_name}, a {first_celebrity_description}, from {first_celebrity_country}")


# MAIN PROGRAM
while ERROR < 1:  

    print(art.vs)
    
    second_celebrity = random_account_choice(SECOND_RANDOM_NUMBER)
    second_celebrity_name = second_celebrity[0] 
    second_celebrity_description = second_celebrity[1]
    second_celebrity_country = second_celebrity[2]
    second_celebrity_followers = second_celebrity[3]
    


    print(f"Compare B: {second_celebrity_name}, a {second_celebrity_description}, from {second_celebrity_country}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()



    new_score = who_wins(first_celebrity, second_celebrity, guess)
    SCORE = new_score[0]
    ERROR = new_score[1]

    if ERROR == 0:
        first_celebrity = second_celebrity
        first_celebrity_name = first_celebrity[0] 
        first_celebrity_description = first_celebrity[1]
        first_celebrity_country = first_celebrity[2]
        first_celebrity_followers = first_celebrity[3]
        
        LAST_SECOND_NUMBER = SECOND_RANDOM_NUMBER
        SECOND_RANDOM_NUMBER = random.randint(0,END_DATA_LIST)
        while SECOND_RANDOM_NUMBER == FIRST_RANDOM_NUMBER or SECOND_RANDOM_NUMBER == LAST_SECOND_NUMBER:
            SECOND_RANDOM_NUMBER = random.randint(0,END_DATA_LIST-1)

        FIRST_RANDOM_NUMBER = SECOND_RANDOM_NUMBER
        
        os.system('cls')
        
        print(art.logo)

        print(f"Score: {SCORE}")
        
        print(f"\nCompare A: {first_celebrity_name}, a {first_celebrity_description}, from {first_celebrity_country}")
    else: 
        os.system('cls')
        print(f"Sorry, that's wrong. Final score: {SCORE}")
        ERROR += 1