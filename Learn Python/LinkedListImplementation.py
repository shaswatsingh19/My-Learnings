class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head= None

# Insert At Beginning

    def insertAtBeginning(self,new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node
# Insert after a Node

    def insertAfterNode(self,prev_node,new_data):
        if prev_node is None:
            print('Previous node must not be None')
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
# Insert at End

    def insertAtEnd(self,new_data):
        new_node = Node(new_data)
       # if no element is in ll 
        if self.head  is None:
            self.head = new_node
            
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = new_node
        
        
# Delete a Node
    def deleteNode(self,pos):
        if self.head is None:
            return

        temp = self.head

        if pos == 0:
            self.head = temp.next
            temp = None # deleting temp node to clear memory
            return

        for i in range(pos-1):
            temp = temp.next
            if temp is None:
                break
            
        # if pos is not present
        if temp is None :
            return
        if temp.next is None:
            return

        next  = temp.next.next
        temp.next = None
        temp.next = next
    
# Search and element

    def search(self,element):
        temp = self.head
        not_found = "Element Not Found"
        i=0
        while temp != None:
            if temp.data == element:
                print("Element found at pos "+str(i))
                return 
            i+=1
            temp =temp.next

        print(not_found)
        return
    
# PrintLinkedList

    def print(self):
        temp  = self.head
        while(temp.next!=None):
            print(temp.data,'-->',end=' ')
            temp = temp.next
        print(temp.data,"-->None")


# making object of linkedlist

ll = LinkedList()
ll.head = Node(2)
second = Node(23)
third  = Node(53)
fourth = Node(32)

# Now we connect everyNode

ll.head.next = second
second.next = third
third.next = fourth

# print LinkedList

print('Inital linkedlist')
ll.print()
print('inserting the data at beginning')
val  = int(input())
ll.insertAtBeginning(val)
print("print after inseting",val)
ll.print()
ll.insertAfterNode(second,232)
print("printing 232 after inserting after second node") 
ll.print()
print("Enter an element to insert at END")
val = int(input())
ll.insertAtEnd(val)
print("print linkedlist after inseting ",val,"at end")
ll.print()
print("Delete at which position, by 0 indexing")
pos  = int(input())
ll.deleteNode(pos)
ll.print()
print("Enter the element to search")
ele = int(input())
ll.search(ele)


'''
Inital linkedlist
2 --> 23 --> 53 --> 32 -->None
inserting the data at beginning
1
print after inseting 1
1 --> 2 --> 23 --> 53 --> 32 -->None
printing 232 after inserting after second node
1 --> 2 --> 23 --> 232 --> 53 --> 32 -->None
Enter an element to insert at END
999
print linkedlist after inseting  999 at end
1 --> 2 --> 23 --> 232 --> 53 --> 32 --> 999 -->None
Delete at which position 0 indexing
3
1 --> 2 --> 23 --> 53 --> 32 --> 999 -->None
Enter the element to search
32
Find element at pos 4
'''
