class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printL(self):
        curr = self
        while curr is not None:
            print(f"{curr.val} -> ")
            curr = curr.next
        print("None")
    def __repr__(self):
        curr = self
        while curr != None:
            print(f"Val: {curr.val} -> ")
            curr = curr.next
        print("None")

def makeLinkedList(l):
    head = ListNode(l[0])
    curr = head

    for num in l[1:]:
        curr.next = ListNode(num)
        curr = curr.next
    return head


def swapPairs(head):
    dumb = ListNode(0)
    dumb.next = head
    curr = dumb 

    while curr.next != None and curr.next.next != None:
        first = curr.next
        second = curr.next.next

        first.next = second.next
        curr.next = second

        second.next = first
        curr = second.next
        
    return dumb.next


        
head = makeLinkedList([1,2,3,4])
print("OG Linked List: ")
head.printL()

a1 = swapPairs(head)
print("List After being swapped: ")
a1.printL()

expected = [2,1,4,3]
r = []
while a1 != None:
    r.append(a1.val)
    a1 = a1.next

if r == expected:
    print("Accepted!")
else:
    print("Failed")

