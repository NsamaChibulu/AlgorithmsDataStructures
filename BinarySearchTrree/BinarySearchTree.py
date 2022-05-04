class TreeNode:
    def __init__(self,val,left=None, right=None):
        self.value = val
        self.leftChild = left
        self.rightChild = right

        node1 = TreeNode(25)
        node2 = TreeNode(75)
        root = TreeNode(50, node1, node2)
    
def search(searchValue, node):
    #Base cas: if the node is none existent
    #or we've found the value we're looking for
    if node is None or node.value == searchValue:
        return node
    #If the value is greater than the current node, 
    #perform serch on left child
    elif searchValue < node.value:
        return search(searchValue, node.leftChild)
    else:
        return(search(searchValue, node.rightchild))

def insert(value, node):
    if value < node.value:
        #if the left child doesn't exist, we want to insert
        #the value as the left child
        if node.leftChild is None:
            node.leftChild = TreeNode(value)
        else:
            insert(value, node.leftChild)
    elif value > node.value:
        #if the right child does not exist, we want to insert
        # the value as the right child
        if node.rightChild is None:
            node.rightChild = TreeNode(value)
        else:
            insert(value, node.rightChild) 
