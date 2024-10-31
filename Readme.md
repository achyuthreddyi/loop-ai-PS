### Stratergy used to solve the problem

1. I have created a 2-D matrix based on the height of the given tree
2. The rows will be height + 1 (to accomodate the last leaves)
3. The no of Columns will be 2**(size of each number) Here I have taken as 4
4. I will loop through each row in the matrix to fill each row

    1. The stratergy to fill each row is of divide and conquer approach
    2. In each iteration I will divide each row into 2 equal halves based on the size of the row.
    3. The left part will be given the left node 
    4. The right part will be given the right node