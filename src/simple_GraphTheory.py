# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:03:09 2020

@author: rbv
"""

# BFS & DFS

LIFO_list = list()

def LIFO_push(LIFO_list,element):
    LIFO_list.append(element)

def LIFO_pop(LIFO_list):
    return LIFO_list.pop(-1)

def add_to_explored_vertices(explored_vertices,vertex):
    explored_vertices.append(vertex)

def is_explored(explored_vertices,vertex):
    return vertex in list(explored_vertices)
    
def DFS(maze_graph, initial_vertex):
    # Define the appending structures
    explored_vertices = list()
    queuing_structure = list()
    parent_dict = dict(maze_graph)
    
    # Push initial vertex:
    LIFO_push(queuing_structure, (initial_vertex, None))
    
    # Start graph traversal
    while len(queuing_structure) > 0:
        current_vertex, parent = LIFO_pop(queuing_structure)
        
        if current_vertex not in explored_vertices:
            explored_vertices.append(current_vertex)
            parent_dict[current_vertex] = parent
            
            for neigh in maze_graph[current_vertex]:
                LIFO_push(queuing_structure, (neigh, current_vertex)) 
        
    return explored_vertices, parent_dict

FIFO_list = list()

def FIFO_push(FIFO_list,element):
    FIFO_list.append(element)

def FIFO_pop(FIFO_list):
    return FIFO_list.pop(0)

def BFS(maze_graph, initial_vertex):
    # Define the appending structures
    explored_vertices = list()
    queuing_structure = list()
    parent_dict = dict(maze_graph)
    
    # Push initial vertex:
    FIFO_push(queuing_structure, (initial_vertex, None))
    
    # Start graph traversal
    while len(queuing_structure) > 0:
        current_vertex, parent = FIFO_pop(queuing_structure)
        
        if current_vertex not in explored_vertices:
            explored_vertices.append(current_vertex)
            parent_dict[current_vertex] = parent
            
            for neigh in maze_graph[current_vertex]:
                FIFO_push(queuing_structure, (neigh, current_vertex)) 
        
    return explored_vertices, parent_dict


def create_walk_from_parents(parent_dict,initial_vertex,target_vertex):  
    # Create empty path list
    path = []
    # Check that the initial and target vertex are not the same,
    # otherwise return empty path
    if initial_vertex == target_vertex:
        return path
    else:
        # Defining the parents of the initial and target vertexes
        parent_i = parent_dict[initial_vertex]
        parent_t = parent_dict[target_vertex]
        # Troubleshooting if final target is the main parent of the tree
        if parent_t == None:
            parent_t = parent_i
        else:
            pass
        # Append the target index and its parent
        curr_parent = parent_t
        path.append(target_vertex)
        path.append(curr_parent)
        # In case the path is of length one, return the path before the loop
        if curr_parent == initial_vertex:
            return path
        else:
            # Now appending the parents in a loop
            for _ in range(len(parent_dict)):
                curr_parent = parent_dict[curr_parent]
                path.append(curr_parent)
                if curr_parent == initial_vertex:
                    path.pop(-1)
                    return path[::-1]
                else:
                    pass
    path.pop(-1)
    return path[::-1]
        

# DIJKSTRA ALGORITHM
# heap_pop function returns the first element of the list implementing the heap, providing the heap is not empty
def heap_pop(heap):
    if heap != []:
        vertex,weight,parent = heap.pop(0)
        return (vertex, weight, parent)
    else:
        raise

def heap_add_or_replace(heap, triplet):
    """
    Given a heap and a triplet (vertex, distance and parent), this function
    checks whether there is another same vertex in the heap, then replaces it
    if the input triplet has a smaller distance or does not do anything. If the 
    vertex of the triplet is not in the heap, the new triplet is added in ascending
    order of distance.
    """
    
    # First consider the case in which the heap is empty, then simply add the 
    # input triplet without worrying about order.
    if heap == []:
        heap.append(triplet)
        
    else:
        # Otherwise, first extract the information from the triplet
        vertex, distance, parent = triplet
        
        # Now, go through the heap and make a list of vertices and distances
        V = [heap[i][0] for i in range(len(heap))]
        D = [heap[i][1] for i in range(len(heap))]
        
        # If the input vertex has already a competing vertex in the heap, check
        # for replacement.
        if vertex in V:
            for i in range(len(heap)):
                # If the distance of the input triplet is greater than the one
                # in the heap, then we do not do anything.
                if vertex == V[i] and distance >= D[i]:
                    return None
                
                # Otherwise we need to replace it
                elif vertex == V[i] and distance < D[i]:
                    D[i] = distance
                    heap[i] = vertex, distance, parent
                    
                    # Still need to sort everything the heap in ascending
                    # order wrt to the distances
                    D = sorted(D)
                    idx = [D.index(heap[i][1]) for i in range(len(heap))]
                    print(idx)
                    
                    if idx != [i for i in range(len(heap))]:
                        heap[0], heap[1] = heap[1], heap[0] 
                    else:
                        pass
                    return None
        
        else:
            # If the input triplet does not have a competing vertex in the heap,
            # add it in the heap and sort wrt to distance in ascending order
            D.append(distance)
            D = sorted(D)
            idx = D.index(distance)
            heap.insert(idx, triplet)            

            
            return None
        
          
class my_dictionary(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value 
  
  
def is_explored(explored_vertices,vertex):
    return vertex in explored_vertices

def add_to_explored_vertices(explored_vertices,vertex):
    explored_vertices.append(vertex)
    
def Dijkstra(maze_graph,initial_vertex):
    # Creating empty data structures
    explored_vertices = list()     # Variable storing the exploredled vertices vertexes not to go there again
    heap = list()                  # stack of vertexes
    parent_dict = my_dictionary()           # parent dictionary to have the same keys as the graph
    distances = my_dictionary()           # distances dictionary
    
    # Initializing heap
    initial_vertex = (initial_vertex, 0, initial_vertex)   # vertex to visit, distance from origin, parent
    heap_add_or_replace(heap,initial_vertex)
    
    # Implementing Dijkstra
    while len(heap) > 0:
        # Get triplet from heap list calling heap_pop() function.
        triplet = heap_pop(heap)
        vertex, distance, parent = triplet
        
        if is_explored(explored_vertices, vertex) is not True:
            
            # Map the vertex to its corresponding parent, add vertex to explored
            # and add distance to Distances data structure.
            parent_dict.add(vertex, parent)
            add_to_explored_vertices(explored_vertices, vertex)
            distances.add(vertex, distance)
            
            # For each unexplored neighbor i of the vertex connected through an edge 
            # of weight w_i, add (i, distance + wi, vertex) to the heap.
            for neigh in maze_graph[vertex]:
                neigh_vertex = neigh
                w_i = maze_graph[vertex][neigh_vertex]
                new_triplet = (neigh_vertex, w_i + distance, vertex)
                heap_add_or_replace(heap,new_triplet)
                
    return explored_vertices, parent_dict, distances   
