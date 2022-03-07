// Remove algorithm 
// finds the node to delete , removes the found node

//Three cases
// Empty list, single node and multiple nodes


// Removes the first occurance of the item from the list (searching from Head to tail)
// <param name ="item"> the item to remove </param>
// returns True if item was found and removed , false otherwise

class removing
{
    public bool Remove(T item)
    {
        DoublyLinkedListNode<T> found = Find(item);
        if (found == null)
        {
            return false;
        }

        DoublyLinkedListNode<T> previous = found.Previous;
        DoublyLinkedListNode<T> next = found.Next;

        if (previous == null)
        {
            //removing the head 
            Head = next;
            if (Head != null)
            {
                Head.Previous = null;
            }
        }
        else
        {
            previous.Next = next;
        }
        if (next == null)
        {
            //we're removing the tail
            Tail = previous;
            if (Tail != null)
            {
                Tail.Next = null;
            }
        }
        else
        {
            next.Previous = previous;
        }
        Count--;

        return true;
    }

    //
}

