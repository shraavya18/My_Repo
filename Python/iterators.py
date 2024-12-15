#iterators - object used to iterate over a list/tuple/collection...

#using basic for loop for printing 
a=list(range(1,6))
for i in a:
    print(i)     #prints 1 to 20 at a time 

print("----------")

#using an iterator 
iter_var=iter(a)      #making a as an iterable using iter() method 
print(next(iter_var))  #prints 1 
print(next(iter_var))  #prints 2 
print(next(iter_var))  #prints 3 

# Pausing iteration here
# Resuming iteration later

print(next(iter_var)) #prints 4 
print(next(iter_var))  #prints 5 - all elements done 


print(next(iter_var))   #will throw stopiteration exception bcz the size of list is 5 

#with iterators you will have control over the list/tuple... only when required you will print and stop when done. comeback later and print few other elements 
#but with for loop, all elements will be printed at once. 

#for loop  internally implements iter() and next() method

#print(dir(a))   #will give all the possible methods that can be done on variable a based on its datatype 
