# Sistemas-inteligentes-Prac-3
## Problem Description
We have the (n^2 - 1)-puzzle, a puzzle that consists on having a board with numbers were these are not in order. For this reason, a computer program has been implemented which helps to order the numbers.
## Solution Description
The algorithm used is A* algortihm. This algorithm uses what is known as a "heuristic function". This function returns a number that represents a characteristic of the board. It can use many heuristic functions and each one of them gives a different response.
The heuristic functions that  are going to be used on this experiments are: 
hˆ1(n) = The number of tiles of the board out of place 
hˆ2(n) = The sum of the Manhattan distance from a piece in the initial state to the same piece in the goal state for all the pieces.
hˆ3(n) = The sum of inverse permutations 

## Running the script
python N-puzzle.py inside the directory of the file. Then introduce the size of the board you want to work with. And last introduce the elements of the board.


## EXPERIMENTS
In the experiments part, first a combination is taken and solved with all heuristic functions for 
is solved with all the heuristic functions to compare the time it takes 
compare the time taken by each function. In the background the average of each function is calculated.
  || H1 | H2 | H3 |  
 :---: | :---: | :---: | :---:  
 ||  32.86 seconds | 0.571 seconds | 37.68 seconds
 || 30.95 seconds | 0.65 seconds | 38.37 seconds
|For 0 3 8 4 1 7 2 6 5|  32.92 seconds | 0.54 seconds | 35.056 seconds
 ||  38.819 seconds | 0.836 seconds | 36.799 seconds
 || 27.2313 seconds | 0.52262 seconds | 36.75 seconds
 |Average| 30.14 seconds | 0.78 seconds |36.34 seconds

In the second part of the experiments, more combinations are taken and the time and memory combinations are taken and the time and memory that each function has is compared. The combinations are processed through
levels so that the first one is the easiest and the last one the easiest. 
last one the most difficult to solve

# Out-of-place tiles
Out-of-place tiles. For this heuristic, the spaces on the board that are out of place are counted by comparing the state
actual state with the goal state and then the sum of each out-of-place tile is obtained.
that is out of place, then we compare the sums and decide which is 
the sums and decide which one is the lowest, once it is obtained we expand that node and so on.
that node and so on. If two states coincide in the sum of the out-of-place tokens, one of them is selected
If two states coincide in the sum of the out of place tokens, one is selected at random.

||Initial State | Time (seconds) | Memory (MB)
|:---: | :---: | :---: | :---:
||0 2 3 1 4 5 6 7 8 | 0.222446203231811 | 1.37038421630859
||0 2 4 1 3 8 6 7 5 | 1.42226362228393 | 15.0011291503906
||0 3 8 4 1 7 2 6 5 | 36.9328112602233 | 238.096641540527
||4 2 0 8 3 5 7 6 1 | 58.2836725711822 | 465.806007385253
||6 4 1 0 2 3 8 5 7 | 104.866127729415 | 821.302085876464

# Manhattan Distance
In this heuristic a tile in the current state and the same tile in the target state.  Once the numbers are obtained, a sum of each is performed. 
of each one. Then, those numbers are compared and the lowest one is expanded. 
lowest one.

||Initial State | Time (seconds) | Memory (MB)
|:---: | :---: | :---: | :---:
||0 2 3 1 4 5 6 7 8 | 0.0339031219482421 | 0.114471435546875
||0 2 4 1 3 8 6 7 5 | 0.837672472000122 | 3.501953125
||0 3 8 4 1 7 2 6 5 | 1.31654977798461 | 2.39399719238281
||4 2 0 8 3 5 7 6 1 | 1.01377058029174 | 4.15076446533203
||6 4 1 0 2 3 8 5 7 | 1.27330470085144 | 5.37344360351562

# Sum of Inverse Permutations
 Inverse Permutations. For this heuristic the current combination is taken in a list and going through each element it is compared with the elements in front, if the element in front is lower, it is added to the counter. Then the comparison process is repeated  with all the elements of the list and then a sum is performed with all the counters.  Then the number is obtained and 
 the lowest one is chosen and that is the node to be expanded.
||Initial State | Time (seconds) | Memory (MB)
|:---: | :---: | :---: | :---:
||0 2 3 1 4 5 6 7 8 | 1.00835633277893 | 6.0256118774414
||0 2 4 1 3 8 6 7 5 | 118.148568868637 | 434.005943298339
||0 3 8 4 1 7 2 6 5 | 50.3002603054046 | 194.452728271484
||4 2 0 8 3 5 7 6 1 | 11.6959052085876 | 77.3878936767578
||6 4 1 0 2 3 8 5 7 | 342.6548941      | 1354.87213742

# With which heuristic does A∗ use more memory?
The heuristic of A* that occupies more memory is that of the
summation of the inverse permutations, it could be observed 
that the heuristic in some cases was faster than the heuristic
hˆ1(n) and in others not but something that called our
attention was that it occupied a great amount of memory,
and in terms of performance it is not the best since more 
powerful computers would be needed.

# With which heuristic A∗ find the solution faster?
The heuristic that found the target solution the fastest was
the manhattan function since all the tests performed were 
solved in less than two seconds and it also took less memory.

# A* is or is not optimal using hˆ1(n), hˆ2(n), hˆ3(n)?
According to the experiments carried out, the only heuristic
function that is optimal is the manhattan function since it has 
a better execution time and more optimal memory management due 
to the fact that it uses the shortest and most optimal path to 
the objective function.

# Conclusions
In this practice we had to test three different heuristic 
functions and analyze their advantages and disadvantages, we 
could also observe that there is a big difference between them
 since one was optimal and gave us a low execution time, the 
 other functions were the opposite, giving us execution times 
 and memory reservation higher than expected.
So we came to the conclusion that the most optimal heuristic 
is the manhattan distance.

# Recommendations