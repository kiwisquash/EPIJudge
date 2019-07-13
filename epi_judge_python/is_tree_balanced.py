from test_framework import generic_test

def is_balanced_binary_tree(tree, heights = None):
    # TODO - you fill in here.
    if tree is None: return True
    
    if heights is None:
        heights = {}

    def tree_height(tree):
        if tree is None: return -1
        if tree not in heights:
            heights[tree] = max(tree_height(tree.left), tree_height(tree.right)) + 1
        return heights[tree]

    height_diff = abs(tree_height(tree.left) - tree_height(tree.right))
    return height_diff <= 1 and is_balanced_binary_tree(tree.left, heights) and is_balanced_binary_tree(tree.right, heights)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
