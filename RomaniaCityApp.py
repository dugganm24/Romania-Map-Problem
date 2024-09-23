#from SimpleProblemSolvingAgent import SimpleProblemSolvingAgent
import SPSA 
from search import romania_map, Node, GraphProblem 
from cities import get_city_input, origin, destination
import sys
from collections import deque

from utils import *

def main():
    
    #print map
    print(f"Here are all the possible Romania cities that can be traveled:\n{list(romania_map.locations.keys())}")

    while True:
        
        #user input for origin and destination
        #store globally for utilization elsewhere
        origin = get_city_input("Please enter the origin city: ")
        destination = get_city_input("Please enter the destination city: ")

        #check if origin and destination are same city 
        if origin == destination:
            print("The same city can't be both origin and destination. Please try again.")
            continue
        
        #define graph problem
        romaniaProblem = GraphProblem(origin, destination, romania_map)
       
        #informed search implementation:
        path = SPSA.best_first_graph_search(romaniaProblem, romaniaProblem.h)
        result = path.path()
        print("\nGreedy Best-First Search")
        print("Path:" + result[0].state, end=" ")
        for i in range(1, len(result)):
            print(" -> " + result[i].state, end=" ")
        print("\nTotal Cost:" + str(result[-1].path_cost))
        print("\n")

        
        path = SPSA.astar_search(romaniaProblem)
        result = path.path()
        print("\nA* Search")
        print("Path:" + result[0].state, end=" ")
        for i in range(1, len(result)):
            print(" -> " + result[i].state, end=" ")
        print("\nTotal Cost:" + str(result[-1].path_cost))
        print("\n")

        #local search implementation:
        result = SPSA.hill_climbing(romaniaProblem)
        #check if stuck
        if "Plateau" in result:
            result.remove("Plateau")
        print("Hill Climbing Search")
        print("Path: " + result[0].state, end=" ")
        for i in range(1, len(result)):
            print(" -> " + result[i].state, end=" ")
        print("\nTotal Cost: " + str(result[-1].path_cost))
        print("\n")

              
        result = SPSA.simulated_annealing(romaniaProblem)
        #check if stuck 
        if "Plateau" in result:
            result.remove("Plateau")
        print("Simulated Annealing Search")
        print("Path: " + result[0].state, end=" ")
        for i in range(1, len(result)):
            print(" -> " + result[i].state, end=" ")
        print("\nTotal Cost: " + str(result[-1].path_cost))
        print("\n")
        
        
        #check if user repeat program
        repeat = input("\nWould you like to find the best path between the other two cities?").capitalize()
        if repeat.lower() != "yes":
            print("Thank You for Using Our App")
            break
        

if __name__ == "__main__":
    main()
