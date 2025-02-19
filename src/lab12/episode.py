''' 
Lab 12: Beginnings of Reinforcement Learning
We will modularize the code in pygrame_combat.py from lab 11 together.

Then it's your turn!
Create a function called run_episode that takes in two players
and runs a single episode of combat between them. 
As per RL conventions, the function should return a list of tuples
of the form (observation/state, action, reward) for each turn in the episode.
Note that observation/state is a tuple of the form (player1_health, player2_health).
Action is simply the weapon selected by the player.
Reward is the reward for the player for that turn.
'''
import sys
from pathlib import Path

# line taken from turn_combat.py
sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))

from lab11.turn_combat import CombatPlayer, Combat
from lab11.pygame_combat import PyGameComputerCombatPlayer
from lab11.pygame_human_player import PyGameHumanCombatPlayer
    

def run_episode(player1, player2):
    RL = []
    
    
    episode = Combat()
    while not episode.gameOver:
        start_hp1 = player1.health
        start_hp2 = player2.health

        State = (player1.health, player2.health) 

        

        #Run combat turn
        player1.selectAction((State))
        player2.selectAction(State)
        episode.newRound()
        episode.takeTurn(player1, player2)
        print("%s's health = %d" % (player1.name, player1.health))
        print("%s's health = %d" % (player2.name, player2.health))
        episode.checkWin(player1, player2)
    

        
        Action = player1.weapon

        #calculate reward
        Reward = 0
        if start_hp1 > player1.health:
            Reward -= 5
        if start_hp2 > player2.health:
            Reward += 2
        elif start_hp2 == player2.health and player1.weapon == player2.weapon:
            Reward-=50
        
  
        RL.append((State, Action, Reward))
    return RL

if __name__ == "__main__":
    player = PyGameHumanCombatPlayer("player")
    op = PyGameComputerCombatPlayer("CPU")
    
    print(run_episode(player, op))
        
