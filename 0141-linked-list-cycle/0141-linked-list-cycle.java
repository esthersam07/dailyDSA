/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode temp = head;
        ArrayList<ListNode> l = new ArrayList<>();
        while(temp!=null){
            if(l.contains(temp)){
                return true;
            }
            l.add(temp);
            temp=temp.next;
        }
        return false;
    }
}