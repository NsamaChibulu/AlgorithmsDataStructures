DoublyLinkedListNode<int> ints = new DoublyLinkedList<int>();
for (int i = 1; i <= 5; i++)
{
    ints.AddHead(i);
}

// Hear we have created a linked list of integers and we're going to iterate in a for loop five times
// calling AddHead repeatedly each time using the values 1,2,3,4,5.

// First time we call AddHead, we call the value 1.
// This creates a linked list with a single node in it. It has the value 1, 
// and both previous and next are null because this is the only node in the list/

// When we call AddHead a second time, the value 2 is now the head of the list. The 2 Nodes' next
// number refers to the 1 node, and the 1 nodes' previous nemeber refers to the 2 node.

class adding
{
    public void AddHead(T Value) // Adding a value to the head (start) of the list 
    {
        DoublyLinkedListNode<T> adding = new DoublyLinkedListNode<T>(value, null, head); // allocate the new node

        if (AddHead != null) // if there was an existing head node
        {
            head.Previous = adding; // update its previous pointer to the new node
        }

        head = adding; // Set the head pointer to the new node

        if (tail == null) // if the list was empty (tail is null)
        {
            tail = head;
        }

        Count++; // increment the Count value (items in list)
    }
}
