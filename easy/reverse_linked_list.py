# time -> o(n)
# space -> o(1)

def iteratively(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next 
        curr.next = prev
        prev = curr
        curr = nxt 
    return prev

# im not doing this recursively bruh 






