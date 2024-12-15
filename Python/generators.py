#similar to iterators, but they dont need an extra memory for storing the list or tuple or....

#iterator implementation 
a=list(range(1,6))
iter_var=iter(a)      #making a as an iterable using iter() method 
print(next(iter_var))  #prints 1 
print(next(iter_var))  #prints 2 
print(next(iter_var)) 

print("--------------")

#same thing using generator 
def numbers():        #here numbers is generator not a function, it is having yield keyword not return
    for i in range(5):   #no need to have a list here, the memory is saved. 
        yield i

def squares(sequence):  
    for num in sequence:
        yield num**2

for i in numbers():  #using the generator as an iterable 
    print(i)

for val in squares(numbers()):
    print(val)

print("---------------")

for i in range(5):      #this simple for loop also does the same thing then what is the use of generators 
    print(i)    #here it just prints numbers and if you want to do any further operations on these numbers like finding squares you cant do that,  
                #but with generators they can be futher processed 


#fibonacci series using generator
def fibonacci():
    a,b=0,1
    while True:
        yield a 
        a,b=b,a+b

fib=fibonacci()
for _ in range(10):
    print(next(fib))