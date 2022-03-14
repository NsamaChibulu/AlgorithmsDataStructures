
package LinkedLists.Exercises;

// step one ; Parse limked list and to retrive the digit sequence for the binary number 
// step two ; convert binary to decimal 

//Definition for singly-linked list.

class Solution {

    public int getDecimalValue(ListNode head) {
        int num = head.val; // initialize result number to be equal to head value
        while (head.next != null) // Parse linked list starting from the head: while head.next
        {
            num = num * 2 + head.next.val;
            head = head.next;
        }

        return num;

    }
}

// Time complexity: \mathcal{O}(N)O(N).

// Space complexity:\mathcal{O}(1)O(1)
