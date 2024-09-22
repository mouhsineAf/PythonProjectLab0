inputFile = open('input.txt', 'r')
outputFile = open('output.txt', 'w')
minInput = -10 ** 9
maxInput = 10 ** 9

result = "Error input!"


a, b = map(int, inputFile.readline().split())

if minInput <= a <= maxInput and minInput <= b <= maxInput:
    result = a + b**2

outputFile.write(str(result))

inputFile.close()
outputFile.close()