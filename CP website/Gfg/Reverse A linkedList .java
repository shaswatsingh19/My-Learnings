// https://practice.geeksforgeeks.org/problems/reverse-a-linked-list/1
class Solution
{
    //Function to reverse a linked list.
    Node reverseList(Node head)
    {
        // Iteratively
        
        Node  c = head;
        Node p = null;Node n = null;
        
        while(c != null){
            n = c.next;
            c.next = p;
            p = c;
            c = n;
        }
        
        head = p;
        return head;
        
        // Recursively
        
        if(head == null || head.next == null){
            return head;
        }
        
        Node newHead = reverseList(head.next);
        Node headNext = head.next;
        headNext.next = head;
        head.next = null;
        return newHead;
    }
}
