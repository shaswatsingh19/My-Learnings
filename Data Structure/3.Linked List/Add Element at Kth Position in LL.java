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
// https://workat.tech/problem-solving/practice/add-kth-element-linked-list
class Solution {
	ListNode addAtkthElement (ListNode head, int k, ListNode newElement) {
	    // add your logic here
		int i=1;
		ListNode t  = head;
		while(t != null){
			if(k==1){
				newElement.next = head;
				head = newElement;
				break;
			}
			if(i ==  k-1 ){
				newElement.next = t.next;
				t.next = newElement;
				break;
			}
			t = t.next;
			i+=1;
		}
		return head;
	}
}