#multithreading in python - codebasics YT Channel 

#lets say we have 2 methods to find squares and cubes 

import time
import threading

def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.5)  #waits for 0.5 second before moving to next 
        print('square:',n*n)

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.5)
        print('cube:',n*n*n)

arr = [2,3,8,9]

t=time.time()
# calc_square(arr)
# calc_cube(arr)

# print("done in : ",time.time()-t)   #done in 4.02 seconds without multithreading
# print("done")

#instead of calling the functiond directly, now we will use threading 
t1=threading.Thread(target=calc_square, args=(arr,))   #creating a thread 
t2=threading.Thread(target=calc_cube,args=(arr,))

t1.start()  #starting a thread 
t2.start()

t1.join()   #it signals the main thread to wait until the t1's execution is completed
t2.join()

print("done in : ",time.time()-t)   #done in 2.00 seconds with multithreading
print("done")
