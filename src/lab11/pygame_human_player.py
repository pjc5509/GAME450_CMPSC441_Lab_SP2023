import pygame
from lab11.turn_combat import CombatPlayer


class PyGameHumanPlayer:
    def __init__(self) -> None:
        pass
    
    #Checks if destination is connected to start
    def isRoute(self, routes, start, destination):
        for route in routes:
            if route == (start, destination) or route ==  (destination, start):
                return 1
        return 0

    def selectAction(self, state):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if ord("0") <= event.key <= ord("9"):
                    if self.isRoute(state.routes, state.cities[state.current_city], state.cities[int(chr(event.key))]) == 1:
                        #state.gold -= 10
                        return event.key
        return ord(str(state.current_city))  # Not a safe operation for >10 cities


class PyGameHumanCombatPlayer(CombatPlayer):
    def __init__(self, name):
        super().__init__(name)

    def weapon_selecting_strategy(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key in [ord("s"), ord("a"), ord("f")]:
                        choice = {ord("s"): 1, ord("a"): 2, ord("f"): 3}[event.key]
                        self.weapon = choice - 1
                        return self.weapon
