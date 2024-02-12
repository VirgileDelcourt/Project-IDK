from Scripts.CharCreator import *
from Scripts.GameWindow import *
from Scripts.CombatManager import *
from Scripts.CharacterScripts import *
from Scripts.TraitsClass import *
from Scripts.AllTraits import *
from Scripts.AllCharacters import *
from Scripts.AllActions import *


class GameManager:
    def __init__(self):
        self.createwindow = None
        self.gamewindow = None
        self.inventorywindow = None
        self.combatmanager = None
        self.entities = {}
        for c in get_all_characters():
            name = c.__name__
            while name in self.entities:
                name = name + "I"
            self.entities[name] = c
        print(self.entities)

        self.init_characters()
        self.init_creation()

    def close_all_windows(self):
        for w in [self.createwindow, self.gamewindow, self.inventorywindow]:
            if w != None:
                w.end()

    def init_characters(self):
        classes = get_all_characters()
        for c in classes:
            name = c().name
            if name not in self.entities:
                self.entities[name] = c

    def init_creation(self):
        self.close_all_windows()
        self.createwindow = CreationWindow(self)
        self.createwindow.run()

    def init_game_window(self):
        self.close_all_windows()
        self.combatmanager = CombatManager(self, [self.entities["player"], self.entities["Potemkin"]()])
        self.gamewindow = GameWindow(self)
        self.gamewindow.run()

    def character_creation(self):
        if "player" in self.entities:
            raise RecursionError("Tried to create a player when one already existed")
        if self.createwindow != None:
            data = self.createwindow.get_all()
            if data == False:
                return
            else:
                print(auto_create_init_character(data[0], data[1], data[2], data[3]))
                self.entities["player"] = Character(data[0], data[1], data[2], data[3])
                self.init_game_window()

    def gamelog_append(self, mes):
        if self.combatmanager == CombatManager:
            self.combatmanager.logappend(mes)
        else:
            return False


if __name__ == '__main__':
    manager = GameManager()
