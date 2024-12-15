class BinarySearchTreeNode:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None 

    def add_child(self, data):
        if data==self.data:
            return 
        if data<self.data:
            #add data into left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinarySearchTreeNode(data)
        else:
            #add data to right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements=[]
        #visit left node
        if self.left:
            elements+=self.left.in_order_traversal()

        #visit the root node 
        elements.append(self.data)

        #visit right node 
        if self.right:
            elements+=self.right.in_order_traversal()

        return elements
    
    def search(self, val):
        if self.data==val:
            return True
        
        if val<self.data:
            #the value might be in left sub tree
            if self.left:  #if element exists in left 
                return self.left.search(val)
            else:
                return False
        
        if val>self.data:
            #value might be in right sub tree
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    def find_max(self):
        if self.right is None: #checking only right is enough bcz anyway the max data will be in the right sub tree only 
            return self.data
        return self.right.find_max() 
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def delete(self, val):
        if val<self.data:
            if self.left:
                self.left=self.left.delete(val)
        elif val>self.data:
            if self.right:
                self.right=self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left  

            min_val=self.right.find_min() 
            self.data=min_val
            self.right.delete(min_val)
        return self        

def build_tree(elements):
    root=BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root 
    
if __name__=='__main__':
    #numbers=[17,4,1,20,9,23,18,34]
    numbers=[17,4,1,20,9,23,18,34,18,34] #list with duplicates - it will remove the duplicate elements  
    number_tree=build_tree(numbers)
    print(number_tree.in_order_traversal())
    print(number_tree.search(20))
    print(number_tree.search(21))
    number_tree.delete(20)
    print(number_tree.in_order_traversal())  #after deleting element 20 

    #bst with string data type
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)
    print(country_tree.in_order_traversal())

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))