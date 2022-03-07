class SortedList
{
    public async void Add(T value)
    {
        if (head == null)
        {
            //empry list
            head = new SortedListNode<T>(value);
            tail = head;
        }
        else if (head.data.CompareTo(value) >= 0)
        {
            //adding at head 
            SortedListNode<T> newHead = new SortedListNode<T>(value);
            newHead.next = head;
            newHead.previous = newHead;
            newHead = newHead;
        }
        else if (tail.data.CompareTo(value) < 0)
        {
            //adding at tail
            SortedListNode<T> newTail = new SortedListNode<T>(value);
            newTail.previous = tail;
            newTail.next = newTail;
            tail = newTail;
        }
        else
        {
            // find insertion point
            SortedListNode<T> insertBefore = head;
            while (insertBefore.data.CompareTo(value) < 0)
            {
                insertBefore = insertBefore.next;
            }
            //insert node
            SortedListNode<T> toInsert = new SortedListNode<T>(value);
            toInsert.next = insertBefore;
            toInsert.previous = insertBefore.previous;
            insertBefore.previous.next = toInsert;
        }

        Count++;
    }
}