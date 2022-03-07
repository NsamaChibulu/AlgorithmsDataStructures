//Creating a linked list class, adding items to it , iterating over the items
using System.Collections;

namespace DataStructures
{
    //A Node in a LinkedList. This node class below contains the node value 
    // and the next and previous memebers 
    public class DoublyLinkedListNode<T>
    {
        //Constructs a new node with the specified value.
        public DoublyLinkedListNode(T value)
        {
            Value = value;
        }
        // The node value 
        public T value { get; set; }

        //The next node in the linked list (null if last node)
        public DoublyLinkedListNode<T> Next { get; set; }
        // The previous node in the linked list (null if first node)
        public DoublyLinkedListNode<T> Previous { get; set; }

    }

    // Doubly linked list class below contains the head and tail nodes. And through the 
    // head and tail nodes' previous and next members, you can access all of the nodes in the 
    // linked list. 
    public class DoublyLinkedList<T> : System.Collections.Generic.ICollection<T>
    {
        // <summary>
        // the first node in the list or null if empty 

        public DoublyLinkedListNode<T> Head
        {
            // nodes can be accessed publicly but set priavtely 
            // This allows the user of the list to quickly check whats at the
            // start and the end of the list. 
            get;
            private set;
        }

        public DoublyLinkedListNode<T> Tail
        {
            get;
            private set;
        }

        // 
    }

}