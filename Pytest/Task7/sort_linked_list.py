class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    

def linked_list_to_tab(ll):
    tab = []
    while ll is not None:
        tab.append(ll.val)
        ll = ll.next
    return tab


def tab_to_linked_list(tab):
    if len(tab) == 0:
        return None
    
    head = Node(tab[0])
    head.val = tab[0]
    head.next = None
    temp = head
    for i in range (1, len(tab)):
        curr = Node(tab[i])
        curr.val = tab[i]
        temp.next = curr
        temp = curr
    
    return head


def MiddleOfLinkedList(first):
    if first is None:
        return None

    a = first
    b = first
    while b is not None and b.next is not None and b.next.next is not None:
        a = a.next
        b = b.next.next
    return a


def MergeTwoLinkedList(first, second):
    if first is None:
        return second
    if second is None:
        return first
    
    curr_first = first
    curr_second = second
    
    if curr_first.val <= curr_second.val:
        head = curr_first
        curr_first = curr_first.next
        head.next = None
    else:
        head = curr_second
        curr_second = curr_second.next
        head.next = None

    temp = head

    while curr_first is not None and curr_second is not None:
        if curr_first.val <= curr_second.val:
            temp.next = curr_first
            temp = temp.next
            curr_first = curr_first.next
            temp.next = None
        else:
            temp.next = curr_second
            temp = temp.next
            curr_second = curr_second.next
            temp.next = None

    if curr_first is not None:
        temp.next = curr_first
    else:
        temp.next = curr_second
    return head


def MergeSort(first):
    if first is None:
        return None
    if first.next is None:
        return first
    
    middle = MiddleOfLinkedList(first)
    right_part = middle.next
    middle.next = None
    left_part = first


    right = MergeSort(right_part)
    left = MergeSort(left_part)

    sorted_linked_list = MergeTwoLinkedList(left, right)
    return sorted_linked_list


