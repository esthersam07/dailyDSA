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
    public ListNode detectCycle(ListNode head) {
        ListNode temp = head;
        int ind = 0;
        Map<ListNode,Integer> m = new HashMap<>();
        while(temp!=null){
            if(m.containsKey(temp)){
                return temp;
            }
            m.put(temp,ind++);
            temp=temp.next;
        }
        return null;
    }
}