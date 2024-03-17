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
    public ListNode sortList(ListNode head) {
        ArrayList<Integer> l = new ArrayList<>();
        ListNode temp=head;
        while(temp!=null){
            l.add(temp.val);
            temp=temp.next;
        }
        Collections.sort(l);
        int i=0;
        temp=head;
        while(i<l.size() && temp!=null){
            temp.val=l.get(i);
            i+=1;
            temp=temp.next;
        }
        return head;
        
    }
}