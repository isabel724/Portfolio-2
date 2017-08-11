import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')

print(countries)
country = input("Country: ").title()

# Start your search algorithm here.
first = 0
last = len(countries)

notFound = True

while notFound and first <= last:
    midpoint = (first+last) // 2
    if country > countries[midpoint]:
        first = midpoint + 1
    elif country < countries[midpoint]:
        last = midpoint - 1
    elif country == countries[midpoint]:
        print (countries[midpoint] + " was found at index " + str(midpoint+1))
        notFound = False

if notFound:
    print ("That was not found in the list..")
