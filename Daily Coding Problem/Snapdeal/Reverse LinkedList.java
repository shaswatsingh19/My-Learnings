// https://workat.tech/problem-solving/practice/reverse-linked-list
// class ListNode {
// 	int data;
// 	ListNode next;

// 	ListNode (int data) {
// 		this.data = data;
// 	}
// }

class Solution {
	ListNode reverseLinkedList (ListNode head) {
		// add your logic here
		
		ListNode c = head;
		ListNode n = null;
		ListNode p = null;
		
		while(c != null){
			n = c.next;
			c.next = p;
			p = c;
			c = n;
		}
		head  = p;
		
		return head;
		
	}
}