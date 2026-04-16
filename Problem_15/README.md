![Grid paths problem](image.png)

Starting in the top left corner of a $2\times 2$ grid, and only being able to move to the right and down, there are exactly $6$ routes to the bottom right corner.

How many such routes are there through a $20\times 20$ grid?

<span style="color:green;">

Solution: Given that the only two legal directions to go are right or down (2 directions) then the problem could be restated as follows. We basically have to count, how many downs and rights we do. But in an $n\times n$ grid there will be a total of $2n$ possible moves. Therfore, we just have to count how many of the $2n$ are down/right, because then the rest movements are going to be right/down. Thus, it's the same question as: "How many $n$-subsets does a $2n$-set have?" 

</span>