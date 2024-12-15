#finding sum of elements without recursion 
def find_sum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum 

#same method with recursion 
def find_sum_recursion(n):
    if n==1:
        return 1          #base function - where to stop 
    return n + find_sum_recursion(n-1)

#fibonacci with recursion 
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)

if __name__=='__main__':
    print(find_sum(5))
    print(find_sum_recursion(6))
    print(fib(10))
