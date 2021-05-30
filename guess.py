import random
n=random.randint(1,20)

count=1
guess_chances=8
while 1<=guess_chances:
    num=int(eval(input("Enter the number:")))
    if num>n:
        print("Your guess chances is to high, guess the number lower than :", num)

    elif num<n:
        print("Your guess is to low. Guess a number higher than :", num)
    else:
        print("You win")
        print(count,"Guess you took")
        break
    guess_chances-=1
    print(guess_chances,"guesses left")
    count+=1
    print()

print("Game over")
print("Number is:",n)