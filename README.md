<b>Citation:</b>
Discussed ideas with Aditya Kartikeya,Vivek Shresta and Vansh Shah


<b>Part 1:  Finding your way :</b>

In this problem, the first thing I observed was the problem was going into an infinite loop without giving any output. A quick glance at the code helped me understand that a stack-based solution was being used here(By looking at the fringe.pop()).

I immediately realized that a Depth first search(DFS) based approach may sometimes lead to the solution never being found as it can get stuck in loops. I quickly defined a function that replaced the stack-based implementation to queue based and the code immediately ran.

<b>Queue implementation:</b>

Basically pops the element from the front of the list:

        def queue(fringe):
              return fringe.pop(0)

The next challenge posed was to display the direction traversed along with the path length which was already being displayed. This was slightly trickier. Initially, I thought of creating a 2D array and keeping track of the direction traversed in a string for each and every point where each element of the 2D array represents a point in the map.
But, this wasn't a good approach to this problem because there would be no way to keep track of the state if it came back. Hence I decided to add another element to the tuple containing the current position and path length. This third element was a string that would hold the data regarding the traversed path to get to that state.

fringe=[(you_loc,0,"")]

Also, to track the direction, I defined another function where with the help of coordinates of the current and previous positions,I decided the direction of the move.

def compass(move,curr_move):
        tracker=""
        if [move[0]-curr_move[0],move[1]-curr_move[1]]==[1,0]:
                tracker+="S"
        elif [move[0]-curr_move[0],move[1]-curr_move[1]]==[0,1]:
                tracker+="E"
        elif [move[0]-curr_move[0],move[1]-curr_move[1]]==[-1,0]:
                tracker+="N"
        elif [move[0]-curr_move[0],move[1]-curr_move[1]]==[0,-1]:
                tracker+="W"
        return tracker

<b>Initial State:</b>

The initial state here is where the # is positioned initially with respect to other positions on the map.

For example, in the given map:

 ....&&&<br/>
.&&&...<br/>
....&..<br/>
.&.&...<br/>
.&.&.&.<br/>
#&...&@<br/>

<b>State Space:</b>

The state space here is all the possible positions of # on the map, which is on every possible sidewalk.

<b>Goal state:</b>

The state where the # coincides with @.That is the point where we find Luddy Hall.

<b>Successor function:</b>

The successor function defined here takes in your current position and returns all the possible states you can move to from the current position. If there is a building on one of the directions, it wouldn't return that state.

One additional thing I added later was some extra code to eliminate duplicate states.By doing this the program was quickly able to return Inf if there was no solution.

         if move not in visited:

                                
                fringe.append((move, curr_dist + 1,tracked_by_compass+compass(move,curr_move)))
                visited.append(move)

<b>Cost Function:</b>

The cost function here is the length of the path moved each time. That is, we take one step every time hence the cost is the same for every move.






<b>Part 2: Hide and Seek :</b>

<b>Initial State:</b>

The initial state is the state with no “F” on the map. Hence it looks like below:

....&&&<br/>           
.&&&...<br/>
....&..<br/>
.&.&...<br/>
.&.&.&.<br/>
#&...&@<br/>

_________________________________________________________________________________________________________________________________
<b>State Space:</b>

The state space in this problem can be defined as all the possible positions of the map where “F” can be placed. The state space includes all the possible maps which contain 1 * “F”  to 
 K * “F”s.

<b>examples:</b>

.F..&&&<br/>             
.&&&...<br/>  
....&..<br/>  
.&.&...<br/>  
.&.&.&.<br/>  
#&...&@<br/>  
_________________________________________________________________________________________________________________________________

....&&&<br/>  
F&&&...<br/>  
....&..<br/>  
F&.&...<br/>  
.&.&.&.<br/>  
#&...&@<br/>  
_________________________________________________________________________________________________________________________________

....&&&<br/>  
F&&&F..<br/>  
....&..<br/>  
.&.&F..<br/>  
.&.&.&.<br/>  
#&...&@<br/>  

_________________________________________________________________________________________________________________________________

<b>Goal State:</b>

The goal state would be the state with K * “F”  position on the board such that no two “F” can see each other.

For K=9:

