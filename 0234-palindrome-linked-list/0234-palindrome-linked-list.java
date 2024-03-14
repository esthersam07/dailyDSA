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
        ArrayList<Integer> n = new ArrayList<>();
        ListNode temp=head;
        while(temp!=null){
            n.add(temp.val);
            temp=temp.next;
        }
        int l=0;
        int r=n.size()-1;
        while(l<=r){
            if(!n.get(l).equals(n.get(r))){
                return false;
            }
            l+=1;
            r-=1;
        }
        return true;
    }
}