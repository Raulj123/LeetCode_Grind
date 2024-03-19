# slow and fast ptr appr.

def middleNode(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow






head = [1,2,3,4,5] # lets just say this is a linked list 
middleNode(head)
