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
// https://workat.tech/problem-solving/practice/remove-duplicates-sorted-linked-list
class Solution {
	ListNode removeDuplicates(ListNode head) {
		// add your logic here
		ListNode t = head;
		while(t!=null && t.next != null){
			if(t.data == t.next.data){
				t.next = t.next.next;
			}
			else{
				t=t.next;
			}
		}
		
		return head;
	}
}