import utils
import player
import npc
import world_engine as world

class Encounter():
    main_player = None

    #list of NPC objects
    npc_list = []
    npc_distances = []

    location = world.LocationType

    def begin_encounter(self):
        """run encounter from start;
        introduce NPCs, present interaction choices, and start social/combat encounter based on choices"""

        #introduce NPCs - run all introduce methods, unless the NPCs have the same name
        #npc_indices tracks index of npc to introduce
        npc_names = []
        npc_indices = []
        npc_quantities = []

        #finding enemy quantities by name
        for i in range(len(self.npc_list)):
            _npc = self.npc_list[i]
            if _npc.name not in npc_names:
                npc_names.append(_npc.name)
                npc_indices.append(i)
                npc_quantities.append(1)
            else:
                for j in range(len(npc_names)):
                    if npc_names[j] == _npc.name:
                        npc_quantities[j] += 1
        
        #call introduce methods
        for k in range(len(npc_indices)):
            npc_index = npc_indices[k]
            self.npc_list[npc_index].introduce(npc_quantities[k], self.location)

        #select NPC to interact with
        #interactions may return flags that spawn social/combat encounters

        #spawn social/combat encounter
        #if combat, pass npc list to generate turn order

        #when encounter ends, present next choices and any loot from area

    def __init__(self, _player, _npc_list, _npc_distances, _location):
        super().__init__()
        self.main_player = _player
        self.npc_list = _npc_list
        self.npc_distances = _npc_distances
        self.location = _location

        self.begin_encounter()