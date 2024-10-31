# Write a program that prints the following given the code below, implement your own node class and print binary tree function. Any language is fine. Sample code for python alone is given below. 

# The tree is printed in such a way that any vertical line has only 1 character. The output of your program should exactly match the output present here. 

# Expectation is to write a fully working program that prints the same output in a language of your choice.

# ------------------------------------------------------------------------------
# Empty tree
# x
# ------------------------------------------------------------------------------
# Example tree with 1 node

#   1
# x   x
# ------------------------------------------------------------------------------
# Example tree with 3 nodes

#           1
#   2         x
# x     5
#     x   x

# Example tree with 5 nodes

#           1
#   2           3
# x     5     x     4
#     x   x       x   x
# ------------------------------------------------------------------------------
# Example tree with 5 nodes and big numbers

#                1923
#   202                 32
# x       5343        x      40232
#       x      x           x       x
# ------------------------------------------------------------------------------


class Node:
    def __init__(self, data, left_node=None, right_node=None):
        self.data: int = data
        self.left: Node = left_node
        self.right: Node = right_node


def calculate_depth(root: Node):
    if root is None:
        return 0
    
    return 1 + max(calculate_depth(root.left), calculate_depth(root.right))
    
def print_binary_tree(root):
    if not root:
        print('x')
        return

    depth = calculate_depth(root)
    rows = depth + 1 # TO accomodate the last leaves
    # Increase width to accommodate larger numbers
    # Kept 4 becauase the usual largest number is 4 except 5 which is in one case
    width = 4 ** depth
    
    # Initialize the matrix with spaces
    matrix = [[' ' for _ in range(width)] for _ in range(rows)]
    
    def fill_matrix(node, row, left_index, right_index):
        mid = (left_index + right_index) // 2
        
        if not node:
            matrix[row][mid] = 'X'
            return
            
        # Start from the middle place such that it is in the center of that 
        # particular column of that row
        value = str(node.data)
        start = mid - len(value) // 2
        for i, char in enumerate(value):
            if 0 <= start + i < width:
                matrix[row][start + i] = char
                   
        if row + 1 < len(matrix):
            fill_matrix(node.left, row + 1, left_index, mid)
            fill_matrix(node.right, row + 1, mid + 1, right_index)
            
    fill_matrix(root, row=0, left_index=0, right_index=width - 1)
    
    # Print the matrix
    for row in matrix:
        print(''.join(row).rstrip())


def selftest():
    print('-' * 80)
    print('Empty tree')
    print_binary_tree(None)
 
    print('-' * 80)
    print('Example tree with 1 node')
    n1 = Node(1, None, None)
    print_binary_tree(n1)
 
    print('-' * 80)
    print('Example tree with 3 nodes')
    n5 = Node(5, None, None)
    n2 = Node(2, None, n5)
    n1 = Node(1, n2, None)
    print_binary_tree(n1)
 
    print('Example tree with 5 nodes')
    n5 = Node(5, None, None)
    n2 = Node(2, None, n5)
    n4 = Node(4, None, None)
    n3 = Node(3, None, n4)
    n1 = Node(1, n2, n3)
    print_binary_tree(n1)
 
    print('-' * 80)
    print('Example tree with 5 nodes and big numbers')
    n5 = Node(5343, None, None)
    n2 = Node(202, None, n5)
    n4 = Node(40232, None, None)
    n3 = Node(32, None, n4)
    n1 = Node(1923, n2, n3)
    print_binary_tree(n1)
 
    print('-' * 80)
    
    
selftest()