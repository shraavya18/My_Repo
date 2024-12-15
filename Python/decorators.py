#decorators 

#lets say we have 2 functions to calculate square and cube of numbers and you also find out the time taken for each function 

import time

#for the below two programs, the main purpose is to find squares or cubes but time logic is also there 
#also, you are writing the same code for 2 times - if 100 functions - 100 times 

'''
def cal_square(numbers):
    start_time=time.time()   #extra code for measuring time 
    result=[]
    for num in numbers:
        result.append(num*num)
    end_time=time.time()   #extra code
    print(f"calculate squares took str({end_time-start_time}) seconds") #extra code 
    return result

def cal_cube(numbers):
    start_time=time.time()   ##extra code for measuring time 
    result=[]
    for num in numbers:
        result.append(num*num*num)
        end_time=time.time()  #extra code 
    print(f"calculate cubes took str({end_time-start_time}) seconds")  #extra code 
    return result 

array=range(1,100000)
squares=cal_square(array)
cubes=cal_cube(array)

'''

#same logic with decorators 

def time_it(func):   #wrapper function 
    def wrapper(*args, **kwargs):
        start=time.time()
        result=func(*args, **kwargs)
        end=time.time()
        print(func.__name__ + "took " +str(end-start) +"seconds")
        return result 
    return wrapper


#same above fucntions 

@time_it     #decorating the fucntion with time_it()
def cal_square(numbers):
    result=[]
    for num in numbers:     #no timing code but still you can get the time, because of decorator 
        result.append(num*num)          #you can get cleaner code now which only has squares logic and no duplication of code 
    return result

@time_it
def cal_cube(numbers):
    result=[]                     
    for num in numbers:
        result.append(num*num*num)
    return result 

array=range(1,100000)
squares=cal_square(array)   #put a debug here, it will first take you to time_it function, then only squares 
cubes=cal_cube(array) 