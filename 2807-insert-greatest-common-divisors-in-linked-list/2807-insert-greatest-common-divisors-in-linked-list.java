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
        ListNode i = head;
        ListNode j = head.next;
        while(j!=null){
            int gcd = gcd(i.val,j.val);
            i.next = null;
            ListNode n = new ListNode(gcd,j);
            i.next = n;
            i = i.next.next;
            j = j.next;
        }
        return head;
    }
}