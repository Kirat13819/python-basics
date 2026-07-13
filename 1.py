import random
y = random.randint(0,5)
for attempt in range(3):
    x = int(input('guess the number between 1 to 10: '))
    if x==y:
        print('wow! you guessd it right')
        break
    else:
        z = 2 - attempt
        print(f'wrong!, you have {z} attempts remaning')

else:
    print(f'game is over, the answer was {x}')
