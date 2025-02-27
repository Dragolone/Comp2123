from linkedList import LinkedList

def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order.
    - Recursively divide the linked list into sublists containing a single node.
    - Repeatedly merge the sublists to produce sorted sublists until one remains

    :param linked_list:
    :return:a sorted linked list
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists.
    :param linked_list:
    :return:
    """
    if linked_list is None or linked_list.head is None:
        left_half, right_half = linked_list, None
        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size // 2
        mid_node = linked_list.node_at_index(mid - 1)
        left_half = linked_list
        right_half = LinkedList()
        mid_node.nextNode = None
        return left_half, right_half
        


def merge(left, right):
    """
    Merge two sorted linked lists.
    :param left:
    :param right:
    :return:
    """