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
// https://workat.tech/problem-solving/practice/remove-occurences-linked-list
class Solution {
	ListNode removeOccurences(ListNode head, int k) {
		// add your logic here
		
		ListNode t = head;
		ListNode p = null;
		
		while(t!= null && t.data == k){
			head = t.next;
			t = head;
		}
		
//		while(t!=null){
//			while(t!=null && t.data != k){
//				p = t;
//				t = t.next;
//			}
//			
//			if(t == null)return head;
//			p.next = t.next; // unlink the t value 
//			
//			t = p.next; // new temp will be the next value of temp
//			
//		}

		while(t!=null && t.next != null){
			if(t.next.data == k){
				t.next = t.next.next;
			}
			else{
				t = t.next;
			}
		}
		

		
		
		
		
		return head;
	}
}