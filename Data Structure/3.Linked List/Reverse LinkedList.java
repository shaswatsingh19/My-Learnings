//https://leetcode.com/problems/reverse-linked-list
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
        
        ListNode c = head;
		ListNode p = null;
		ListNode n = null;
		while(c != null){
			n = c.next;
			c.next = p;
			p = c;
			c=n;
		}
        head = p;
		return head;

    }
}