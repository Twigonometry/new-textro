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
            location_intro = "crouched by a small fire in an oil can, staring emptily into the flames. "
            weapon_intro = "They keep their makeshift weapons close by as they tend to a slowly turning piece of meat that is mostly bone."
        elif location_type == world.LocationType.OUTDOORS:
            location_intro = "kicking stones down this abandoned street, shadowed by the empty husks of heavily shelled buildings. "
            weapon_intro = "They clutch their makeshift beatsticks and thrown together catapults close to their belts as they scavenge for money or meat."
        if quantity > 1:
            plural = "The bandits are "
        else:
            plural = "The bandit is "
        
        print(plural + location_intro + "Their clothes are dusty and torn, but rough hide armour can be seen underneath the ragged holes. " + weapon_intro)

    
    def fight(self):
        """chase down player and engage in melee combat. retreat once below 10% HP;
        should be passed a combat_encounter object that describes state of current combat"""

    def __init__(self, name, race, health, speed, host, mwn, mab, mdd, mdb, hra, rwn, rab, rdd, rdb):
        super().__init__(name, race, health, speed, host, mwn, mab, mdd, mdb, hra, rwn, rab, rdd, rdb)