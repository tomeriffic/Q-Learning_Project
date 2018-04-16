import numpy as np
import pylab as plt

# Fenchruch Street to Angel
# In order of 1st by fenchurch street 
# If Above 10 list with *

# Name							        
# 0.  Windsor Fenchurch,			      	
# 1.  The Swan Tavern,				      
# 2.  Corney & Barrow Lime Street,	    
# 3.  The Swan						   
# 4.  The Crosse Keys				   
# 5.  Golden Fleece					    
# 6.  The Vintry					    
# 7.  Cock & Woolpack				
# 8.  One New Change, Rooftop Bar,	
# 9. Williamson's Tavern			
# 10. The Viaduct Tavern			
# 11. The Sutton Arms               
# 12. The Jerusalem Tavern          
# 13. Grand Union Farringdon        
# 14. Lord Raglan                   
# 15. Betsey Trotwood               
# 16. The Slaughtered Lamb
# 17. The Blacksmith & The Toffeemaker
# 18. Old Red Lion Theatre Pub      
# 19. The Angel                    
#

# Graph with minutes from state to 
#	/	0	1	2	3	4	5	6	7	8	9	10  11  12  13  14  15  16  17  18  19
#	0	/	2,	3,	6,	7,	,	,	9,	,	,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,
#	1	,	/	3,	4,	5,	,	9,	7,	,	,	,   ,   ,   ,   ,   ,   ,   ,   ,   ,
#	2	,	,	/	4,	5,	,	,	6,	,	,	,   ,   ,   ,   ,   ,   ,   ,   ,   ,
#	3	,	,	,	/	2,	9,	6,	4,	,	,	,   ,   ,   ,   ,   ,   ,   ,   ,   ,
#	4	,	,	,	,	/	9,	7,	3,	,	,	,   ,   ,   ,   ,   ,   ,   ,   ,   ,
#	5	,	,	,	,	,	/	7,	8,	4,	2,	9,  ,   ,   ,   8,  ,   ,   ,   ,   ,
#	6	,	,	,	,	,	,	/	5,	9,	8,	,   ,   ,   ,   ,   ,   ,   ,   ,   ,  
#	7	,	,	,	,	,	,	,	/	,	9,	,   ,   ,   ,   ,   ,   ,   ,   ,   ,
#	8	,	,	,	,	,	,	,	,	/	3,	6,  ,   ,   ,   6,  ,   ,   ,   ,   ,  
#	9	,	,	,	,	,	,	,	,	,	/	9,  ,   ,   ,   7,  ,   ,   ,   ,   ,
#	10	,	,	,	,	,	,	,	,	,	,	/   8,  ,   5,  7,  ,   ,   ,   ,   ,
#   11  ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   /   8,  5,  7,  ,   8,  ,   ,   ,
#   12  ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   /   6,  ,   5,  5,  ,   ,   ,
#   13  ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   /   ,   9,  8,  ,   ,   ,
#   14  ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   /   ,   ,   ,   ,   ,
#   15  ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   /   8,  ,   ,   ,
#   16  ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   /   9,  ,   ,
#   17  ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,       /   5,  ,
#   18  ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,       ,   /   6,
#   19  ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,       ,   ,   /

# 1  -> {2, 3, 4, 5, 7, 8}
# 2  -> {3, 4, 5, 7, 8}
# 3  -> {4, 5, 8}
# 4  -> {5, 6, 7, 8}
# 5  -> {6, 7, 8}
# 6  -> {7, 8, 9, 10, 11, 15}
# 7  -> {8, 9, 10}
# 8  -> {10}
# 9  -> {10, 11, 15}
# 10 -> {11, 15}
# 11 -> {12, 14, 15}
# 12 -> {13, 14, 15, 17}
# 13 -> {14, 16, 17}
# 14 -> {16, 17}
# 15 -> {}
# 16 -> {17}
# 17 -> {18}
# 18 -> {19}
# 19 -> {20}
# 20 -> {}


# map State to action
state_action_list = [(0,1), (0,2), (0,3), (0,4), (0,6), (0,7), (1,2), (1,3), (1,4), (1,6), (1,7), (2,3),
    (2,4), (2,7), (3,4), (3,5), (3,6), (3,7), (4,5), (4,6), (4,7),
    (5,6), (5,7), (5,8), (5,9), (5,10), (5,14),
    (6,7), (6,8), (6,9),(7,9), (8,9), (8,10), (8,14), (9,10), (9,14), (10,11), (10,13), (10,14),
    (11,12), (11,13), (11,14), (11,16), (12,13), (12,15), (12,16), (13,15), (13,16), (14,15),
    (15,16),(16,17),(17,18),(18,19)]

