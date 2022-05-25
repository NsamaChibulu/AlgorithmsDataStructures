def insert(self, word):
    currentNode = self.root
    for char in word:
        #If the current node has a child key with current characger
        if currentNode.children.get(char):
            #follow the child node
            currentNode = currentNode.Children[char]
        else:
            #if the current character isn't found among
            #the current nodes children,we add
            #the character as a new child node
            newNode = TrieNode()
            currentNode.children[char] = newNode

            #follow this new node
            currentNode = newNode

    # After inserting the entire word into the trie
    # we add the * ket at the end
    currentNode.children['*'] = None