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
    public ListNode reverse(ListNode head){
        ListNode temp = head;
        ListNode prev = null;
        while(temp!=null){
            ListNode front = temp.next;
            temp.next = prev;
            prev = temp;
            temp = front;
        }
        return prev;
    }
    public ListNode doubleIt(ListNode head) {
        ListNode reversed = reverse(head);
        ListNode current = reversed;
        ListNode prev = null;
        int carry = 0;

        while (current != null) {
            int sum = current.val * 2 + carry;
            current.val = sum % 10;
            carry = sum / 10;
            prev = current;
            current = current.next;
        }

        if (carry > 0) {
            prev.next = new ListNode(carry);
        }

        return reverse(reversed);
    }
}