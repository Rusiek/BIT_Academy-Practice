# Pierwszy zawiera funkcję sortującą linked-list

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def list_to_tab(head):
    tab = []
    while head is not None:
        tab.append(head.val)
        head = head.next
    return tab


def tab_to_list(tab):
    n = len(tab)
    if n == 0:
        return None
    p = Node(tab[0])
    head = p
    for i in range(1, n):
        p.next = Node(tab[i])
        p = p.next
    return head


def get_center(head):
    if head is None:
        return head
    one = head
    two = head
    while one.next is not None and two.next is not None and two.next.next is not None:
        one = one.next
        two = two.next.next
    return one


def merge(head1, head2):
    p1 = head1
    p2 = head2
    if p2 is None:
        return p1
    if p1 is None:
        return p2
    if p1.val <= p2.val:
        head = p1
        p1 = p1.next
        head.next = None
    else:
        head = p2
        p2 = p2.next
        head.next = None
    merged = head
    while p1 is not None and p2 is not None:
        if p1.val <= p2.val:
            merged.next = p1
            merged = merged.next
            p1 = p1.next
            merged.next = None
        else:
            merged.next = p2
            merged = merged.next
            p2 = p2.next
            merged.next = None
    if p1 is not None:
        merged.next = p1
    else:
        merged.next = p2
    return head


def merge_sort(head):
    if head is None or head.next is None:
        return head
    center = get_center(head)
    after_center = center.next
    center.next = None
    left = merge_sort(head)
    right = merge_sort(after_center)
    sorted_list_head = merge(left, right)

    return sorted_list_head

