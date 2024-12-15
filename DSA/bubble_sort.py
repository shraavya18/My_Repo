#bubble sort implementation  - code basics YT Playlist

def bubble_sort(elements):
    size=len(elements)

    for k in range(size-1):
        swapped=False
        for i in range(size-1-k):   #already sorted elements are ignored bcz of -i
            if elements[i]>elements[i+1]:
                tmp=elements[i]
                elements[i]=elements[i+1]
                elements[i+1]=tmp
                swapped=True
        if swapped==False:     #used to handle already sorted arrays, so that iterations will be skipped
            break

def bubble_sort_key(elements, key=None):
    size=len(elements)

    for i in range(size-1):
        swapped=False
        for j in range(size-1-i):
            a=elements[j][key]
            b=elements[j+1][key]
            if a>b:
                tmp=elements[j]
                elements[j]=elements[j+1]
                elements[j+1]=tmp
                swapped=True
        if not swapped:
            break 

if __name__=='__main__':
    elements=[5,9,2,1,67,34,88,34]
    element_strings = ["mona", "dhaval", "aamir", "tina", "chang"]
    bubble_sort(elements)
    print(elements)
    bubble_sort(element_strings)
    print(element_strings)

    elements_key = [
            { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
            { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
            { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
            { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        ]
    bubble_sort_key(elements_key, key='transaction_amount')
    print(elements_key)

