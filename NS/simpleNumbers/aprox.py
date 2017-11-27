import random

k = random.uniform(-5, 5)
c = random.uniform(-5, 5)
print('begin line: ', k, '* X + ', c)

data = {
    1: 2,
    2: 4,
    2.5: 5,
    3.8: 7.6,
    4: 8,
    6: 12,
    6.6: 13.2,
    7.2: 14.4,
    8: 16,
    8.5: 17
}

rate = 0.0001

def proceed(x):
    return k * x + c

for i in range(1000000):
    x = random.choice(list(data.keys()))
    true_result = data[x]
    out = proceed(x)
    delta = true_result - out
    k += delta * rate * x
    c += delta * rate 

print("end line: {0} * x + {1}".format(k, c))  