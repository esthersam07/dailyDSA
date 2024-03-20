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
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        
        ListNode l = list1;
        int i=0;
        while(i!=a-1){
            l=l.next;
            i+=1;
        }
        ListNode r = l;
        int j=i;
        while(j!=b){
            r=r.next;
            j+=1;
        }
        ListNode temp2=list2;
        while(temp2.next!=null){
            temp2 = temp2.next;
        }
        
        l.next=list2;
        temp2.next=r.next;
        r.next=null;
        
        return list1;
        
    }
}