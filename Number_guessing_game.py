import random
import math
lower = int(input('Enter lower bound:'))
upper = int(input('Enter upper bound:'))

x=random.randint(lower,upper)
print('You have only',round(math.log(upper-lower+1,2)),'chances to guess the integer')

count=0
while count< math.log(upper-lower+1,2):
    count+=1

    guess=int(input('Guess a number:-'))

    if x==guess:
        print('Congratulations you did it in',count,'try')
        break
    elif x>guess:
        print('You guessed too small')
    elif x<guess:
        print('You guessed too high')

if count>= math.log(upper-lower+1,2):
    print('The number is ',x)
    print('Better luck next time')