#sets and frozen sets 
#sets - unordered and mutable, no duplicate elements 
#frozenset - immutable 

#initializing a set 
empty_set=set()
print(type(empty_set))   #prints the type as set 

a={}
print(type(a))  #Prints dict if empty curly braces are used, it takes as dictionary

my_set={1,2,3,4,5}
print(type(my_set))  #now it prints set bcz there are elements between the curly braces 

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers=set(numbers)  #converts numbers into a set = removes the duplicate elements 
print(unique_numbers)  

for i in my_set:  #iterating through a set 
    print(i)

#basic set operations 
my_set.add(6)    #value to add should be passed, not index - no indexing bcz elements are unordered 
print(my_set)

my_set.remove(6)  #removes 6
print(my_set)

#my_set.remove(8)  #error bcz 8 is not there in the set 
my_set.discard(9)  #will not throw error even though 9 is not in the set 

print(2 in my_set)   #checks if 2 is in the set or not - returns True
print(10 in my_set)     #returns False 
 
my_set.clear()   #clears up a set 
print(my_set)

#set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

#union - 2 ways - or operator, keyword 
print(set_a | set_b)
print(set_a.union(set_b))

#intersection 
print(set_a & set_b)
print(set_a.intersection(set_b))

#difference 
print(set_a-set_b)
print(set_b.difference(set_a))

#symmetric_difference - Finds elements in either set but not both.
print(set_a^set_b)
print(set_a.symmetric_difference(set_b))

#copy 
my_set = {1, 2, 3}
new_set = my_set.copy()
print(new_set)  

#subset and superset 
set_a = {1, 2}
set_b = {1, 2, 3}

print(set_a.issubset(set_b))  # Output: True
print(set_b.issuperset(set_a))  # Output: True
print(set_a<set_b)   #checks if subset or not 

#disjoint sets 
set_a = {1, 2}
set_c = {3, 4}

print(set_a.isdisjoint(set_c))  # Output: True


#frozen set - immutable - cannot add or remove elements from it 
frozen=frozenset([1,2,3,4])
print(frozen)
#frozen.add(5)   #raises an exception bcz it is a frozenset 

 


