import utils
import player
import npc

class CombatEncounter():
    main_player = None
    npc_list = []
    npc_distances = []
    npc_names = []
    npc_quantities = []
    turn_order = []
    non_friendlies = []

    def get_turn_order(self):
        """generate turn order based on dexterity modifiers"""

        #tuple list of all parties in combat, including player, and their initiatives
        party_list = []

        #calculate initiatives for each NPC
        for _npc in self.npc_list:
            modifier = utils.get_score_mod(_npc.abils[2])
            party_list.append((_npc, utils.die_roll(20, 1, single_mod=modifier)))

            #add name to list of non-friendly NPCs
            if not _npc.hostility == utils.HostilityLevel.FRIENDLY:
                self.non_friendlies.append(_npc.name)
        
        player_dex = utils.get_score_mod(self.main_player.abils[2])
        player_initiative = utils.die_roll(20, 1, single_mod=player_dex)

        #append player to list with PLAYER marker so it can be extracted later
        party_list.append(("PLAYER", player_initiative))

        #sort list by initiative
        party_list.sort(key = lambda x: x[1], reverse=True)

        #unzip list to get parties in order
        self.turn_order = [list(p) for p in zip(*party_list)][0]

    def run_combat(self):
        """while there are still enemies present, allow each party in combat to fight in turn"""
        while len(self.non_friendlies) > 0:
            for party in self.turn_order:
                if party == "PLAYER":
                    print("Present player with combat options")
                else:
                    #run NPC's combat method
                    party.fight()

    def __init__(self, _player, npc_list, npc_distances, npc_names, npc_quantities):
        super().__init__()
        self.main_player = _player
        self.npc_list = npc_list
        self.npc_distances = npc_distances
        self.npc_names = npc_names
        self.npc_quantities = npc_quantities

        self.get_turn_order()

        print(self.turn_order)
        print(self.non_friendlies)

        self.run_combat()