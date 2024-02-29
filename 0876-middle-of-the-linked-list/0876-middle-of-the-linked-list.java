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
    public ListNode middleNode(ListNode head) {
        int l=0;
        ListNode temp=head;
        while(temp!=null){
            l+=1;
            temp=temp.next;
        }
        int c=0;
        ListNode temp2=head;
        if(l%2==0){
            int m=l/2;
            while(c<m){
                c+=1;
                temp2=temp2.next;
            }
            return temp2;
            
        }else{
            int m=l/2;
            while(c<m){
                c+=1;
                temp2=temp2.next;
            }
            return temp2;
        }
        
    }
}