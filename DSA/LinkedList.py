class Node:
    def __init__(self, data=None, next=None):
        self.data=data   #data refers to the data stored in LL
        self.next=next #next refers to the address of the next element

class LinkedList:
    def __init__(self):
        self.head=None #head refers to the first node

    #various methods using Linkedlists
    def insert_at_beginning(self, data):  #taking data and inserting a node at beginning
        node=Node(data, self.head)  #node is an object of Node class, it is an object that we are trying to insert into LL
        self.head=node  #since we are inserting at beginning, it is pointed as head    

    def print(self):
        if self.head is None:  #this means ll is empty
            print("My Linked List is empty")
            return
        
        itr=self.head #iterating variable to go over the linked list
        llstr=''  #empty str to print the LL
        while itr:      #checks till the end of list
            llstr=llstr+str(itr.data) + '-->'
            itr=itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head=Node(data, None)
            return
    
        itr=self.head   #similar to i=0
        while itr.next:
            itr=itr.next

        itr.next=Node(data, None)

    def insert_values(self, data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count=count+1
            itr=itr.next

        return count

    def remove_at(self, index):
        if index<0 or index>=ll2.get_length():
            raise Exception("not a valid index")
        
        if index==0:
            self.head=self.head.next
            return

        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break

            itr=itr.next
            count=count+1

    def insert_at(self, index, data):
        if index<0 or index>=ll2.get_length():
            raise Exception("not a valid index")
        
        if index==0:
            self.insert_at_beginning(data)
            return

        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node = Node(data, itr.next)
                itr.next=node
                break

            itr=itr.next
            count+=1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head==None:
            return

        if self.head.data==data_after:
            self.head.next=Node(data_to_insert, self.head.next)
            return

        itr=self.head
        while itr:
            if itr.data==data_after:
                itr.next=Node(data_to_insert,itr.next)
                break

            itr=itr.next

     # Remove first node that contains data
    def remove_by_value(self, data):
        if self.head==None:
            return
        
        if self.head.data==data:
            self.head=self.head.next

        itr=self.head
        while itr.next:
            if itr.next.data==data:
                itr.next=itr.next.next
                break
            itr=itr.next

if __name__=='__main__':
   ll=LinkedList()  #object of linkedlist class
   ll2=LinkedList()
   ll.insert_at_beginning(5)
   ll.insert_at_beginning(89)
   ll.insert_at_end(79)
   ll.print()
   ll2.insert_values(["banana","mango","grapes","orange"])
   ll2.remove_at(2)
   #ll2.remove_at(-1)
   ll2.insert_at(0,'figs')
   ll2.print()
   ll2.insert_at(2,'jackfruit')
   ll2.print()
   print("length is: ", ll2.get_length())
   