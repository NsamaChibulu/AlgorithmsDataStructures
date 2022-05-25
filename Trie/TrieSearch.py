def search(self, word):
    currentNode = self.root

    for char in word:
        #If the current node has a child key with current character
        if currentNode.Children.get(char):
            #Follow the child node
            currentNode = currentNode.children[char]
        else:
            #If current character isn't found among
            #the current nodes children, our search word
            #must be in the trie
            return None 
        
    return currentNode
