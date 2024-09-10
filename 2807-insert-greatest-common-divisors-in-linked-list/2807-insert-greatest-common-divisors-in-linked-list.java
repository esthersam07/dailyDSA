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
    public int gcd(int a,int b){
        while(a!=0 && b!=0){
            if(a>b){
                a = a-b;
            }
            else{
                b = b-a;
            }
        }
        if(b==0){
            return a;
        }
        return b;
    }
    public ListNode insertGreatestCommonDivisors(ListNode head) {
        if(head.next==null){
            return head;
        }
        //using only one pointer
        ListNode temp = head;
        while(temp.next!=null){
            ListNode n = new ListNode(gcd(temp.val,temp.next.val),temp.next);
            temp.next = n;
            temp = n.next;
        }
        return head;
    }
}