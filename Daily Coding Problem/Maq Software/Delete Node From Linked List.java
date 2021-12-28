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
// https://workat.tech/problem-solving/practice/delete-node-linked-list
class Solution {
	void deleteNode(ListNode node) {
	    // add your logic here
		
// 		ListNode p = null;
// 		while(node.next != null){
// 			node.data = node.next.data;
			
// 			 p  = node;
// 			node = node.next;
// 		}
// 		p.next = null;
		
		ListNode newNode = node.next;
		node.data = newNode.data;
		node.next = newNode.next;

//		int value = node.next.val;
//		node.data = value;
//		node.next = node.next.next;

		


	}
}