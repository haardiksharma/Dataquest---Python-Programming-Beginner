## 2. Enumerate ##

"""
Enumerate the ships list using a for loop and the enumerate() function.
For each iteration of the loop:
Print the item from ships at the current index.
Print the item from cars at the current index.

"""
ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for i,v in enumerate(ships):
    print (v)
    print (cars[i])
    

## 3. Adding Columns ##

"""
Loop through each row in things using the enumerate() function.
Append the item in trees that has the same index (as the current thing) to the end of each row in things.
After the code runs, things should have an extra column.
"""
things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for i,v in enumerate(things):
    v.append(trees[i])
things

## 4. List Comprehensions ##

"""
We've written many short for loops to manipulate lists. Here's an example:


animals = ["Dog", "Tiger", "SuperLion", "Cow", "Panda"]
animal_lengths = []
for animal in animals:
    animal_lengths.append(len(animal))
It takes three lines to calculate the length of each string animals this way. However, we can condense this down to one line with a list comprehension:
    animal_lengths = [len(animal) for animal in animals]

This comprehension consists of the list operation len(animal), the loop variable animal, and the list that we're iterating over, animals.
"""
"""
    Use list comprehension to create a new list called apple_prices_doubled, where you      multiply each item in apple_prices by 2.
    Use list comprehension to create a new list called apple_prices_lowered, where you      subtract 100 from each item in apple_prices.
"""
apple_prices = [100, 101, 102, 105]
apple_prices_doubled = [2*i for i in apple_prices]
apple_prices_lowered = [i-100 for i in apple_prices]

apple_prices_doubled
apple_prices_lowered

## 5. Counting Female Names ##

"""
Create an empty dictionary called name_counts.
Loop through each row in legislators.
If the gender column of the row equals F and the year column is greater than 1940:
Assign the first_name column of the row to the variable name.
If name is in name_counts:
Add 1 to the value associated with name in name_counts.
If name isn't in name_counts:
Set the value associated with name in name_counts to 1.
When the loop finishes, name_counts should contain each unique name in the first_name column of legislators as a key, and the corresponding number of times it appeared as the value.
"""
"""
# Raw Code - Straight out of mind
dictnry = {}
date_year = []
for i in legislators:
    date_year = (i[2].split("-"))
    date_year = date_year[0]
    if (date_year > '1940') and (i[3] == "F"):
        fname = i[1]
        if fname not in dictnry:
            dictnry[fname] = 1
        else:
            dictnry[fname] += 1
dictnry
# how to remove keys from dictnry based on values??
"""
name_counts = {}
for i in legislators:
    if i[7] > 1940 and i[3] == "F":
        fname = i[1]
        if fname not in name_counts:
            name_counts[fname] = 1
        else:
            name_counts[fname] += 1
name_counts
        

            

        