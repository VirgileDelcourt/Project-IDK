import inspect
import random
import sys
from Scripts.TraitsClass import *

traits = {"frog": None, "gay": None, "clumsy": None, "bisexual": None, "annoying": None, "wall": None, "gay2": None,
          "demon": None, "sexy demon (hot)": None, "stupid": None, "muscular": None, "narcissistic": None, "man": None,
          "woman": None, "neither": None, "gender is a social construct": None,
          "gender is a scam created by bathroom selling companies": None, "penis": None, "no penis (L)": None,
          "no vagina (big L)": None, "androgynous": None, "you lost the game": None, "fucking cop": None,
          "fun haver": None, "unfun haver (boring)": None, "august 12 2036, the heath death of the universe": None,
          "chimken eater (yummy)": None, "snussy baka": None, "gragonborn": None, ",": None, "edgy": None,
          "teenager": None, "Blahaj haver": None, "sandwich eater": None, "french": None, "ohon baguette": None,
          "Never gonna give you up, never gonna let you down,...": None, "fish man (man of fishes)": None,
          "T-rex": None, "T-shirt": None, "T-pose": None, "T-roc": None, "HOG RIDAAAA": None, "terrorist": None,
          "meme man": None, "political": None, "ball": None, "ugly": None, "communist": None, "catboy": None,
          "straight man (boring)": None, "femboy (hot)": None, "slave": None,
          "hey guys, did you know that in term of water based pokemons, vaporeon is the most": None, "himbo": None}


class Frog(Trait):
    def __init__(self, owner):
        super().__init__("frog", owner, ["race"], ["race"])

    def on_pickup(self):
        self.owner.stats["dexterity"] += 2

    def on_action(self):
        pass


class Gay(Trait):
    def __init__(self, owner):
        super().__init__("gay", owner, ["gay"], [])

    def on_pickup(self):
        self.owner.stats["charisma"] += 1

    def on_action(self):
        return ["charm (gay)"]


class Clumsy(Trait):
    def __init__(self, owner):
        super().__init__("clumsy", owner, [], [])

    def on_pickup(self):
        self.owner.stats["dexterity"] -= 2
        self.owner.stats["luck"] += 1

    def on_action(self):
        pass


class Bisexual(Trait):
    def __init__(self, owner):
        super().__init__("bisexual", owner, ["gay"], [])

    def on_pickup(self):
        self.owner.stats["charisma"] += 1

    def on_action(self):
        return ["charm (gay)"]


class Annoying(Trait):
    def __init__(self, owner):
        super().__init__("annoying", owner, [], [])

    def on_pickup(self):
        self.owner.stats["charisma"] -= 2

    def on_action(self):
        pass


class Wall(Trait):
    def __init__(self, owner):
        super().__init__("wall", owner, ["race"], ["race"])

    def on_pickup(self):
        self.owner.stats["constitution"] += 1
        self.owner.stats["strength"] += 1

    def on_action(self):
        pass


class Gay2(Trait):
    def __init__(self, owner):
        super().__init__("gay2", owner, ["gay", "gay"], [])

    def on_pickup(self):
        self.owner.stats["charisma"] += 1
        self.owner.stats["charisma"] += 1

    def on_action(self):
        return ["charm (gay)"]


class Demon(Trait):
    def __init__(self, owner):
        super().__init__("demon", owner, [], [])

    def on_pickup(self):
        pass

    def on_action(self):
        pass


class SexyDemon(Trait):
    def __init__(self, owner):
        super().__init__("sexy demon (hot)", owner, [], [])

    def on_pickup(self):
        self.owner.stats["charisma"] += 1

    def on_action(self):
        pass


class Stupid(Trait):
    def __init__(self, owner):
        super().__init__("stupid", owner, [], [])

    def on_pickup(self):
        self.owner.stats["charisma"] -= 3
        self.owner.stats["luck"] += 1

    def on_action(self):
        pass


class Muscular(Trait):
    def __init__(self, owner):
        super().__init__("muscular", owner, [], [])

    def on_pickup(self):
        self.owner.stats["strength"] += 2

    def on_action(self):
        pass


class Narcissistic(Trait):
    def __init__(self, owner):
        super().__init__("narcissistic", owner, [], [])

    def on_pickup(self):
        self.owner.stats["charisma"] += random.choice([-1, 1])

    def on_action(self):
        pass


class Man(Trait):
    def __init__(self, owner):
        super().__init__("man", owner, ["gender", "man"], ["gender"])

    def on_pickup(self):
        self.owner.gender = "man"

    def on_action(self):
        pass


class Woman(Trait):
    def __init__(self, owner):
        super().__init__("woman", owner, ["gender", "woman"], ["gender"])

    def on_pickup(self):
        self.owner.gender = "woman"

    def on_action(self):
        pass


class Enby(Trait):
    def __init__(self, owner):
        super().__init__("neither", owner, ["gender", "gay"], ["gender"])

    def on_pickup(self):
        self.owner.gender = "2"
        type(get_trait("androgynous"))(self.owner)

    def on_action(self):
        return ["charm (gay)"]


