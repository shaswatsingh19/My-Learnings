// https://practice.geeksforgeeks.org/problems/reverse-a-linked-list/1#
//function Template for Java

/* linked list node class:

class Node {
    int value;
    Node next;
    Node(int value) {
        this.value = value;
    }
}

*/

class Solution
{
    //Function to reverse a linked list.
    Node reverseList(Node head)
    {
        code here
        Node c = head;
        Node p =null; Node n = null;
        
        while(c != null){
            n = c.next;
            c.next = p;
            p = c;
            c = n;
        }
        head = p;
        
        return head;
        
        
    }
}
