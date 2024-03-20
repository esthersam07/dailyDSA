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
        ListNode rOne = new ListNode();
        int i=-1;
        ListNode temp = list1;
        while(i!=b+1){
            i+=1;
            if(i==a-1){
                l = temp;
            }
            else if(i==b){
                r = temp;
            }
            else if(i==b+1){
                rOne = temp;
            }
            temp=temp.next;
        }
        ListNode temp2=list2;
        while(temp2.next!=null){
            temp2 = temp2.next;
        }
        l.next=null;
        l.next=list2;
        r.next=null;
        temp2.next=rOne;
        return list1;
        
    }
}