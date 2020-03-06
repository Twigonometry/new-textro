import npc
import world_engine as world
import encounter as enc_class
import utils

class Bandit(npc.NPC):
    """basic bandit enemy"""

    def display_stats(self):
        return super().display_stats()

    def introduce(self, quantity, location_type):
        location_intro = ""
        weapon_intro = ""
        plural = ""

        if location_type == world.LocationType.INDOORS:
            location_intro = "crouched by a small fire in an empty oil drum, staring emptily into the flames. "
            weapon_intro = "They keep their makeshift weapons close by as they tend to a slowly turning piece of meat that is mostly bone."
        elif location_type == world.LocationType.OUTDOORS:
            location_intro = "kicking stones down this abandoned street, shadowed by the empty husks of heavily shelled buildings. "
            weapon_intro = "They clutch their makeshift beatsticks and thrown together catapults close to their belts as they scavenge for money or meat."
        if quantity > 1:
            plural = "The bandits are "
        else:
            plural = "The bandit is "
        
        print(plural + location_intro + "Their clothes are dusty and torn, but rough hide armour can be seen underneath the ragged holes. " + weapon_intro)

    def interact(self, encounter, npc_index, player):
        super().interact(encounter, npc_index, player)

        close_proximity = encounter.npc_distances[npc_index] < 10

        #avoid option only available if further than 10ft away
        if not close_proximity:
            print("5. Turn around and avoid the bandits.")

        choice = 0
        while choice < 1 or choice > 5:
            try:
                choice = int(input("Enter choice: "))
            except:
                print("Enter an integer between 1 and 5")

        #based on choice, return a flag to encounter method that tells it what to do next
        if choice == 1:
            #approaching hostile bandit starts combat encounter
            if self.hostility == utils.HostilityLevel.HOSTILE:
                print("You approach the bandit, hoping to start a dialogue, but they launch into a desperate rage and charge towards you.")
                return enc_class.NextState.COMBAT
            else:
                print("You approach the bandit and, to your surprise, they look up without immediately reaching for their weapon.")
                return enc_class.NextState.SOCIAL
        elif choice == 2:
            print("You charge into combat, and the bandit looks up and grabs their weapon.")
            return enc_class.NextState.COMBAT
        elif choice == 3:
            #make stealth check - present next area if success, launch combat if failure
            print("You take a deep, silent breath, and try to tiptoe past the bandit.")
        elif choice == 4:
            #make stealth check - allow options to pickpocket/backstab/subdue if success, launch combat if failure
            print("You take a deep, silent breath, and approach the bandit from behind.")
        elif choice == 5:
            #leave the area and return to the previous one
            print("You turn around, unnoticed by the bandit.")
    
    def fight(self, combat_encounter, npc_index):
        """chase down player and engage in melee combat. retreat once below 10% HP;
        takes a combat_encounter object that describes state of current combat, and its own index within that encounter"""
        print(self.name + " fighting\n")
        print("Index: ", npc_index)

        dist = combat_encounter.npc_distances[npc_index]
        if dist > 5:
            new_dist = super().approach_player(dist)

            print("The bandit approaches you! It is now " + str(new_dist) + "ft. away\n")

            #update adjacencies
            if new_dist <= 5:
                combat_encounter.adjacent_npcs[npc_index] = True

            #update distances
            combat_encounter.npc_distances[npc_index] = new_dist

    def alert_close_proximity(self, multiple):
        if multiple:
            print("You are too close to turn away or attempt to hide from the closest bandit, and they attack you on sight!")
        else:
            print("You are too close to turn away or attempt to hide from the bandit, and they attack you on sight!")

    def __init__(self, name, race, health, AC, speed, size, host, mwn, mab, mdd, mdb, hra, rwn, rab, rwr, rdd, rdb, pen, abils, skills_dict):
        super().__init__(name, race, health, AC, speed, size, host, mwn, mab, mdd, mdb, hra, rwn, rab, rwr, rdd, rdb, pen, abils, skills_dict)