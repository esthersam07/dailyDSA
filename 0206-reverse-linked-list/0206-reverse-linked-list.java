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
    public ListNode reverseList(ListNode head) {
        ArrayList<Integer> l = new ArrayList<>();
        ListNode temp=head;
        int count=0;
        while(temp!=null){
            l.add(temp.val);
            count+=1;
            temp=temp.next;
        }
        ListNode temp2=head;
        for(int i=count-1;i>=0;i--){
            temp2.val=l.get(i);
            temp2=temp2.next;
        }
        return head;
    }
}