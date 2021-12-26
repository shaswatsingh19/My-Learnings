/** This is the ListNode class definition

class ListNode {
	int data;
	ListNode next;

	ListNode(int data) {
		this.data = data;
		this.next = null;
	}
}
**/

// https://workat.tech/problem-solving/practice/delete-kth-element-linked-list
class Solution {
	ListNode removekthElement (ListNode head, int k) {
	    // add your logic here
		int i=1;
		ListNode current = head;
		while(current != null){
			if(k==1){
				// head = head.next;
				return head.next;
			}
			if(i  == k-1){
				current.next = current.next.next;
				break;
				
			}
			current = current.next;
			i+=1;
		}
		return head;
	}
}