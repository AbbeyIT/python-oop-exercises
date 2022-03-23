class CharacterProfile:
    def __init__(self, playerNo, name, attack, defense, hp):
        self.playerNo = playerNo
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp 
        
    def characterStats(self):
        print("Player: " + str(self.playerNo))
        print("Character Name: " + self.name)
        print("Attack: " + str(self.attack))
        print("Defense: " + str(self.defense))
        print("Health Points: " + str(self.hp))


playerOne = CharacterProfile(1, "Kirito", 100, 140, 700)
playerOne.characterStats()

print(" ")

playerOne = CharacterProfile(2, "Asuna", 500, 20, 400)
playerOne.characterStats()

