#multiprocessing in python - codebasics YT - refer multithreading before this 
#here 3 processes will run if you check your task manager - one for parent, one for p1, one for p2

import time
import multiprocessing

square_result=[] #to store the result - defined outside the function 
def calc_square(numbers):
    global square_result
    for n in numbers:
        print('square ' + str(n*n))
        square_result.append(n*n)
    print("within a process result is: "+ str(square_result))

def calc_cube(numbers):
    for n in numbers:
        print('cube ' + str(n*n*n))

if __name__ == "__main__":
    arr = [2,3,8]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('result' +str(square_result))  #empty result will come - why? - in multiprocessesing, every process will create a new variable 
    print("Done!")