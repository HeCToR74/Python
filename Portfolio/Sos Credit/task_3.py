import sys

n = int(sys.argv[1])

with open('random_numbers.txt', 'r') as file:
    for line in file.readlines()[-n:]:
        print(line.replace('\n', ''))