.F..&&&<br/>  
.&&&F..<br/>  
.F..&F.<br/>  
F&F&F..<br/>  
.&.&.&F<br/>  
#&.F.&@<br/>  

_________________________________________________________________________________________________________________________________


<b>Successor function:</b>

The basic successor function take the map as input and outputs another map with one F more than the previous state.This is the one defined in the skeleton code.It definitely works but a major problem associated with it was it generates a huge number of states which almost makes the program impossible to ever find the solution.


A good approach to solve this would be to have a successor function that returns much fewer states. Hence I came up with an idea which I have described below:

My 1st version of successor function was as follows:

Here I eliminate states which are invalid and then return the states. For this, all I had to make sure to write a function where no 2 friends can see each other. The program is given below:

def not_eliminate_state(board):
    main_goal=True
    for row in board:
            if row.count('F')>1: 
                    a=[index for index,element in enumerate(row) if element == "F"]
                    for i in range(len(a)-1):
                            temp_list=row[a[i]:a[i+1]]
                            if ("&" not in temp_list):
                                    main_goal=False
    board_transpose=[*zip(*board)]
    for row in board_transpose:
            if row.count('F')>1: 
                    a=[index for index,element in enumerate(row) if element == "F"]
                    for i in range(len(a)-1):
                            temp_list=row[a[i]:a[i+1]]
                            if ("&" not in temp_list):
                                    main_goal=False
    return main_goal

Now, this got my code working but again here comes a twist. This approach worked till K=8 for the given map. But when it went to K=9 it became extremely slow. The reason is as follows:

In this question, we are using a DFS based approach, hence what happens is, it starts to look deeper and deeper in the tree in the same direction. The problem that arises because of this is given in the example below:

Say the first F was added in this position given below

....&&&<br/>  
.&&&...<br/>  
....&..<br/>  
.&.&...<br/>  
.&.&.&.<br/>  
#&..F&@<br/>  
_________________________________________________________________________________________________________________________________

When we solve the program using DFS it first looks for all the options with this F fixed in the same position. Now, with F in this position, this problem will never have a solution for K=9. This causes the program to be extremely slow.

A way in which I overcame this problem is instead of going in the first direction of depth output by the successor function, we can randomize the direction in which the search is being started from. This successor function always gives the same start point which is




....&&&<br/>  
.&&&...<br/>  
....&..<br/>  
.&.&...<br/>  
.&.&.&.<br/>  
#&..F&@<br/>  
_________________________________________________________________________________________________________________________________

But if we randomly choose the point where we start from the chance of success increases which is how I managed to make it work for K=9.

Now after thinking for a couple of more days I came up with another version of successor function

My final version of the successor function was as follows:

def not_eliminate_state(board,row,col):
          
        

         for i in range(col,-1,-1):
                 if board[row][i]=='&':
                         break
                 if board[row][i]=='F':
                         return False
         for i in range(col+1,len(board[0])):
                 if board[row][i]=='&':
                         break
                 if board[row][i]=='F':
                         return False
         for i in range(row,-1,-1):
                 if board[i][col]=='&':
                         break
                 if board[i][col]=='F':
                         return False
         for i in range(row+1,len(board)):
                 if board[i][col]=='&':
                         break
                 if board[i][col]=='F':
                         return False
         return True

Here we eliminate the state before entering it into the fringe itself rather than removing them after entering into fringe. Hence the add_friend function was modified slightly:

def successors(board):
        return [add_friend(board, r, c) for r in range(0, len(board)) for c in range(0,len(board[0])) if board[r][c] == '.' and not_eliminate_state(board,r,c)]

The state checking is being done in the above condition itself.

This was also done along with the help of a random shuffling which seems to speed up the search by a huge margin.


One issue I encountered here is that it takes a massive amount of time which I realised is because of duplicate states.I fixed this with a small piece of extra code.

           if s not in visited:
                       fringe.append(s)
                       visited.append(s)
<b>Cost Function:</b>

The cost function used here is moving from one state to another. Here, it is just the cost of adding one F more than the previous state.

<b>Conclusions:</b>

->The program by itself takes a while to run but with the introduction of the random shuffling it speeds up a lot. So, this I feel was something innovative I did to make my program run faster.




