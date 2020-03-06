import utils
import player
import npc
import world_engine as world
import enum
import combat_encounter as combat

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

    #npc names and quantities by type
    npc_names = []
    npc_quantities = []

    location = world.LocationType

    def begin_encounter(self):
        """run encounter from start;
        introduce NPCs, present interaction choices, and start social/combat encounter based on choices"""

        #introduce NPCs - run all introduce methods, unless the NPCs have the same name
        for i in range(len(self.npc_names)):
            for _npc in self.npc_list:
                if _npc.name == self.npc_names[i]:
                    _npc.introduce(self.npc_quantities[i], self.location)
                    break

        #list visible enemies
        self.display_npcs()

        #check close proximity - if hostile enemy within 10 ft, don't go to interact menu
        hostile_close_proximity = False
        
        for m in range(len(self.npc_distances)):
            if self.npc_distances[m] < 10:
                if self.npc_list[m].hostility == utils.HostilityLevel.HOSTILE:
                    hostile_close_proximity = True
                    multiple = self.npc_quantities[self.npc_names.index(self.npc_list[m].name)] > 1
                    self.npc_list[m].alert_close_proximity(multiple)
                    break

        interaction_result = NextState
        
        if hostile_close_proximity:
            #start combat
            interaction_result = NextState.COMBAT
        else:
            #run interaction choice menu - interactions may return flags that spawn social/combat encounters
            print("Select NPC to interact with:")
            for l in range(len(self.npc_list)):
                print(str(l + 1) + ". " + self.npc_list[l].name + " (Distance: " + str(self.npc_distances[l]) + "ft.)")
            
            choice = 0
            while choice < 1 or choice > len(self.npc_names) + 1:
                try:
                    choice = int(input("Make selection: "))
                except:
                    print("Enter an integer between 1 and " + str(len(self.npc_names)))
            
            interaction_result = self.npc_list[choice - 1].interact(self, choice - 1, self.main_player)

        #spawn social/combat encounter
        #if combat, pass npc list to generate turn order
        if interaction_result.name == "COMBAT":
            #spawn combat encounter
            print("Starting combat")
            new_combat = combat.CombatEncounter(self.main_player, self.npc_list, self.npc_distances, self.npc_quantities)
        elif interaction_result.name == "SOCIAL":
            #spawn social encounter
            print("Starting social encounter")
        elif interaction_result.name == "FINISHED":
            #present next choices, award loot from area
            #allow player to interact with any remaining/new NPCs
            print("Encounter finished")
        elif interaction_result.name == "DEATH":
            #kill the player and end the game
            print("Player dead")

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

        #list of NPC names
        temp_names = []
        for _npc in _npc_list:
            temp_names.append(_npc.name)
        
        self.npc_names = list(set(temp_names))

        for name in self.npc_names:
            self.npc_quantities.append(temp_names.count(name))

        print("Starting encounter")

        self.begin_encounter()