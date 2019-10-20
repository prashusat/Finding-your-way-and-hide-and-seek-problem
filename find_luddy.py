#!/usr/local/bin/python3
#
# find_luddy.py : a simple maze solver
#
# Submitted by : [PUT YOUR NAME AND USERNAME HERE]
#
# Based on skeleton code by Z. Kachwala, 2019
#

import sys
import json

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().split("\n")]

# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
	return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
	moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))

	# Return only moves that are within the board and legal (i.e. on the sidewalk ".")
	return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]
#A funnction which tracks the move made when you go from one state to another and appends the direction to the state.
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
def queue(fringe):
#https://stackoverflow.com/questions/4426663/how-to-remove-the-first-item-from-a-list
#The line below was referred from the link above
#################################################
        return fringe.pop()
#################################################
def search1(IUB_map):
	# Find my start position
	you_loc=[(row_i,col_i) for col_i in range(len(IUB_map[0])) for row_i in range(len(IUB_map)) if IUB_map[row_i][col_i]=="#"][0]
	#At every state along with the move that has been made,and the distance covered,i add one more object which is a string keeping track of the path traversed until now in terms of NORTH,SOUTH,EAST,WEST.
	fringe=[(you_loc,0,"")]
	visited=[]
	while fringe:
                #In the next line I called a queue function defined by me above which changes the original stack based implementation given in the skeleton code to a queue based implementation!!
		(curr_move, curr_dist,tracked_by_compass)=queue(fringe)
		for move in moves(IUB_map, *curr_move):
                        
			if IUB_map[move[0]][move[1]]=="@":
				return curr_dist+1,tracked_by_compass+compass(move,curr_move)
			if move not in visited:

                                
				fringe.append((move, curr_dist + 1,tracked_by_compass+compass(move,curr_move)))
				visited.append(move)
			
	              
	if (len(fringe)==0):
                        return "Inf",""
if __name__ == "__main__":
	IUB_map=parse_map(sys.argv[1])
	print("Shhhh... quiet while I navigate!")
	solution,compass = search1(IUB_map)
	print("Here's the solution I found:")
	print(solution,compass)
                
   
	
