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

def deletion(valueToDelete, node):
    #the base case is when we've hit the bottom of the tree
    # and the parent node has no children
    if node is None:
        return None
    
    #If the value we are deleting is less or greater than the current
    # we set the left or right child respectively to be 
    # the return value of the recursive call of this
    # very method on the current 
    # nodes left or right subtree
    
    elif valueToDelete < node.value:
        node.leftChild = delete(valueToDelete, node.leftChild)
        
        # We return the current node (and its subtree if existent) to 
        # be used as the new value of uts parents left or right child
        return node
    elif valueToDelete > node.value:
        node.rightChild = delete(valueToDelete,node.rightChild)
        return node

    # If the current node is the one we want to delete
    elif valueToDelete == node.value:

        # if the current node has no left child, try to delete it by 
        # returning its right child (and it subtree if existent)
        # to be its parent's new subtree
        if node.leftChild is None:
            return node.rightChild

            #(if the current node has no left or right child, this ends up
            # being None as per the first line of in code in this function)

        elif node.rightChild is None:
            return node.leftChild

            #If the current node has two children, we delete the current node
            #by calling the lift function
            # which changes the  urrent node's
            # value to the value of its successor node

        else:
            node.rightChild = life(node.rightChild, node)
            return node
        
def lift(node, nodeToDelete):

    # If the current node of this function has a left child, 
    # we recursively call this function to continue down 
    # the left subtree to find the successor node
    if node.leftChild:
        node.leftChild = lift(node.leftChild, nodeToDelete)
        return node
    
    # If the current node has no left child, that means the current node
    # of this function is the successor node, we take its value 
    # and make it the new value of the node that we're deleting
    else:
        nodeToDelete = node.value
        # We return the successor node's right child to be now used 
        # as its parents left child
        return node.rightChild

def traverse_and_print(node):
    if node is None:
        return
    traverse_and_print(node.leftChild)
    print(node.value)
    traverse_and_print(node.rightChild)
