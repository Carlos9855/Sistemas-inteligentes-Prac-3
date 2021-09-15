# Sistemas-inteligentes-Prac-3
## Problem Description
We have the (n^2 - 1)-puzzle, a puzzle that consists on having a board with numbers and the numbers are not in order. So that we want to implement a computer program that helps us to get the numbers in order.
## Solution Description
We are going to use the A* algortihm. This algorithm uses what is known as a "heuristic function". This function returns a number that represents a characteristic of the board. We can use many heuristic functions and each one of them is getting us a different response
The heuristic functions that we are going to use on this experiments are: 
hˆ1(n) = The number of tiles of the board out of place 
hˆ2(n) = The sum of the Manhattan distance from a piece in the initial state to the same piece in the goal state for all the pieces.
hˆ3(n) = The sum of inverse permutations 

## Running the script
python N-puzzle.py inside the directory of the file. Then introduce the size of the board you want to work with. And last introduce the elements of the board.


  || H1 | H2 | H3 |  
 :---: | :---: | :---: | :---:  
 ||  32.86 seconds | 0.571 seconds | 37.68 seconds
 || 30.95 seconds | 0.65 seconds | 38.37 seconds
|For 0 3 8 4 1 7 2 6 5|  32.92 seconds | 0.54 seconds | 35.056 seconds
 ||  38.819 seconds | 0.836 seconds | 36.799 seconds
 || 27.2313 seconds | 0.52262 seconds | 36.75 seconds
 || 30.14 seconds | 0.78 seconds |36.34 seconds

