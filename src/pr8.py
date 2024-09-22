import time
import tracemalloc


t_start = time.perf_counter()
tracemalloc.start()


inputFile = open('input.txt', 'r')
outputFile = open('output.txt', 'w')

minInput = 0
maxInput = 10 ** 7

result = "Error input!"


n = int(inputFile.readline())

if minInput <= n <= maxInput:
    if n == 0 or n == 1:
        result = n
    else:
        a, b = 0, 1
        for i in range(n -1):
            a, b = b, a + b

        result = b % 10

outputFile.write(str(result))

inputFile.close()
outputFile.close()

current, peak = tracemalloc.get_traced_memory()

current = current / 10**3
peak = peak / 10**3

print("Time used: ", (time.perf_counter() - t_start))
print("Current memory usage is: "  + str(current))
print("Peak memory usage was: "  + str(peak))

tracemalloc.stop()