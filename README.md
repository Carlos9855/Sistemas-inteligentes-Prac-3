# Sistemas-inteligentes-Prac-3
## Members
* Jose Carlos Camacho Salazar
* Diego Delgadillo
* Sebastian Lazarte Catellon

# Problem Description
We have the (n^2 - 1)-puzzle, a puzzle that consists on having a board with numbers and the numbers are not in order. So that we want to implement a computer program that helps us to get the numbers in order.
# Solution Description
We are going to use the A* algortihm. This algorithm uses what is known as a "heuristic function". This function returns a number that represents a characteristic of the board. We can use many heuristic functions and each one of them is getting us a different response
The heuristic functions that we are going to use on this experiments are: 

hˆ1(n) = The number of tiles of the board out of place 

hˆ2(n) = The sum of the Manhattan distance from a piece in the initial state to the same piece in the goal state for all the pieces.

hˆ3(n) = The sum of inverse permutations 

# Running the script
In order to run the program you first have to enter the 
directory where the ***N-puzzle.py*** file is located through 
the ***CMD*** console or the one of your choice.

Then in the console you have to enter the `python N-puzzle.py` or `py N-puzzle.py`, a message will 
 appear asking you to enter the size of the puzzle, then it will
  ask you to enter the values for the puzzle and finally you 
  will see a menu with the available heuristics


# EXPERIMENTS

On the part of experiments first we are taking one combination 
and we are solving it with all the heuristic functions to 
compare the time that takes to every function. At the bottom we 
are calculating the average of every function.
  || H1 | H2 | H3 |  
 :---: | :---: | :---: | :---:  
 ||  32.86 seconds | 0.571 seconds | 37.68 seconds
 || 30.95 seconds | 0.65 seconds | 38.37 seconds
|For 0 3 8 4 1 7 2 6 5|  32.92 seconds | 0.54 seconds | 35.056 seconds
 ||  38.819 seconds | 0.836 seconds | 36.799 seconds
 || 27.2313 seconds | 0.52262 seconds | 36.75 seconds
 |Average| 30.14 seconds | 0.78 seconds |36.34 seconds

On the second part of experiments we are taking more 
combinations and we are comparing the time and the memory that 
every function has. We are processing the combinations through
levels so that the first one should be the easiest and the last
one the hardest to solve.


## Tiles out of place
Tiles out of place. For this heuristic we are counting the
spaces in the board that are out place by comparing the actual
state with the goal state and then we get the sum of every
one that is not in place, after that we compare the sums and 
decide which one is the lowest, once we get it we expand 
that node and so on. If two states match at the sum of the
out of place tiles we select one randomly.

||Initial State | Time (seconds) | Memory (MB)
|:---: | :---: | :---: | :---:
||0 2 3 1 4 5 6 7 8 | 0.222446203231811 | 1.37038421630859
||0 2 4 1 3 8 6 7 5 | 1.42226362228393 | 15.0011291503906
||0 3 8 4 1 7 2 6 5 | 36.9328112602233 | 238.096641540527
||4 2 0 8 3 5 7 6 1 | 58.2836725711822 | 465.806007385253
||6 4 1 0 2 3 8 5 7 | 104.866127729415 | 821.302085876464

## Manhattan Distance
Manhattan distante. In this heuristic we are comparing the 
distance between one tile in the actual state and the same 
tile on the goal state. Once we get the numbers we make a sum 
of every one. Then we compare the those numbers and expand the 
lowest one.

||Initial State | Time (seconds) | Memory (MB)
|:---: | :---: | :---: | :---:
||0 2 3 1 4 5 6 7 8 | 0.0339031219482421 | 0.114471435546875
||0 2 4 1 3 8 6 7 5 | 0.837672472000122 | 3.501953125
||0 3 8 4 1 7 2 6 5 | 1.31654977798461 | 2.39399719238281
||4 2 0 8 3 5 7 6 1 | 1.01377058029174 | 4.15076446533203
||6 4 1 0 2 3 8 5 7 | 1.27330470085144 | 5.37344360351562

## Sum of Inverse Permutations
 Inverse permutations. For this heuristic we have the actual 
 combination on a list and going through every element we 
 compare it to the ones ahead and if the element ahead is 
 lower we add it to the a counter. Then we repeat the comparing 
 process with all the elements of the list and after that we 
 make a sum with all the counters. Then we get the number and 
 choose the lowest one and that is the node we expand.

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
As we perform the experiments we have noticed that some 
combinations for the board could only be solved with the 
Manhattan distance. Such as 876543210, so we recomend that 
the combinations for the board to be reviewed before putting 
them on the program.

Some combinations also take a lot of time but they can be solved. 
Some of those times are on the experiments table. We also 
recommend to take a look to those times before shutting the 
process down.

Also it is recommended to make a review of the components of the 
system, especially the memory since the processes consume a lot 
and it can make a difference at the execution performance.
# Poroto
In the bean part we designed a heuristic function which 
consisted in choosing randomly a value that could be zero 
or one, and that was added to a counter when the value of 
the current state of the node was equal to the value of the 
target state. 
||Initial State | Time (seconds) | Memory (MB)
|:---: | :---: | :---: | :---:
||0 2 3 1 4 5 6 7 8 | 104.745321273803 | 703.587684631347

With the test we did we could see that our heuristic function 
is not the best because it consumes a lot of memory and time, 
therefore it is not admissible.
Note: Several verification tests could not be performed since 
this heuristic function consumes a lot of resources (RAM).

# BIBLIOGRAPHY
* Class slides
* Code reference: https://github.com/duaraghav8/N-Puzzle-through-A-Star
