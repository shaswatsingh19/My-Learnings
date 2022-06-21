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
//https://workat.tech/problem-solving/practice/find-xth-node-end-linked-list/
class Solution {
	ListNode xthNodeFromEnd(ListNode head, int x) {
		// add your logic here
		ListNode t = head;
		int n=0;
		while(t!=null){
			n++;
			t=t.next;
		}
		t = head;
		x = n-x;
		while(x>0){
			t = t.next;
			x-=1;
		}
		return t;
	}
}