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
        ListNode l = new ListNode();
        ListNode r = new ListNode();
        int i=-1;
        ListNode temp = list1;
        while(i!=b){
            i+=1;
            if(i==a-1){
                l = temp;
            }
            else if(i==b){
                r = temp;
            }
            temp=temp.next;
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