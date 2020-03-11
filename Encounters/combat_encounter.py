import utils
import player
import npc

class CombatEncounter():
    main_player = None
    npc_list = []
    npc_distances = []
    npc_quantities = []
    turn_order = []
    non_friendlies = []
    adjacent_npcs = []
    engagements = 0

    def setup_combat(self):
        """generate turn order based on dexterity modifiers, and record adjacencies to player"""

        #tuple list of all parties in combat, including player, and their initiatives
        party_list = []

        #calculate initiatives for each NPC
        for i in range(len(self.npc_list)):
            _npc = self.npc_list[i]
            modifier = utils.get_score_mod(_npc.abils[2])
            party_list.append((_npc, utils.die_roll(20, 1, single_mod=modifier)))

            #is npc adjacent?
            if self.npc_distances[i] <= 5:
                self.adjacent_npcs.append(True)
            else:
                self.adjacent_npcs.append(False)

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
            player_found = False
            for i in range(len(self.turn_order)):
                party = self.turn_order[i]
                if party == "PLAYER":
                    player_found = True
                    self.player_turn()
                else:
                    #run NPC's combat method
                    if player_found:
                        party.fight(self, i - 1)
                    else:
                        party.fight(self, i)

    def player_turn(self):
        """present player with a series of combat options"""

        print("Your turn!\n")

        print("Your current health: ", self.main_player.current_health)

        #tell player which NPCs are in melee range (within 5 feet)
        self.engagements = 0
        print("Engaged in melee with the following NPCs:")
        for i in range(len(self.adjacent_npcs)):
            if self.adjacent_npcs[i]:
                self.engagements += 1
                print(str(self.engagements) + ") " + self.npc_list[i].name)
        if self.engagements == 0:
            print("\tNone")

        choice = input("\nSelect option\n")

    def attack_player(self, npc_name, attack_bonus, damage_die, damage_bonus):
        """roll an attack against a player from a given NPC"""

        roll = utils.die_roll(20, 1, single_mod=attack_bonus)

        if roll[0] >= self.main_player.AC:
            print("The " + npc_name + " hits!")

            damage = utils.die_roll(damage_die[0], damage_die[1], single_mod=damage_bonus)[0]

            self.main_player.current_health -= damage

        else:
            print("The " + npc_name + " misses!")

    def __init__(self, _player, npc_list, npc_distances, npc_quantities):
        super().__init__()
        self.main_player = _player
        self.npc_list = npc_list
        self.npc_distances = npc_distances
        self.npc_quantities = npc_quantities

        self.setup_combat()

        self.run_combat()