## 1. The Data Set ##

# Weather has been loaded in.
first_element = weather[1]
print(first_element)
last_element  = weather[len(weather)-1]
print(last_element)

## 3. Practice Populating a Dictionary ##

superhero_ranks = {}
superhero_ranks["Aquaman"] = 1
superhero_ranks["Superman"] = 2

## 4. Practice Indexing a Dictionary ##

president_ranks = {}
president_ranks["FDR"] = 1
president_ranks["Lincoln"] = 2
president_ranks["Aquaman"] = 3
fdr_rank = president_ranks["FDR"] 
lincoln_rank = president_ranks["Lincoln"]
aquaman_rank = president_ranks["Aquaman"]

## 5. Defining a Dictionary with Values ##



animals = {
    7:"raven",
    8:"goose",
    9:"duck"
}


times  = {
    "morning":9,
    "afternoon":14,
    "evening":19,
    "night":23
}

## 6. Modifying Dictionary Values ##

students = {
    "Tom": 80,
    "Jim": 70+5,
    "Ann": 85
}

## 7. The In Statement and Dictionaries ##

planet_numbers = {"mercury": 1, "venus": 2, "earth": 3, "mars": 4}
jupiter_found = "jupiter" in planet_numbers
earth_found = "earth" in planet_numbers

## 9. Practicing with the Else Statement ##

planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Uranus"]
short_names = []
long_names = []

for planet in planet_names:
    if len(planet) > 5:
        long_names.append(planet)
    else:
        short_names.append(planet)
        

## 10. Counting with Dictionaries ##

pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]

#Declaring a dictionary to do the counting in a smart way:
pantry_counts = {}
for i in pantry:
    if i in pantry_counts:
        pantry_counts[i] += 1
    else:
        pantry_counts[i]=1

print(pantry_counts)
     

## 11. Counting the Weather ##

weather_counts = {}

for i in weather:
    if i in weather_counts:
        weather_counts[i] += 1
    else:
        weather_counts[i] = 1
        
print(weather_counts)