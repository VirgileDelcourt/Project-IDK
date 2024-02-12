from random import randint, choice
from time import sleep
from Scripts.AllActions import *
from Scripts.AllActions import get_action


class CombatManager:
    def __init__(self, manager, entities):
        self.manager = manager
        self.entities = entities
        self.log = []  # log of all actions to be displayed
        self.stack = []  # turn order
        self.map = [[None for _ in range(5)] for _ in range(3)]

        self.updatemethod = lambda: None

        for e in self.entities:
            if len([e for i in self.entities if i.name == e.name]) > 1:
                try:
                    int(e.name[-1])
                except:
                    e.name = e.name + " " + str(len([e for i in self.entities if i.name == e.name]) - 1)
                else:
                    e.name = e.name[:-1] + str(int(e.name[-1]) + 1)
            print(e.name + " entered the chat")

        entities = self.get_entities()
        if len(entities) > 5:
            entities = entities[:4]
        pos = [0, 4, 1, 3, 2]
        for i in range(len(entities)):
            self.map[0][pos[i]] = entities[i]

        self.start_turn()

    def get_entity(self, name):
        for e in self.entities:
            if e.name == name:
                return e
        else:
            return False

    def get_entities(self):
        return self.entities

    def start_turn(self):
        print("\nstart of a new turn")
        temp = {}
        for e in self.entities:
            roll = e.roll("1d20", dexterity=True, mean="initiative")
            temp[e] = roll[0]
            print(roll)
        self.stack = [k for k, v in sorted(temp.items(), key=lambda item: item[1], reverse=True)]
        self.updatemethod()
        self.turn()

    def turn(self):
        if len(self.stack) > 0:
            print("\nit is " + self.stack[0].name + "'s turn")
        else:
            self.start_turn()
            return
        if self.stack[0] == self.manager.entities["player"]:
            return
        else:
            user = self.stack.pop(0)
            action = get_action(choice(user.getaction()))
            if "player" in self.manager.entities:
                target = self.manager.entities["player"]
            else:
                target = choice(self.manager.entities.values())
            action.on_use(user, target)
            sleep(0.1)
        self.updatemethod()
        self.turn()