#Goal state initialised
goal = 19

#Import used to create network diagram
#https://networkx.github.io/documentation/networkx-1.9.1/tutorial/tutorial.html?highlight=graph
import networkx as nx
#Create an empty graph
G=nx.Graph()
#Adds multiple edges. edges defined in the state_action_list
G.add_edges_from(state_action_list)
#Positions nodes in specific algorithm
pos = nx.spring_layout(G)
#Draw nodes/states of graph G in positions
nx.draw_networkx_nodes(G,pos)
#Draw edges of graph G in positions
nx.draw_networkx_edges(G,pos)
#Draw state labels
nx.draw_networkx_labels(G,pos)
#Uncomment to show the generated G graph
# plt.show()

# Matrix size, used for R and Q matrices
MATRIX_SIZE = 20

# create matrix x*y
R = np.matrix(np.ones(shape=(MATRIX_SIZE, MATRIX_SIZE)))
#Set all values in matrix R to -1
R *= -1
#Uncomment to display R matrix before setting values
#print(R)

# assign zeros to paths and 100 to goal-reaching state_action
for state_action in state_action_list:
    if state_action[1] == goal:
        #If the first part of tuple is the goal value of 19 set to 100
        R[state_action] = 100
    else:
        #If a state_action exists from the state_action_list assign 0
        #Edge exists
        R[state_action] = 0
    #Inversed operations occour here
    if state_action[0] == goal:
        R[state_action[::-1]] = 100
    else:
        # reverse of state_action
        R[state_action[::-1]]= 0

#Uncomment to print R matrix following population
#print(R)

#create Q matrix with 0 values matrix_size x*y
Q = np.matrix(np.zeros([MATRIX_SIZE,MATRIX_SIZE]))


#Learning parameter Gamma
gamma = 0.8
#Learning parameter Aplha
alpha = 0.1
# Episodes
episodes = 300

#Start state
initial_state = 1

#Function to retrun all possible actions
def available_actions(state):
    current_state_row = R[state,]
    av_act = np.where(current_state_row >= 0)[1]
    return av_act

available_act = available_actions(initial_state) 

#function to return a random action from the avaliable actions
def sample_next_action(available_actions_range):
    next_random_action = int(np.random.choice(available_act,1))
    return next_random_action

action = sample_next_action(available_act)

def update(current_state, action, gamma):
    
  max_index = np.where(Q[action,] == np.max(Q[action,]))[1]
  
  if max_index.shape[0] > 1:
      max_index = int(np.random.choice(max_index, size = 1))
  else:
      max_index = int(max_index)
  max_value = Q[action, max_index]
  
  #Q-Learning Function for Gamma Only
  #Q[current_state, action] = R[current_state, action] + gamma * max_value
  #Q-Learning Function for Gamma and Alpha
  Q[current_state, action] = R[current_state, action] + (alpha * R[current_state, action]  + gamma * max_value) - Q[current_state, action]

  #print('max_value', R[current_state, action] + gamma * max_value)
  
  if (np.max(Q) > 0):
    return(np.sum(Q/np.max(Q)*100))
  else:
    return (0)
    
update(initial_state, action, gamma)

# Training
#Initialise scores list to empty
scores = []
#For each iteration of episodes
for i in range(episodes):
    #current state is random number between 0 and 19 
    current_state = np.random.randint(0, int(Q.shape[0]))
    #store avaliable actions in available_act from the current state
    available_act = available_actions(current_state)
    #next action stored in action
    action = sample_next_action(available_act)
    #score is the return of update
    score = update(current_state,action,gamma)
    #Add to end of scores list
    scores.append(score)
    #print ('Score:', str(score))
    
#Uncomment to Print the trained Q matrix 
#print("Trained Q Matrix")   
#print(Q/np.max(Q)*100)

# Testing
#Start state
current_state = 0
steps = [current_state]

#while the current state is not the accept state
while current_state != 19:

    next_step_index = np.where(Q[current_state,] == np.max(Q[current_state,]))[1]
    
    if next_step_index.shape[0] > 1:
        next_step_index = int(np.random.choice(next_step_index, size = 1))
    else:
        next_step_index = int(next_step_index)
    #Add next_step_index to end of steps list
    steps.append(next_step_index)
    #set the current state to the next step
    current_state = next_step_index

#display line chart of scores list
plt.plot(scores)
#show
plt.show()