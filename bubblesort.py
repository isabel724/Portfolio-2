import csv
import string

# Open the CSV File and read it in.
f = open('cities.csv')
data = f.read()

# Split the data into an array of countries.
cities = data.split('\n')

# Start your search algorithm here.
for x in range (1, len(cities)):
    y = x
    while cities[y] < cities[y-1]:
        holder = cities[y]
        cities[y] = cities[y-1]
        cities[y-1] = holder
        if y > 1:
            y -= 1

city = input("City: ").title()

# Start your search algorithm here.
first = 0
last = len(cities)

notFound = True

while notFound and first <= last:
    midpoint = (first+last) // 2
    if city > cities[midpoint]:
        first = midpoint + 1
    elif city < cities[midpoint]:
        last = midpoint - 1
    elif city == cities[midpoint]:
        print (cities[midpoint] + " was found at index " + str(midpoint+1))
        notFound = False

if notFound:
    print ("That was not found in the list..")
