import random
randNum=random.randint(1,100)
# print(randNum)
user=False
guesscount=0

while(user!=randNum):
    user=int(input("Enter your guess: "))
    guesscount+=1
    if(randNum==user):
        print("You guessed it right!")
    else:
        if(user>randNum):
            print("You guessed it wrong! Enter a smaller number")
        elif(user<randNum):
            print("You guessed it wrong! Enter a larger number")

print(f'You guessed the number in {guesscount} guesses')

with open('bestscore.txt','r') as f:
    bestscore=int(f.read())
    if(bestscore>guesscount):
        with open('bestscore.txt','w') as f:
            f.write(str(guesscount))

with open('bestscore.txt') as f:
    r=f.read()
    print(f'Best score: {r}')

