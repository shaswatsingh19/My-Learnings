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
// https://workat.tech/problem-solving/practice/middle-element-linked-list
// If the list has even number of elements, print the first of the two middle elements
class Solution {
	int getMiddleElementOfLinkedList (ListNode list) {
	    // add your logic here
		ListNode slow = list;
		ListNode fast = list;
		int i=0;
		ListNode p = slow;
		int n = 0;
		while(fast != null){
			fast= fast.next;
			n+=1;
		}
		while(i<n/2){
			p = slow;
			slow=slow.next;
			i++;
		}
		if(n % 2==0){
			return p.data;
		}
		return slow.data;
	}
}