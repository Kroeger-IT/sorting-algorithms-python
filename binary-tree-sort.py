class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if root.data < data:
            root.right = insert(root.right, data)
        else:
            root.left = insert(root.left, data)
    return root

def in_order_traversal(root):
    res = []
    if root:
        res = in_order_traversal(root.left)
        res.append(root.data)
        res = res + in_order_traversal(root.right)
    return res

def binary_tree_sort(arr):
    root = None
    for i in arr:
        root = insert(root, i)
    return in_order_traversal(root)

# Example usage
arr = [5, 2, 9, 1, 5, 6]
print("Unsorted array:", arr)
sorted_arr = binary_tree_sort(arr)
print("Sorted array:", sorted_arr)
