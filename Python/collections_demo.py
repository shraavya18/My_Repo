#collections - extension of lists, tuples, dict... with some more additional features 
#There are so many collections, but we are going to learn about 5 of them 
# Counter, namedtuple, OrderedDict, defaultdict, deque 

#1. Counter  - will store the elements as dict keys and their count as values 
from collections import Counter
c='aaaabbbcccddddeeeeffffdddd'  
my_counter=Counter(c)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1))
print(my_counter.most_common(2))
print(my_counter.elements())

#works on lists also 
list_demo=['apple', 'banana', 'orange','apple','kiwi', 'grapes','banana', 'orange','apple','kiwi', 'grapes', 'banana']
my_list_counter=Counter(list_demo)
print(my_list_counter)

#namedtuple 
from collections import namedtuple
Point=namedtuple('Point', 'x,y')  #first arg is Point and second arg (x,y) are co ordinates of the point 
pt=Point(1,-4)
print(pt)
print(pt.x)

#ordered dictionaries - regular dictionary but they remember the order of insertion 
#but from Python 3.7, regular dictionary also remembers their order of creation - so ordereddict is not so used 
from collections import OrderedDict
ordered_dict=OrderedDict()
ordered_dict['a']=1
ordered_dict['b']=2
ordered_dict['c']=3
ordered_dict['d']=4
print(ordered_dict)  #prints in the order inserted 

#defaultdict 
from collections import defaultdict
d=defaultdict(int)  #if no key is specified, give the default value of int which is 0 or default value of datatype specified
d['a']=1
d['b']=2
d['c']=3
print(d)
print(d['a'])  #returns 1 
print(d['d'])  #returns 0 - default value of integer, in regular dict it will throw key error if we try to access a key that is not specified

#deque - double ended queue - used for implementation of stack and queue 
#insertion and deletion can be done from both the ends 
from collections import deque
d=deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)
d.pop()
d.popleft()
print(d)
d.extend([3,4,5])
d.extendleft([5,6,7])
print(d)
d.rotate(1) # all vlaues will be moved by one place to right 
d.rotate(-1) #moved one place to the left 