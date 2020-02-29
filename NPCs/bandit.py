import npc

class Bandit(npc.NPC):
    """basic bandit enemy"""

    def display_stats(self):
        return super().display_stats()

    def fight(self):
        """chase down player and engage in melee combat. retreat once below 10% HP;
        should be passed a combat_encounter object that describes state of current combat"""

    def __init__(self, name, race, health, speed, host, mwn, mab, mdd, mdb, hra, rwn, rab, rdd, rdb):
        super().__init__(name, race, health, speed, host, mwn, mab, mdd, mdb, hra, rwn, rab, rdd, rdb)