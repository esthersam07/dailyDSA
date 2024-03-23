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
        ArrayList<ListNode> l = new ArrayList<>();
        ListNode temp = head.next;
        while(temp!=null){
            l.add(temp);
            temp=temp.next;
        }
        temp=head;
        temp.next=null;
        int lo=0;
        int h=l.size()-1;
        while(lo<=h){
            if(lo==h){
                l.get(h).next = null;
                temp.next = l.get(h);
                h-=1;
                temp=temp.next;
            }else{
                l.get(h).next = null;
                temp.next = l.get(h);
                h-=1;
                temp=temp.next;
                l.get(lo).next = null;
                temp.next = l.get(lo);
                lo+=1;
                temp=temp.next;
            }
        }
        return;
    }
}