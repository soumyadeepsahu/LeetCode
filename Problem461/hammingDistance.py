x = 30
y = 10

X = []
Y = []
power = 0

powerX = 0
powerY = 0

while(2**power <= x):
    power += 1
powerX = power

while(2**power <= x):
    power += 1
powerY = power

while(powerX > 0):
    if((x-(2**powerX)) > 0):
        x -= 2**powerX
        powerX -= 1
        X.append("1")
    else:
        X.append("0")
print(X)
