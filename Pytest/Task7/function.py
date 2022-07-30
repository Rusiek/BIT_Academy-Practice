
class Node():
    def __init__(self, val):
        self.next = None
        self.val = val
        
def tab2list(t):
    n = len(t)
    p = None

    for i in range(n-1,-1,-1):
        q = Node(t[i])
        q.val = t[i]
        q.next = p
        p = q

    return p


def list2tab(l):
    t = []
    while l!=None:
        t.append(l.val)
        l = l.next

    return t

def divide(A):
    p = Node(None)
    p.next = A
    low = low_s = Node(None)
    big = big_s = Node(None)
    mid = mid_s = Node(None)
    to_cmp = p.next.val
    while p.next != None:
        if p.next.val < to_cmp:
            low.next = p.next
            low = low.next
        elif p.next.val > to_cmp:
            big.next = p.next
            big = big.next
        else:
            mid.next = p.next
            mid = mid.next
        p = p.next
    low.next = None
    big.next = None
    mid.next = None
    return low_s.next, big_s.next, mid_s.next


def quicker_sort(A):
    if A != None:
        triplet = divide(A)
        low = triplet[0]
        big = triplet[1]
        mid = triplet[2]
        # print(list2tab(low), list2tab(big), list2tab(mid))
        Ans = Ans_s =  Node(None)
        sorted_left = quicker_sort(low)
        if sorted_left != None:
            Ans.next = sorted_left
            while Ans.next != None:
                Ans = Ans.next
        if mid != None:
            Ans.next = mid
            while Ans.next != None:
                Ans = Ans.next
        sorted_right = quicker_sort(big)
        if sorted_right != None:
            Ans.next = sorted_right
        return Ans_s.next

# t = t = [9, 99, 57, 47, 32, 50, 75, 20, 77, 28, 33, 34, 82, 41, 39, 86, 95, 1, 70, 54, 19, 61, 16, 80, 42, 64,
#      37, 56, 7, 92, 87, 67, 81, 85, 91, 79, 13, 76, 73, 5, 12, 21, 65, 3, 71, 94, 6, 58, 98, 97]
# t = []
# p = tab2list(t)

# p2 = quicker_sort(p)
# print(t)
# t.sort()
# print(t)
# print(list2tab(p2))
