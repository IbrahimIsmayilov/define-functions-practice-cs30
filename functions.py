def studentFeeback(name, performance):
    return f"{name} is doing {performance} in this class."

import math

def heronsFormula(sideA, sideB, sideC):
    s = (sideA + sideB + sideC) / 2
    area = math. sqrt(s * (s - sideA) * (s - sideB) * (s - sideC))
    return area

test = heronsFormula(1, 1, 1)
print(test)

def analyzeNumber(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

print(analyzeNumber(-1))

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False


def seriesSum(start, stop, step):
    sum = 0
    while start <= stop:
        sum += start
        start += step   
    return sum

print(seriesSum(1, 10, 1))
print(seriesSum(1, 4, 1))