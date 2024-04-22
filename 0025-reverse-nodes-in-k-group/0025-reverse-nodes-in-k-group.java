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
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dum = new ListNode(0,head);
        ListNode prev = dum;
        ListNode curr = dum;
        
        while(curr.next!=null){
            for(int i=0;i<k && curr!=null;i++){
                curr = curr.next;
            }
            if(curr==null){
                return dum.next;
            }
            ListNode nextIterNode = curr.next;
            curr.next = null;
            ListNode start = prev.next;
            prev.next = reverse(start);
            start.next = nextIterNode;
            prev = start;
            curr = prev;
        }
        return dum.next;
    }
    public ListNode reverse(ListNode head) {
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
}