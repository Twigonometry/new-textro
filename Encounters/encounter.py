import utils
import player
import npc
import world_engine as world
import enum

class NextState(enum.Enum):
    FINISHED = "FINISHED"
    COMBAT = "COMBAT"
    SOCIAL = "SOCIAL"
    DEATH = "DEATH"

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

        #list visible enemies
        self.display_npcs()

        #check close proximity - if hostile enemy within 10 ft, don't go to interact menu
        hostile_close_proximity = False
        
        for m in range(len(self.npc_distances)):
            if self.npc_distances[m] < 10:
                if self.npc_list[m].hostility == utils.HostilityLevel.HOSTILE:
                    hostile_close_proximity = True
                    multiple = npc_quantities[npc_names.index(self.npc_list[m].name)] > 1
                    self.npc_list[m].alert_close_proximity(multiple)
        
        if hostile_close_proximity:
            #start combat
            print("Starting combat")
        else:
            #run interaction choice menu - interactions may return flags that spawn social/combat encounters
            for l in range(len(self.npc_list)):
                print(str(l + 1) + ". " + self.npc_list[l].name + " (Distance: " + str(self.npc_distances[l]) + "ft.)")
            
            choice = 0
            while choice < 1 or choice > len(npc_names) + 1:
                try:
                    choice = int(input("Make selection: "))
                except:
                    print("Enter an integer between 1 and " + str(len(npc_names)))
            
            self.npc_list[choice - 1].interact(self, choice - 1, self.main_player)

        #spawn social/combat encounter
        #if combat, pass npc list to generate turn order

        #when encounter ends, present next choices and any loot from area

    def display_npcs(self):
        """quick description of npcs in current location"""
        if self.location == world.LocationType.INDOORS:
            print("In the room before you, you see:")

        for i in range(len(self.npc_list)):
            print("A " + self.npc_list[i].name + " (Distance: " + str(self.npc_distances[i]) + "ft.)")

    def __init__(self, _player, _npc_list, _npc_distances, _location):
        super().__init__()
        self.main_player = _player
        self.npc_list = _npc_list
        self.npc_distances = _npc_distances
        self.location = _location

        self.begin_encounter()