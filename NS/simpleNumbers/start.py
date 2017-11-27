import random

def readNumbers():
    numbers = {}
    for line in open('numbers.txt'):
        separated_line = line.rsplit()
        numbers[int(separated_line[0])] = separated_line[2]
    return numbers
def readFives():
    fives = []
    for line in open('test5.txt'):
        fives.append(line.rstrip())
    return fives

numbers = readNumbers()
fives = readFives()
weights = [0 for i in range(15)]
bias = 7

def main():
    train()
    print(weights)

    for i in range(10):
        print("{0} is 5 ? {1}".format(i, proced(numbers.get(i))))
    for i in fives:
        print("is 5? - {0}".format(proced(i)))

def train():
    for i in range(10000):
        option = i % 10
        if option != 5:
            if proced(numbers.get(option)):
                decrease(numbers.get(option))
        else:
            if not proced(numbers.get(option)):
                increase(numbers.get(option))

def proced(number):
    net = 0
    for i in range(15):
        net += (int(number[i]) * weights[i])
    return net >= bias

def decrease(number):
    for i in range(15):
        if int(number[i]) == 1:
            weights[i] -= 1

def increase(number):
    for i in range(15):
        if int(number[i]) == 1:
            weights[i] += 1

def readNumbers():
    numbers = {}
    for line in open('numbers.txt'):
        separated_line = line.rsplit()
        numbers[int(separated_line[0])] = separated_line[2]
    return numbers

def readFives():
    fives = []
    for line in open('test5.txt'):
        fives.append(line.rstrip())
    return fives

main()
