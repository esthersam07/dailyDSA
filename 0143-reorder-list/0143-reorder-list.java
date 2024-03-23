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
    public void reorderList(ListNode head) {
        ArrayList<Integer> l = new ArrayList<>();
        ListNode temp = head;
        while(temp!=null){
            l.add(temp.val);
            temp=temp.next;
        }
        int lo=0;
        int r=l.size()-1;
        ArrayList<Integer> res = new ArrayList<>();
        while(lo<=r){
            res.add(l.get(lo));
            res.add(l.get(r));
            lo+=1;
            r-=1;
        }
        int ind=0;
        temp=head;
        while(temp!=null){
            temp.val=res.get(ind);
            ind+=1;
            temp=temp.next;
        }
        return;
    }
}