// https://practice.geeksforgeeks.org/problems/reverse-a-linked-list/1
class Solution
{
    //Function to reverse a linked list.
    Node reverseList(Node head)
    {
        
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