class Agender(Trait):
    def __init__(self, owner):
        super().__init__("gender is a social construct", owner, ["gender", "gay"], ["gender"])

    def on_pickup(self):
        self.owner.gender = None
        type(get_trait("androgynous"))(self.owner)

    def on_action(self):
        return ["charm (gay)"]


class GenderScam(Trait):
    def __init__(self, owner):
        super().__init__("gender is a scam created by bathroom selling companies", owner, ["gender", "troll"], [])

    def on_pickup(self):
        self.owner.gender = "Toilet :)"

    def on_action(self):
        pass


class Penis(Trait):
    def __init__(self, owner):
        super().__init__("penis", owner, ["penis"], [])

    def on_pickup(self):
        pass

    def on_action(self):
        pass


class NoPenis(Trait):
    def __init__(self, owner):
        super().__init__("no penis (L)", owner, [], ["penis", "man"])

    def on_pickup(self):
        pass

    def on_action(self):
        pass


class NoVagina(Trait):
    def __init__(self, owner):
        super().__init__("no vagina (big L)", owner, [], ["woman"])

    def on_pickup(self):
        pass

    def on_action(self):
        pass


class Androgynous(Trait):
    def __init__(self, owner):
        super().__init__("androgynous", owner, [], [])

    def on_pickup(self):
        self.owner.stats["charisma"] += 1

    def on_action(self):
        pass


class Troll(Trait):
    def __init__(self, owner):
        super().__init__("you lost the game", owner, ["troll"], [])

    def on_pickup(self):
        pass

    def on_action(self):
        pass


class Cop(Trait):
    def __init__(self, owner):
        super().__init__("fucking cop", owner, [], [])

    def on_pickup(self):
        self.owner.stats["charisma"] -= 1
        self.owner.stats["strength"] += 1

    def on_action(self):
        pass


class Comma(Trait):
    def __init__(self, owner):
        super().__init__(",", owner, ["troll"], [])

    def on_pickup(self):
        self.owner.stats["constitution"] -= 5
        self.owner.stats["wisdom"] += 10

    def on_action(self):
        pass


class FunHaver(Trait):
    def __init__(self, owner):
        super().__init__("fun haver", owner, [], [])

    def on_pickup(self):
        self.owner.stats["charisma"] += 1

    def on_action(self):
        pass


class UnfunHaver(Trait):
    def __init__(self, owner):
        super().__init__("unfun haver (boring)", owner, [], [])

    def on_pickup(self):
        self.owner.stats["charisma"] -= 3
        self.owner.stats["intelligence"] += 1
        self.owner.stats["wisdom"] += 1

    def on_action(self):
        pass


class Oracle(Trait):
    def __init__(self, owner):
        super().__init__("august 12 2036, the heath death of the universe", owner, ["troll"], [])

    def on_pickup(self):
        self.owner.stats["wisdom"] += 3

    def on_action(self):
        pass


class ChickenEater(Trait):
    def __init__(self, owner):
        super().__init__("chimken eater (yummy)", owner, [], [])

    def on_pickup(self):
        self.owner.stats["constitution"] += 1
        self.owner.stats["strength"] += 1
        self.owner.stats["dexterity"] += 1

    def on_action(self):
        pass


class Amogus(Trait):
    def __init__(self, owner):
        super().__init__("snussy baka", owner, ["troll"], [])

    def on_pickup(self):
        self.owner.stats["charisma"] -= 2
        self.owner.stats["wisdom"] += 1

    def on_action(self):
        pass


class FailedDragonborn(Trait):
    def __init__(self, owner):
        super().__init__("gragonborn", owner, ["i fucked up"], [])

    def on_pickup(self):
        pass

    def on_action(self):
        pass


class Edgy(Trait):
    def __init__(self, owner):
        super().__init__("edgy", owner, [], [])

    def on_pickup(self):
        self.owner.stats["charisma"] -= 10

    def on_action(self):
        pass


class Teenager(Trait):
    def __init__(self, owner):
        super().__init__("teenager", owner, [], [])

    def on_pickup(self):
        pass

    def on_action(self):
        pass


class Blahaj(Trait):
    def __init__(self, owner):
        super().__init__("Blahaj haver", owner, ["gender"], [])

    def on_pickup(self):
        self.owner.stats["charisma"] += 1

    def on_action(self):
        pass


class HeavyTF2(Trait):
    def __init__(self, owner):
        super().__init__("sandwich eater", owner, [], [])

    def on_pickup(self):
        self.owner.stats["constitution"] += 4
        self.owner.stats["strength"] += 2
        self.owner.stats["dexterity"] -= 1

    def on_action(self):
        pass


class French(Trait):
    def __init__(self, owner):
        super().__init__("french", owner, [], [])

    def on_pickup(self):
        self.owner.stats["charisma"] -= 1

    def on_action(self):
        pass


class French2(Trait):
    def __init__(self, owner):
        super().__init__("ohon baguette", owner, ["troll"], [])

    def on_pickup(self):
        pass

    def on_action(self):
        pass


class RickAstley(Trait):
    def __init__(self, owner):
        super().__init__("Never gonna give you up, never gonna let you down,...", owner, ["troll"], [])

    def on_pickup(self):
        self.owner.stats["charisma"] += 3

    def on_action(self):
        pass


