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
    public ListNode mergeNodes(ListNode head) {
        ListNode newHead = new ListNode(-1);
        ListNode temp = newHead;
        ListNode l = head;
        ListNode r = head.next;
        while(r!=null){
            int res = 0;
            while(r.val!=0){
                res += r.val;
                r = r.next;
            }
            l = r;
            r = l.next;
            ListNode node = new ListNode(res);
            temp.next = node;
            temp = node;
        }
        return newHead.next;
        
    }
}