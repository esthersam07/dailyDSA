/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || k == 0) return head;

        // Calculate the length of the list and find the tail
        int length = 1;
        ListNode tail = head;
        while (tail.next != null) {
            tail = tail.next;
            length++;
        }

        // Calculate the effective rotation
        int effectiveRotation = k % length;
        if (effectiveRotation == 0) return head;

        // Find the new tail node
        ListNode newTail = head;
        for (int i = 1; i < length - effectiveRotation; i++) {
            newTail = newTail.next;
        }

        // Set the new head and break the list
        ListNode newHead = newTail.next;
        newTail.next = null;

        // Connect the original tail to the original head to form a circular structure
        tail.next = head;

        return newHead;
    }
}
