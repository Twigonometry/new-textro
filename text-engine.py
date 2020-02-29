"""main game engine that displays text messages to screen"""

import utils
import player
import NPCs.bandit as bandit

#necessary background variables
hostility = utils.HostilityLevel

def main():
    print("Hello New Metro")
    #main_player = player.Player()
    bandit1 = bandit.Bandit("Bandit", "Human", 22, 30, hostility.HOSTILE, "Wrench", 1, (8, 1), 1, True, "Catapult", 1, (6, 1), 1)
    bandit1.display_stats()

if __name__ == '__main__':
    main()