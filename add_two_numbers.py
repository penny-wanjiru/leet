# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        remainder = 0
        value1 = l1.val
        value2 = l2.val
        start_node_l1 = l1.next
        start_node_l2 = l2.next
        new_values = []
        new_value = value1 + value2
        if new_value > 9:
            str_value = str(new_value)
            new_value = int(str_value[-1])
            remainder = int(str_value[0])
        new_values.append(new_value)
        current_node_l1 = start_node_l1
        current_node_l2 = start_node_l2


        while current_node_l1 and current_node_l2 is not None:

            new_val1 = current_node_l1.val
            new_val2 = current_node_l2.val
            new_val = new_val1 + new_val2 + remainder
            remainder = 0
            if new_val > 9:
                str_value = str(new_val)
                new_val = int(str_value[-1])
                remainder = int(str_value[0])
            new_values.append(new_val)
            current_node_l1 = current_node_l1.next
            current_node_l2 = current_node_l2.next
        new_nodes = [ListNode(val) for val in new_values]
        for index, node in enumerate(new_nodes):
            if index + 1 < len(new_nodes):
                node.next = new_nodes[index + 1]

        return new_nodes[0]
