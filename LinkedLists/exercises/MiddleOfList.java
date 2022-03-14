package LinkedLists.Exercises;



class MiddleOfList {

    /**
     * Put every node into an array A in order. middle node is then just A[A.Length
     * // 2]
     * can initalize the array to be of length 100
     */

    public ListNode middleNode(ListNode head) {
        ListNode[] A = new ListNode[100];
        int t = 0;
        while (head != null) {
            A[t++] = head;
            head = head.next;

        }

        return A[t / 2];
    }

    /**
     * When traversing the list with a pointer slow, make another pointer fast that
     * traverses twice as fast. When fast reaches the end of the list, slow must be
     * in the middle.
     */

    public ListNode midNode(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;

    }

}
