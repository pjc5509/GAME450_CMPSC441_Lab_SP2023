""" Create PyGameAIPlayer class here"""
import pygame
from lab11.turn_combat import CombatPlayer

class PyGameAIPlayer:
    def __init__(self) -> None:
        pass

    def selectAction(self, state):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if ord("0") <= event.key <= ord("9"):
                    return event.key
        return ord(str(state.current_city))  # Not a safe operation for >10 cities


""" Create PyGameAICombatPlayer class here"""
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
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
