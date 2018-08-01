# The Perfect Doodle Puzzle To Keep You Busy

>**Riddler Classic:** Start with an empty 5-by-5 grid of squares, and choose any square you want as your starting square. The rules for moving through the grid from there are strict:
>- You may move exactly three cells horizontally or vertically, or you may move exactly two cells diagonally.
>- You are not allowed to visit any cell you already visited.
>- You are not allowed to step outside the grid.
>- You win if you are able to visit all 25 cells.
>
>Is it possible to win?

**Solution:** Yes, there are in fact 12,400 distinct ways in which you could solve this puzzle, though this pales in comparison to the 2,404,881 different variations to the puzzle. This means it would take you on average roughly 194 tries to solve the puzzle if you selected your moves at random.

I didn't have the time to attempt 194 different combinations, so I built a brute force algorithm that implements a gameboard and tries every one of the 8 possible moves from each of the 25 possible starting positions. The algorithm also keeps track of the moves made to reach each of the 12,400 solutions.

A sample solution is shown below:

[0, 0], [3, 0], [3, 3], [0, 3], [2, 1], [2, 4], [4, 2], [1, 2], [3, 4], [0, 4], [0, 1], [3, 1], [1, 3], 
[4, 3], [4, 0], [1, 0], [3, 2], [0, 2], [2, 0], [2, 3], [4, 1], [1, 1], [1, 4], [4, 4], [2, 2]

The table below shows these moves happening in order (0-24) on the gameboard. Starting at [0, 0], marked as 0 on the board, we go to [3, 0], marked as 1, which is a horizontal move of +3. Then we move to [3, 3] marked as 2 and so on...

||0|1|2|3|4|
|--|--|--|--|--|--|
|**0**|0|15|18|1|4|
|**1**|10|21|4|11|20|
|**2**|17|7|24|16|6|
|**3**|3|12|19|2|13|
|**4**|9|22|5|8|12|
