//https://leetcode.com/problems/add-two-numbers/
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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode l = new ListNode(0);
        ListNode curr = l;
        int c = 0;
        while(l1!=null || l2!=null){
            int x = (l1!=null)?l1.val:0;      
            int y = (l2!=null)?l2.val:0;
            int s = x+y+c;
            c = s/10;
            curr.next = new ListNode(s%10);
            curr=curr.next;
            if(l1!=null)l1=l1.next;
            if(l2!=null)l2=l2.next;
        }
        if(c>0){
            curr.next = new ListNode(c);
        }
        
        
        return l.next;
    }
}