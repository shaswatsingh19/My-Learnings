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
//https://workat.tech/problem-solving/practice/append-linked-lists/
class Solution {
	ListNode appendLists (ListNode list1, ListNode list2) {
	    // add your logic here
		ListNode currList1 = list1;
		while(currList1.next != null){
			currList1 = currList1.next;
		}
		currList1.next  = list2;
		
		return list1;
	}
}