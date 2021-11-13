import csv
import math

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#To remove headers from CSV
data = file_data[0]

def mean(data):
    total = 0
    n = len(data)

    for x in data:
        total += int(x)

    mean = total / n
    return mean

square_list = []
for number in data:
    a = int(number) - mean(data)
    a = a**2 
    square_list.append(a)

sum = 0
for i in square_list:
    sum = sum+i

result = sum / 9
standard_deviation = math.sqrt(result)
print("The standard deviation is " + str(standard_deviation))


