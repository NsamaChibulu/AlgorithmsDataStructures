/**
 * Write a function to delete a node in a singly-linked list. You will not be
 * given access to the head of the list, instead you will be given access to the
 * node to be deleted directly.
 * 
 * It is guaranteed that the node to be deleted is not a tail node in the list.
 */

package LinkedLists.exercises;

class Solution {
    public void deleteNode(ListNode2 node) {
        // Define number of nodes
        ListNode2 prev = node;
        ListNode2 curr = node;
        prev = prev.next;
        curr.val = prev.val;
        curr.next = prev.next;

    }
}