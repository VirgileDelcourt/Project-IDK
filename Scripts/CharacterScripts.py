from Scripts.AllTraits import *
from random import randint
from enum import Enum

stats = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
classes = {"Paladin": ["Heretic", "New Faith", "A Real Paladin"],
           "Tank": ["Prayer Tank", "Punch Tank", "A Real Tank"],
           '"Mage"': ["Gatling Gun", "Sniper Rifle", "Hand Grenade"],
           "Generic Clerc Guy": ["(Un)Holy Presence", "Inverse Healing", "That One Skill"],
           "Capitalist": ["Midas Potion", "Gilded Sacrifice", "Useless"],
           "Furry": ["Fursuit Jellyfish", "Fursuit Yugi Muto", "Fursuit Tsar Bomba"],
           "Grappler": ["Red Oni", "Russian Guy", "POTEMKIN BASUTAAAA"]}


class Character:
    def __init__(self, name, subclass, stat, trait):
        self.name = name
        self.skin = "grey"

        self.classe = get_class_by_subclass(subclass)
        self.subclass = subclass

        self.hp = 10
        self.stats = {"strength": stat[0], "dexterity": stat[1], "constitution": stat[2],
                      "intelligence": stat[3], "wisdom": stat[4], "charisma": stat[5],
                      "luck": 0}
        self.attackpower = "1d4"
        self.armorclass = 0

        self.love = []
        self.gender = None
        self.gay = False

        self.traits = []
        for t in trait:
            if type(t) == str:
                t = get_trait(t)
            type(t)(self)

    def getaction(self):
        ans = ["attack"]
        for t in self.traits:
            temp = t.on_action()
            if temp != None:
                if type(temp) != list:
                    temp = [temp]
                for act in temp:
                    if act not in ans:
                        ans.extend(temp)
        return ans

    def roll(self, *args, **kwargs):
        ans = 0
        log = ""
        for s in stats:
            if s in kwargs and kwargs[s] == True:
                modif = (self.stats[s] - 10) // 2
                ans += modif
                if modif < 0:
                    log += "-" + str(modif)[1:] + " from " + s
                else:
                    log += "+" + str(modif) + " from " + s
            elif s in kwargs and kwargs[s] == False:
                modif = (self.stats[s] - 10) // 2
                ans -= modif
                if modif < 0:
                    log += "+" + str(modif)[1:] + " from " + s
                else:
                    log += "-" + str(modif) + " from " + s
        for d in args:
            split = d.split("d")
            n, w = int(split[0]), int(split[1])
            for _ in range(n):
                roll = randint(1, w)
                if kwargs["mean"]:
                    print(self.name + " rolled a nat " + str(roll) + " " + log + " for " + kwargs["mean"])
                else:
                    print(self.name + " rolled a nat " + str(roll) + " " + log)
                ans += roll
        if "bonus" in kwargs and kwargs["bonus"] == True:
            ans += kwargs["bonus"]
        if ans > 20:
            ans = 20
        elif ans < 0:
            ans = 0
        return ans, log

    def damage(self, dmg):
        self.hp -= dmg
        print(self.name + " got hit for " + str(dmg) + " (" + str(self.hp) + " hp left)")

    def __repr__(self):
        return self.name + " (" + self.classe + ")"


def get_class_by_subclass(subclass):
    return [c for c in classes if subclass in classes[c]][0]


def check_subclass(subclass):
    return len([c for c in classes if subclass in classes[c]]) > 0
