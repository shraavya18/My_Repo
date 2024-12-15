#List, set, dictionary comprehensions  - codebasics YT Channel

#regular approach for picking even numbers from list 
numbers=[1,2,3,4,5]
even=[]
for i in numbers:
    if i%2==0:
        even.append(i)
print(even)

#by using list comprehensions - same code 
even_comp=[i for i in numbers if i%2==0] #single line 
print(even_comp)
squares=[i*i for i in numbers]
print(squares)

#set comprehensions - set - unordered, unique
s=set([1,2,3,4,5,6,7,7,6,5,4])   #getting a set out of list
print(s)
even_set={i for i in s if i%2==0}
print(even_set)

#dictionary comprehension 
#consider 2 lists and then lets combine them using zip() function
cities=["mumbai","new york","paris"]
countries=["india","america","france"]
z=zip(cities,countries)   #zip() function combines the two lists and creates a dictionary
for a in z:
    print(a)

dict_comp={city:country for city, country in zip(cities,countries)}
print(dict_comp)