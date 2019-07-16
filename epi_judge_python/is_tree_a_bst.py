from test_framework import generic_test

def min_val(node, current=float('inf')):
    if node:
        current = min(node.data, current)
        current = min_val(node.left, current)
        current = min_val(node.right, current)
    return current

def max_val(node, current=-float('inf')):
    if node:
        current = max(node.data, current)
        current = max_val(node.left, current)
        current = max_val(node.right, current)
    return current

def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    if tree:
        if tree.left and tree.right:
            tree_is_bst = max_val(tree.left) <= tree.data and tree.data <= min_val(tree.right)
        elif tree.left:
            tree_is_bst = max_val(tree.left) <= tree.data
        elif tree.right:
            tree_is_bst = min_val(tree.right) >= tree.data
        else:
            tree_is_bst = True
        return tree_is_bst and is_binary_tree_bst(tree.left) and is_binary_tree_bst(tree.right)
    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
