""" Create PyGameAIPlayer class here"""
import pygame
import math
from lab11.turn_combat import CombatPlayer

class PyGameAIPlayer:
    



    def __init__(self,state) -> None:
        def getNeighbors(state, graph):
            n = []

            for i in range(10):
                if self.graph[state.cities.index(state.current_city)][i] != 0:
                    n.append(i)
            return n

        def genGraph(state):
            len(state.cities)
            graph = [[0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    ]

            for r in state.routes:
                pointA = r[0]
                pointB = r[1]

                cost = math.sqrt((pointB[0] - pointA[0])**2 + (pointB[0] - pointA[0])**2)

                graph[state.cities.index(r[0])][state.cities.index(r[1])] = cost
            return graph
        
        print(state.current_city)
        self.path = [state.current_city]
        self.visited = []
        self.graph = genGraph(state)

        #continue till destination is reached or path is empty
        while state.current_city != state.destination_city and self.path:
            n = getNeighbors(state, graph)
            #If there are no neighbors
            if not n and self.path:
                self.path.pop(-1)
            #if the current citty is connected to destination
            elif n.count(state.destination_city) != 0:
                self.path.append(state.destination_city)
            else:
                #get lowest distance    
                n.sort()
                for i in range(len(n)):
                    if self.visited.count(n[i]) == 0:
                        self.path.append(n[i])
                        self.visited.append(n[i])
                        break
        #if no path exists
        if not self.path:
            print("The is no viable path. Useing acient magic to telaport")
            self.path.append[state.destination_city]
        
        pass   
  
   


    def selectAction(self, state):

        choice = self.path[-1]
        

        self.path.pop(-1)
        return ord(str(choice))


""" Create PyGameAICombatPlayer class here"""
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.model_selection import train_test_split
import random

class PyGameAICombatPlayer(CombatPlayer):
    def __init__(self, name):
        super().__init__(name)

    def weapon_selecting_strategy(self):
            if len(self.my_choices) == 0:
                print("init")
                self.weapon = random.randint(1,3) - 1
                return self.weapon 
            
            else:
                if self.opponent_choices[-1] == 0:
                    self.weapon =1
                    return self.weapon
                
                elif self.opponent_choices[-1] == 1:
                    self.weapon =2
                    return self.weapon
                else:
                    self.weapon =2
                    return self.weapon

                


pass
