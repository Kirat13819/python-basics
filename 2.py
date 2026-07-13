import random
y = random.randint(1,40)
for attempt in range(7):
    x = int(input('guess the number between 1 to 40: '))
    if x==y:
        print('wow! you guessd it right')
        break
    elif x>y:
        z = 6 - attempt
        print(f'attempt too high, you have {z} attempts remaning')
    elif x<y:
        z = 6 - attempt
        print(f'attempt too low, you have {z} attempts remaning')

else:
    print(f'game is over, the answer was {y}')
    