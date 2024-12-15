class TreeNode:
    def __init__(self, data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self, child): 
        child.parent=self
        self.children.append(child)

    def get_level(self):  #for root level is 0, next is level 1 and next is level 2 and so on 
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level

    def print_tree(self):   #to print a tree, you can apply recursion on the root node, so that it prints the tree recursively till it reaches the leaf nodes. 
        spaces = ' ' *self.get_level()*3       #for each level - 3 spaces 
        prefix=spaces + "|__" if self.parent else""  #ternary operator
        print(prefix + self.data)      #adding spaces to the print stmt to make tree look hierarchical
        if len(self.children)>0:
            for child in self.children:
                child.print_tree() 

def build_product_tree():
    root=TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    print (tv.get_level())  #prints level as 1 

    return root

if __name__=='__main__':
    root=build_product_tree()
    print(root.get_level())  #prints 0 
    root.print_tree()
    pass
