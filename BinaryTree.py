class BinaryTree(object):
    def __init__(self, root_value):
        self.root_val = root_value
        self.left_child = None
        self.right_child = None

    def insert_left_child(self,val):
        if self.left_child is None:
            self.left_child = BinaryTree(val)
        else:
            temp = BinaryTree(val)
            temp.left_child = self.left_child
            self.left_child = temp

    def insert_right_child(self, val):
        if self.right_child is None:
            self.right_child = BinaryTree(val)
        else:
            temp = BinaryTree(val)
            temp.right_child = self.right_child
            self.right_child = temp

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root(self, new_root_val):
        self.root_val = new_root_val


def traverse_post_order(tree: BinaryTree):
    if tree is not None:
        traverse_post_order(tree.left_child)
        traverse_post_order(tree.right_child)
        print(tree.root_val)


def traverse_pre_order(tree:BinaryTree):
    if tree is not None:
        print(tree.root_val)
        traverse_pre_order(tree.left_child)
        traverse_pre_order(tree.right_child)


binTree = BinaryTree(1)
binTree.insert_left_child(2)
binTree.left_child.insert_left_child(3)
binTree.left_child.insert_right_child(4)
binTree.insert_right_child(5)

# traverse_post_order(binTree)
traverse_pre_order(binTree)