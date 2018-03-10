## 2. Parsing the File ##

f = open("la_weather.csv",'r')
data = f.read()
rows = data.split("\n")

weather_data = []
for element in rows:
    weather_data.append(element.split(","))
                        
                        
print(rows[1:3])
print ("\n")
print(weather_data[1:3])

## 3. Getting a Single Column From the Data ##

# weather_data has already been read in automatically to make things easier.
weather = []
for element in weather_data:
    weather.append(element[1])
    

## 4. Counting the Items in a List ##

count = 0
for i in weather:
    count += 1
print(count)

## 5. Removing the Header ##

new_weather = weather[1:len(weather)] 
print(new_weather)

## 6. The In Statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]
cat_found = "cat" in animals
space_monster_found = "space_monster" in animals
    

## 7. Weather Types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []

for i in weather_types:
    weather_type_found.append(i in new_weather)
print(weather_type_found)