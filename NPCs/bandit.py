import npc
import world_engine as world

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
            #approaching bandit starts combat encounter
            print("You approach the bandit, hoping to start a dialogue, but they launch into a desperate rage and charge towards you.")
        elif choice == 2:
            print("You charge into combat, and the bandit looks up and grabs their weapon.")
        elif choice == 3:
            #make stealth check - present next area if success, launch combat if failure
            print("You take a deep, silent breath, and try to tiptoe past the bandit.")
        elif choice == 4:
            #make stealth check - allow options to pickpocket/backstab/subdue if success, launch combat if failure
            print("You take a deep, silent breath, and approach the bandit from behind.")
        elif choice == 5:
            #leave the area and return to the previous one
            print("You turn around, unnoticed by the bandit.")
    
    def fight(self):
        """chase down player and engage in melee combat. retreat once below 10% HP;
        should be passed a combat_encounter object that describes state of current combat"""

    def __init__(self, name, race, health, speed, host, mwn, mab, mdd, mdb, hra, rwn, rab, rdd, rdb):
        super().__init__(name, race, health, speed, host, mwn, mab, mdd, mdb, hra, rwn, rab, rdd, rdb)