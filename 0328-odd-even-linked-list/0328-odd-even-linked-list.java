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
    public ListNode oddEvenList(ListNode head) {
        if(head==null || head.next==null){
            return head;
        }
        ListNode odd=head;
        ArrayList<Integer> values = new ArrayList<>();
        
        while (odd != null && odd.next!=null) {
            values.add(odd.val);
            if (odd.next != null) {
                odd = odd.next.next;
            } else {
                break;
            }
        }
        if(odd!=null){
            values.add(odd.val);
        }
        ListNode even=head.next;
        while (even != null && even.next!=null) {
            values.add(even.val);
            if (even.next != null) {
                even = even.next.next;
            } else {
                break;
            }
        }
        if(even!=null){
            values.add(even.val);
        }
        ListNode temp=head;
        int i=0;
        while(temp!=null && i<values.size()){
            temp.val=values.get(i);
            i+=1;
            temp=temp.next;
        }
        return head;
    }
}