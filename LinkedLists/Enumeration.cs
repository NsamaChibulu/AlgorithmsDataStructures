//

LinkedList<int> ints = LinkedListNode<int>(); // Create a list of integers
ints.AddTail(1);   // Build the list with values 1,2,3 
ints.AddHead(2);
ints.AddTail(3);



foreach (int value in ints) /// enumerates from head to tail 
{
    Console.WriteLine(value); //Print out list of values 1,2,3
}

