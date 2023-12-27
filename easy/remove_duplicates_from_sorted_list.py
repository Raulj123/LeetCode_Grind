class linkedlist:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def printL(self):
        curr = self
        while curr is not None:
            print(f"{curr.val} ->")
            curr = curr.next
        print("None ---- end of list")

def makelinkedL(nums):
    head = linkedlist(nums[0])
    curr = head

    for num in nums[1:]:
        curr.next = linkedlist(num)
        curr = curr.next 
    return head 

def deleteDup(head):
    curr = head
    while curr and curr.next is not None:
        if curr.val == curr.next.val:
            print(curr.val)
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head



head = linkedlist([1,1,2])
print("Before: ")
head.printL()
a = deleteDup(head)
print("After: ")
a.printL()
# a1 = []
# while a != None:
#     a1.append(a.val)
#     a = a.next
# print(a1)
