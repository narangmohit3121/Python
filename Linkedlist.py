class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    head = None
    size = 0
    tail = None

    def __init__(self):
        pass

    def add_element(self, val):
        current_node = Node(val)
        current_node.next = self.head
        self.head = current_node
        self.size += 1

    def get_size(self):
        return self.size

    def pop_element(self):
        top_node = self.head
        self.head = top_node.next
        self.size -= 1
        return top_node.value

    def get_element(self, position):
        counter = 0
        current_node = self.head
        while counter < position:
            current_node = current_node.next
            counter += 1

        return current_node.value

    def insert_element(self, position, value):
        counter = 0
        new_node = Node(value)
        node_position_minus_one = None
        current_node = self.head
        while counter < position:
            if counter == position - 1:
                node_position_minus_one = current_node
            current_node = current_node.next
            counter += 1
        node_position_minus_one.next = new_node
        new_node.next = current_node
        self.size += 1

    def print_all_elements(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=';')
            current_node = current_node.next

    def reverse_linked_list_2(self):
        temp_head_node = Node(self.head.value)
        temp_head_node.next = self.head.next
        self.head.next = None
        while True:
            print('Reversing list')
            temp_next_node = Node(temp_head_node.next.value)
            temp_next_node.next = temp_head_node.next.next
            # print('Reversing list')
            # print(temp_node.value)
            temp_head_node.next.next = self.head
            self.head = temp_head_node.next

            if temp_next_node.next is not None:
                temp_head_node = temp_next_node
            else:
                break

    def reverse_linked_list(self):
        temp_node = Node(self.head.next.value)
        temp_node.next = self.head.next.next
        self.head.next = None
        while True:
            print('Reversing list')
            print(temp_node.value)
            current_node = temp_node
            temp_node = temp_node.next
            current_node.next = self.head
            self.head = current_node
            if temp_node.next is not None:
                pass
            else:
                temp_node.next = self.head
                self.head = temp_node
                print('Exiting loop')
                print(current_node.value)
                break


l1 = LinkedList()
l1.add_element(1)
l1.add_element(2)
l1.add_element(3)
l1.add_element(4)
l1.add_element(5)
l1.add_element(6)
l1.add_element(7)
l1.add_element(8)

print(l1.size)
# print(l1.pop_element())
print(l1.get_element(3))
print(l1.insert_element(3, 0))
print(l1.get_element(3))
print(l1.get_element(2))
l1.print_all_elements()
l1.reverse_linked_list()
print('List reversed')
l1.print_all_elements()

