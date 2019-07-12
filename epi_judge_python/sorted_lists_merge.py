from test_framework import generic_test

class ListNode:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def merge_two_sorted_lists(L1, L2):
    dummy = ListNode(data="None")
    r1, r2, r3 = L1, L2, dummy
    while r1 is not None and r2 is not None:
        if r1.data < r2.data:
            r3.next = r1
            r1 = r1.next
        else:
            r3.next = r2
            r2 = r2.next
        r3 = r3.next
    r3.next = r1 if r2 is None else r2
    return dummy.next



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
