inputDataStr = input()
minInput = -10 ** 9
maxInput = 10 ** 9

result = "Error input!"


a, b = map(int, inputDataStr.split())

if minInput <= a <= maxInput and minInput <= b <= maxInput:
    result = a + b**2


print(result)