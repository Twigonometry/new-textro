import utils
import player
import npc

class Encounter():
    main_player = None

    #list of NPC objects
    npc_list = []
    npc_distances = []

    def begin_encounter(self):
        """run encounter from start;
        introduce NPCs, present interaction choices, and start social/combat encounter based on choices"""
        #introduce NPCs - run all introduce methods, unless the NPCs are of the same type

        #select NPC to interact with
        #interactions may return flags that spawn social/combat encounters

        #spawn social/combat encounter
        #if combat, pass npc list to generate turn order

        #when encounter ends, present next choices and any loot from area

    def __init__(self, _player, _npc_list, _npc_distances):
        super().__init__()
        self.main_player = _player
        self.npc_list = _npc_list
        self.npc_distances = _npc_distances

        self.main_player.display_stats()
        
        for i in range(len(self.npc_list)):
            self.npc_list[i].display_stats()
            print("Distance: ", self.npc_distances[i])