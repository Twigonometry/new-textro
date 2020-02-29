"""main game engine that displays text messages to screen"""

import utils
import player
import NPCs.bandit as bandit
import Encounters.encounter as encounter
import world_engine as world

#necessary background variables
hostility = utils.HostilityLevel
location_type = world.LocationType

def main():
    print("Hello New Metro")
    main_player = player.Player()

if __name__ == '__main__':
    main()