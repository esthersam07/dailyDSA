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
    public void reorderList(ListNode head) {
        //find middle
        ListNode s = head;
        ListNode f = head;
        while(f!=null && f.next!=null){
            s=s.next;
            f=f.next.next;
        }
        ListNode sec = s.next;// starting of second half
        
        //reverse second half
        s.next = null; //end of first half pointing to null
        ListNode prev = null;
        while(sec!=null){
            ListNode front = sec.next;
            sec.next = prev;
            prev = sec;
            sec = front;
        }
        ListNode l = head;
        ListNode r = prev;
        
        // do the reorder
        while(l!=null && r!=null){
            ListNode tmp1 = l.next;
            ListNode tmp2 = r.next;
            l.next = r;
            r.next = tmp1;
            l=tmp1;
            r=tmp2;
        }
        return;
    }
}