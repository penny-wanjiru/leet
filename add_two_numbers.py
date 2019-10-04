# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def linked_list_length(self, node):
        "Return the length of the linked list starting at node."
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    def addTwoNumbers(self, l1, l2) -> :
        remainder = 0
        next_node_l1 = l1.next
        next_node_l2 = l2.next
        new_values = []
        new_value = l1.val + l2.val
        if new_value > 9:
            rem, new_value = str(new_value)
            remainder = int(rem)
        if new_value != 0:
            new_values.append(int(new_value))
        current_node_l1 = next_node_l1
        current_node_l2 = next_node_l2
        length = 0
        while current_node_l1 and current_node_l2 is not None:
            length += 1
            new_val = current_node_l1.val + current_node_l2.val + remainder
            remainder = 0
            if new_val > 9:
                rem, new_val = str(new_val)
                remainder = int(rem)
            new_values.append(int(new_val))
            current_node_l1 = current_node_l1.next
            current_node_l2 = current_node_l2.next
            if self.linked_list_length(l1)== len(new_values):
                break
        else:
            new_values.append(remainder)
        new_nodes = [ListNode(val) for val in new_values]
        for index, node in enumerate(new_nodes):
            if index + 1 < len(new_nodes):
                node.next = new_nodes[index + 1]
        return new_nodes[0]





listNode1 = ListNode(2)
listNode2 = ListNode(4)
listNode3 = ListNode(3)

listNode2.next = listNode3
listNode1.next = listNode2

listNodea = ListNode(5)
listNodeb = ListNode(6)
listNodec = ListNode(4)

listNodeb.next = listNodec
listNodea.next = listNodeb
Solution().addTwoNumbers(listNode1, listNode2)
