## 1. Overview ##

f = open("movie_metadata.csv",'r')
data = f.read()
rows = data.split("\n")
movie_data = []

for i in rows:
    movie_data.append(i.split(","))
print (movie_data[0:5])


## 3. Writing Our Own Functions ##

"""Write a function, with a definition, name, argument(s), body and return value, that returns a list containing the names of the movies in movie_data. This function is expected to behave similar to first_elt(), but for multiple lists."""
def first_elements(ip_lst):
    dum_list = []
    for i in ip_lst:
        dum_list.append(i[0])
    return dum_list
   
movie_names = first_elements(movie_data)
print(movie_names[0:5])
    


## 4. Functions with Multiple Return Paths ##

"""Write a function named is_usa() that checks whether or not a movie was made in the United States
"""
wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

# writing a function to work with the schema of movie_metadta.csv:
def is_usa(lst):
    if lst[6] == "USA":
        return True
    else:
        return False
"""
# To check the right index for "USA"
count = 0
for i in wonder_woman:
    if i == "USA":
        print (count)
    count += 1
"""   
wonder_woman_usa = is_usa(wonder_woman)  
print(type(wonder_woman_usa))
print(wonder_woman_usa)

## 5. Functions with Multiple Arguments ##

"""
Because there is more than one argument in this function, the order with which we call the arguments becomes important. for example, equals_str(movie_data[4], "UK") would be correct; however, equals_str("UK",movie_data[4]) would not, because the function expects to get the list first and the string second. If we want to override this, we have to used named arguments instead of the default, positional arguments. If we explicitly write the names of the arguments as we provide them, their positions become unimportant. This means that equals_str(input_str="UK",input_lst=movie_data[4]) does not result in an error. Naming arguments does not add any functionality, but it may embellish the readability of the code, which is important if you are working on a team.
=========================================================================
"""
"""
Write a function index_equals_str() that takes in three arguments: a list, an index and a string, and checks whether that index of the list is equal to that string.

Call the function with a different order of the inputs, using named arguments.

Call the function on wonder_woman to check whether or not it is a movie in color, store it in wonder_woman_in_color, and print the value.
"""

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def index_equals_str(lst, indx, str):
    if lst[indx] == str:
        return True
    else:
        return False

wonder_woman_in_color = index_equals_str(wonder_woman,2,"Color")
print(wonder_woman_in_color)


## 6. Optional Arguments ##

"""
- Write a function named feature_counter() that combines the logic of the index_equals_str() and counter() functions.
- Use this to find out how many of the movies were made in USA, and store the value in num_of_us_movies.
"""

def index_equals_str(input_lst,index,input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False
def counter(input_lst,header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        num_elt = num_elt + 1
    return num_elt

# My function starts here - 
def feature_counter(lst,indx,name_str,header_row = False):
    counter = 0
    if header_row == True:
        lst = lst[1:len(lst)] #subsetting input list by removing the top row 
        
    for elmnt in lst: # looping through the input list
        if elmnt[indx] == name_str: # comparing value of index to name_str
            counter += 1
    return counter # returning the total count

#Calling the function
num_of_us_movies = feature_counter(movie_data,6,"USA",header_row = True)
print(num_of_us_movies)


## 7. Calling a Function inside another Function ##

""" SELF PRACTICE
#list counter function - to count the number of elements in the list of list
def listcounter (lst):
    elemcnt = []
    for elmnt in lst:
        counter  = 0
        for i in elmnt:
            counter += 1
        elemcnt.append(counter) 
    return elemcnt

#Calling function
lists = [["dog","cat","rabbit"],[1,2,3,4],[True]]
list_count = (listcounter(lists))
print(list_count)
=======================================================
END OF SELF PRACTICE""" 


def feature_counter(input_lst,index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt

def summary_statistics(lst):
    dictnry = {}   
    num_japan_films = feature_counter(lst,6,"Japan",True)
    num_color_films = feature_counter(lst,2,"Color",True)
    num_films_in_english = feature_counter(lst,5,"English",True)
    dictnry["japan_films"] = num_japan_films
    dictnry["color_films"] = num_color_films
    dictnry["films_in_english"] = num_films_in_english
      
    return dictnry

summary = summary_statistics(movie_data)
print(summary)