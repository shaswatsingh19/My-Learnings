// https://workat.tech/problem-solving/practice/kth-element-linked-list
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

class Solution {
	ListNode kthElement (ListNode head, int k) {
	
		return ans(head,1,k);
		
	}
	
	
	ListNode ans(ListNode head, int i ,int k){
		if(i == k){
			return head;
		}
		i+=1;
		return ans(head.next,i,k);
		
		
	}
}