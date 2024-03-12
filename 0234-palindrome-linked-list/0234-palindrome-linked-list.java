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
    public boolean isPalindrome(ListNode head) {
        if(head==null){
            return true;
        }
        ListNode temp=head;
        ArrayList<Integer> l = new ArrayList<>();
        while(temp!=null){
            l.add(temp.val);
            temp=temp.next;
        }
        int i=l.size()-1;
        ListNode temp2=head;
        while(temp2!=null && i>=0){
            if(l.get(i)!=temp2.val){
                return false;
            }
            temp2=temp2.next;
            i-=1;
        }
        return true;
        
    }
}