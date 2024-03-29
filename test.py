# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        remainder = 0
        value1 = l1.val
        value2 = l2.val
        start_node_l1 = l1.next
        start_node_l2 = l2.next
        new_values = []
        # if value1 and value2:
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
            # if new_val1 and new_val2:
            new_val = new_val1 + new_val2 + remainder
            remainder = 0
            if new_val > 9:
                str_value = str(new_val)
                new_val = int(str_value[-1])
                remainder = int(str_value[0])
            # elif new_val1:
            #     new_val = new_val1
            # elif new_val2:
            #     new_val = new_val2
            new_values.append(new_val)
            current_node_l1 = current_node_l1.next
            current_node_l2 = current_node_l2.next
        new_nodes = [ListNode(val) for val in new_values]
        for index, node in enumerate(new_nodes):
            if index + 1 < len(new_nodes):
                node.next = new_nodes[index + 1]
        print new_nodes[0].val
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
