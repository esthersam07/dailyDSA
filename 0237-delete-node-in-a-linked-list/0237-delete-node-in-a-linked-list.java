/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {
        //delete the node by copying the next value to the given node and the next value's next to the current node's next
        node.val=node.next.val;
        node.next=node.next.next;
    }
}