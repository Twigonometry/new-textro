import utils
import player
import npc

class CombatEncounter():
    main_player = None
    npc_list = []
    npc_distances = []
    npc_names = []
    npc_quantities = []
    npc_initiatives = []
    turn_order = []

    def get_turn_order(self):
        """generate turn order based on dexterity modifiers"""

        #tuple list of all parties in combat, including player, and their initiatives
        party_list = []

        #calculate initiatives for each NPC
        for _npc in self.npc_list:
            modifier = utils.get_score_mod(_npc.abils[2])
            party_list.append((_npc, utils.die_roll(20, 1, single_mod=modifier)))
        
        player_dex = utils.get_score_mod(self.main_player.abils[2])
        player_initiative = utils.die_roll(20, 1, single_mod=player_dex)

        #append player to list with PLAYER marker so it can be extracted later
        party_list.append(("PLAYER", player_initiative))

        print(party_list)

        #sort list by initiative
        party_list.sort(key = lambda x: x[1])

        print(party_list)

        #unzip list to get parties in order
        parties = [list(p) for p in zip(*party_list)][0]
        
        print(parties)

        #remove player tuple
        #player_tuple = party_list.pop([party_list[0] for p in party_list].index("PLAYER"))

    def __init__(self, _player, npc_list, npc_distances, npc_names, npc_quantities):
        super().__init__()
        self.main_player = _player
        self.npc_list = npc_list
        self.npc_distances = npc_distances
        self.npc_names = npc_names
        self.npc_quantities = npc_quantities

        self.get_turn_order()