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
        Map<ListNode,Integer> m = new HashMap<>();
        while(temp!=null){
            if(m.containsKey(temp)){
                return true;
            }
            m.put(temp,temp.val);
            temp=temp.next;
        }
        return false;
    }
}