class ManFish(Trait):
    def __init__(self, owner):
        super().__init__("fish man (man of fishes)", owner, [], [])

    def on_pickup(self):
        self.owner.stats["charisma"] += 5

    def on_action(self):
        pass


class Trex(Trait):
    def __init__(self, owner):
        super().__init__("T-rex", owner, ["T"], [])

    def on_pickup(self):
        self.owner.stats["dexterity"] -= 1
        if "T" not in self.owner.stats:
            self.owner.stats["T"] = 0
        self.owner.stats["T"] += 1

    def on_action(self):
        pass


class Tshirt(Trait):
    def __init__(self, owner):
        super().__init__("T-shirt", owner, ["T"], [])

    def on_pickup(self):
        self.owner.stats["strength"] -= 1
        if "T" not in self.owner.stats:
            self.owner.stats["T"] = 0
        self.owner.stats["T"] += 1

    def on_action(self):
        pass


class Tpose(Trait):
    def __init__(self, owner):
        super().__init__("T-pose", owner, ["T"], [])

    def on_pickup(self):
        self.owner.stats["wisdom"] -= 1
        if "T" not in self.owner.stats:
            self.owner.stats["T"] = 0
        self.owner.stats["T"] += 1

    def on_action(self):
        pass


class Troc(Trait):
    def __init__(self, owner):
        super().__init__("T-roc", owner, ["T"], [])

    def on_pickup(self):
        self.owner.stats["charisma"] -= 1
        if "T" not in self.owner.stats:
            self.owner.stats["T"] = 0
        self.owner.stats["T"] += 1

    def on_action(self):
        pass


class HogRider(Trait):
    def __init__(self, owner):
        super().__init__("HOG RIDAAAA", owner, ["troll"], [])

    def on_pickup(self):
        self.owner.stats["charisma"] += 1

    def on_action(self):
        pass


class BadJoke(Trait):
    def __init__(self, owner):
        super().__init__("terrorist", owner, [], [])

    def on_pickup(self):
        pass

    def on_action(self):
        pass


class MemeMan(Trait):
    def __init__(self, owner):
        super().__init__("meme man", owner, [], [])

    def on_pickup(self):
        self.owner.stats["charisma"] += 1

    def on_action(self):
        pass


class Political(Trait):
    def __init__(self, owner):
        super().__init__("political", owner, [], [])

    def on_pickup(self):
        self.owner.stats["charisma"] -= 1

    def on_action(self):
        pass


class Ball(Trait):
    def __init__(self, owner):
        super().__init__("ball", owner, [], [])

    def on_pickup(self):
        self.owner.stats["dexterity"] -= 2
        self.owner.stats["strength"] -= 2
        self.owner.stats["constitution"] += 0

    def on_action(self):
        pass


class Ugly(Trait):
    def __init__(self, owner):
        super().__init__("ugly", owner, [], [])

    def on_pickup(self):
        self.owner.stats["charisma"] -= 2

    def on_action(self):
        pass


class Communist(Trait):
    def __init__(self, owner):
        super().__init__("communist", owner, [], [])

    def on_pickup(self):
        pass

    def on_action(self):
        pass


class Catboy(Trait):
    def __init__(self, owner):
        super().__init__("catboy", owner, [], [])

    def on_pickup(self):
        self.owner.stats["charisma"] += 1

    def on_action(self):
        pass


class Straight(Trait):
    def __init__(self, owner):
        super().__init__("straight man (boring)", owner, [], [])

    def on_pickup(self):
        pass

    def on_action(self):
        pass


class Femboy(Trait):
    def __init__(self, owner):
        super().__init__("femboy (hot)", owner, ["gay"], [])

    def on_pickup(self):
        self.owner.stats["charisma"] += 3

    def on_action(self):
        return ["charm (gay)"]


class Slave(Trait):
    def __init__(self, owner):
        super().__init__("slave", owner, [], [])

    def on_pickup(self):
        self.owner.stats["charisma"] -= 3

    def on_action(self):
        pass


class VaporeonCopypasta(Trait):
    def __init__(self, owner):
        super().__init__("hey guys, did you know that in term of water based pokemons, vaporeon is the most", owner,
                         ["troll"], [])

    def on_pickup(self):
        self.owner.stats["charisma"] -= 5

    def on_action(self):
        pass


class Himbo(Trait):
    def __init__(self, owner):
        super().__init__("himbo", owner, [], [])

    def on_pickup(self):
        self.owner.stats["charisma"] += 1

    def on_action(self):
        pass


def get_all_traits():
    classes = inspect.getmembers(sys.modules[__name__], lambda member: inspect.isclass(member) and member.__module__ == __name__)
    return [t[1] for t in classes]


def init_all_traits():
    global traits
    classes = get_all_traits()
    for c in classes:
        if c(None).name not in traits:
            print(c().name + "not in traits")
        traits[c(None).name] = c(None)
    return traits


def get_trait(name):
    for t in traits:
        if t == name:
            return traits[t]


init_all_traits()
