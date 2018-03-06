## 1. Opening Files ##

f = open("crime_rates.csv", "r")
print(f)

## 2. Reading In Files ##

f = open("crime_rates.csv", "r")
data = f.read()

## 3. Splitting ##

# We can split a string into a list.
sample = "john,plastic,joe"
split_list = sample.split(",")
print(split_list)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)

# Code from previous cells
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split("\n")
print(rows[0:5])
print(rows[0])

## 5. Practice - Loops ##

ten_rows = rows[0:10]
for t in ten_rows:
    print(t)
    

## 6. List of Lists ##

three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
listoflist = []
for t in three_rows:
    listoflist.append(t.split(","))
print(listoflist[1])

## 7. Practice - Splitting Elements in a List ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
final_data = []
for listelement in rows:
    final_data.append(listelement.split(","))
#print(final_data[0:5])
print(final_data[:][1])

## 8. Accessing Elements in a List of Lists: The Manual Way ##

#print(five_elements)
cities_list = []
for element in five_elements:
    cities_list.append(element[0])
print(cities_list)

## 9. Looping Through a List of Lists ##

crime_rates = []

for row in five_elements:
    # row is a list variable, not a string.
    crime_rate = row[1]
    # crime_rate is a string, the crime rate of the city.
    crime_rates.append(crime_rate)
    
cities_list = []
for element in final_data:
    cities_list.append(element[0])

## 10. Challenge ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')#list of elements


int_crime_rates = []# list of integers
spltdelmnts = []# list of splitted elments
for element in rows:
    spltdelmnts.append(element.split(","))
    
for element in spltdelmnts:
    int_crime_rates.append(int(element[1]))

print(int_crime_rates)