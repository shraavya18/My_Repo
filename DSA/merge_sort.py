#merge sort implementation - can be done more efficiently without using many intermediate arrays to reduce the space complexity
#concept your channel, code - codebasics 
def merge_two_sorted_arrays(a,b): #merge() function 
    sorted_list=[]
    len_a=len(a)
    len_b=len(b)
    i=j=0
    while i<len_a and j<len_b:
        if a[i]<=b[j]:
            sorted_list.append(a[i])
            i=i+1
        else:
            sorted_list.append(b[j])
            j=j+1
    while i<len_a:
        sorted_list.append(a[i])
        i=i+1
    while j<len_b:
        sorted_list.append(b[j])
        j=j+1
    return sorted_list

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]   #slicing
    right=arr[mid:]

    left=merge_sort(left)
    right=merge_sort(right)

    return merge_two_sorted_arrays(left,right)

if __name__=='__main__':
    # a=[1,2,15,16]
    # b=[7,9,45,51]
    # print(merge_two_sorted_arrays(a,b))
    arr= [10,3,15,7,8,8,23,98,29]
    print(merge_sort(arr))

