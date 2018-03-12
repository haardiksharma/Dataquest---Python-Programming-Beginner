## 3. Read the File Into a String ##

inputfile = open("dq_unisex_names.csv", 'r')
names = inputfile.read()


## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list= names.split("\n")
first_five = names_list[0:5]
print(first_five)

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
nested_list = []
for element in names_list:
    nested_list.append(element.split(","))
print(nested_list)

## 6. Convert Numerical Values ##

numerical_list = []
# temp_list = []
for element in nested_list:
    elem0 = (element[0])
    elem1 = float(element[1])
    temp_list = []
    temp_list.append(elem0)
    temp_list.append(elem1)
    numerical_list.append(temp_list) 
    
print(numerical_list[0:5])

## 7. Filter the List ##

# The last value is ~100 people
thousand_or_greater = []

for element in numerical_list:
    if element[1] >= 1000:
        thousand_or_greater.append(element[0])
        
print(thousand_or_greater[0:10])      