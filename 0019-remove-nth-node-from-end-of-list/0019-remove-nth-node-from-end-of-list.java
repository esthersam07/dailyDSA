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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode temp2 = head;
        int l=0;
        while(temp2!=null){
            temp2=temp2.next;
            l+=1;
        }
        if(l==n){
            ListNode newHead = head.next;
            return newHead;
        }
        int res = l-n;
        ListNode temp=head;
        while(temp!=null){
            res--;
            if(res==0){
                break;
            }
            temp=temp.next;
        }
        ListNode del = temp.next;
        temp.next = temp.next.next;
        return head;
    }
}