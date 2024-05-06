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
    public ListNode removeNodes(ListNode head) {
        ListNode temp = head;
        Stack<Integer> stack = new Stack<>();
        while (temp != null) {
            while (!stack.isEmpty() && temp.val > stack.peek()) {
                stack.pop();
            }
            stack.push(temp.val);
            temp = temp.next;
        }
        ListNode dumm = new ListNode();
        temp = dumm;
        for (int i : stack) {
            temp.next = new ListNode(i);
            temp = temp.next;
        }
        return dumm.next;
        
    }
}