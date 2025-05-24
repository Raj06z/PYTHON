import zombiedice

class SmarterZombie:
    """A bot that follows the rules and rerolls footsteps while taking calculated risks."""
    
    def __init__(self, name):
        self.name = name

    def turn(self, game_state):
        shotguns = 0
        brains = 0
        dice_rolled = zombiedice.roll()
        
        while dice_rolled and shotguns < 3:
            
            shotguns += dice_rolled['shotgun']
            brains += dice_rolled['brains']
            
            if shotguns >= 3:
                print(f"{self.name} got 3 shotguns! Lost all brains this round.")
                break  

            
            footsteps_to_reroll = dice_rolled['footsteps']
            if footsteps_to_reroll > 0:
                dice_rolled = zombiedice.roll() 
            else:
                print(f"{self.name} stops with {brains} brains!")
                break 
zombies = [SmarterZombie("Strategic Zomborg")]
zombiedice.runTournament(zombies=zombies, numGames=100)