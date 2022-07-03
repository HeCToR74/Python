import random

with open('random_numbers.txt', 'w') as file:
    for i in range(random.randint(10, 40)):
        for j in range(random.randint(30, 50)):
            file.write(str(random.randint(0, 1000))+' ')
        file.write('\n')
