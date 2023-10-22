#!/usr/bin/env python
# coding: utf-8

# ### Assignment: Python (Advanced)
# #### Parsing Data
# ##### Relationship Status

# In[1]:


def relationship_status(from_member, to_memeber, social_graph):
    if from_member in social_graph and to_member in social_graph:
        fmt = to_member in social_graph[from_member]["following"]
        tmf = from_member in social_graph[to_member]["following"]
        if fmt and tmf:
            return from_member, "is friends with", to_member
        elif fmt:
            return from_member, "is a follower of", to_member
        elif tmf:
            return from_member, "is followed by", to_member
    return from_member, "and", to_member, "has no relationship"


# In[18]:


from_member = str(input("From member: "))
to_member = str(input("To member: "))
social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  " last_name":"Olpoc",
                  "following":[
                  ]
    },
     "@joaquin":{"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
     "@chums":{"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}

relationship = relationship_status(from_member, to_member, social_graph)
print(relationship)


# ##### Tic Tac Toe

# In[30]:


def tic_tac_toe(board):
    def check(symbol):
        n = len(board)
        for i in range(n):
            if all(cell == symbol for cell in board[i]):
                return True
            if all(row[i] == symbol for row in board):
                return True
        if all(board[i][i] == symbol for i in range(n)) or all(board[i][n-1-i] == symbol for i in range(n)):
            return True
        return False
    if check("X"):
        return "X"
    if check("O"):
        return "O"
    
    return "NO WINNER"


# In[35]:


board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]

board = [board1, board2, board3, board4, board5, board6, board7]

for i, board in enumerate(board, start=1):
    winner = tic_tac_toe(board)
    print(f"Board {i}: Winner - {winner}")


# ##### ETA

# In[49]:


def eta(first_stop, second_stop, route_map):
    start = first_stop
    total_time = 0
    legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
    }
}
    while start != second_stop:
        leg = (start, route_map[start])
        travel_time = legs[leg]["travel_time_mins"]
        total_time += travel_time
        start = route_map[start]
    return total_time


# In[57]:


first_stop = str(input("Depart: "))
second_stop = str(input("Arrive: "))
route_map = {
        "upd" : "admu",
        "admu" : "dlsu",
        "dlsu" : "upd",
}

time = eta(first_stop, second_stop, route_map)
print("Route will take", time, "minutes.")

