package LinkedLists;

//linked list Intro
class Node
{
    public Node(int value)
    {
        this.Value = value; // Value being stored
        this.Next = null; // references the next node to say thats its null



        Node head = new Node(1); // Single node with the value 1. The value is one and the next property is null, meaning its
        // not referring to another node
        head.Next = new Node(2); // this nodes value is too and we've referenced updated the first nodes next memeber to reference this node
        head.Next.Next = new Node(3); // third node


    }

    public Node Next;
    public int Value;
}

//Singly linked List Node

class LinkedListNode<TNode>
{
    public LinkedListNode(TNode value, LinkedListNode<TNode> next = null)
    {
        this.Value = value;
        this.Next = next;
    }
    public LinkedListNode<TNode> Next;
    public TNode Value;
}

//Doubly linked lis 
class Nodee
{
    public Nodee(int value)
    {
        this.Value = value;
        this.Previous = null; //reference to previous node
        this.Next = null;
    }
    public Nodee Previous;
    public Nodee Next;
    public int Value;
}

class DoublyLinkedListNode<TNode>
{
    public DoublyLinkedListNode
    (TNode value,
    Node<TNode> prev = null,
    Node<TNode> next = null)
    {
        this.Value = value;
        this.Previous = null; //reference to previous node
        this.Next = null;
    }

    public Nodee Previous;
    public Nodee Next;
    public int Value;
}

