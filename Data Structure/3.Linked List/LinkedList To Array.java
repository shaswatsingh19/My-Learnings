// https://workat.tech/problem-solving/practice/linked-list-to-array
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
	List<Integer> linkedListToArray (ListNode head) {
	    // add your logic here
		ArrayList<Integer> l = new ArrayList<Integer>();
		
		ListNode currentNode = head;
		while(currentNode != null){
			l.add(currentNode.data);
			currentNode = currentNode.next;
		}
		
		return l;
	}
}