from Scripts.CharacterScripts import *
from Scripts.AllTraits import *


class Potemkin(Character):
    def __init__(self):
        super().__init__("Potemkin", classes["Grappler"][2], (18, 6, 20, 9, 10, 12),
                         [get_trait("muscular"), get_trait("sandwich eater"),
                          get_trait("communist"), get_trait("wall"), get_trait("man")])

    def getaction(self):
        return ["potemkin buster"]


class Panzerkampfwagen(Character):
    def __init__(self):
        super().__init__("Panzerkampfwagen", "A Real Tank", [20, 10, 20, 0, 0, 10],
                         [get_trait("wall"), get_trait("muscular"),
                          get_trait("gender is a social construct"),
                          get_trait("no penis (L)"), get_trait("no vagina (big L)")])


class Succubus(Character):
    def __init__(self):
        super().__init__("Sexxy", "(Un)Holy Presence", [10, 15, 12, 8, 12, 18],
                         [get_trait("sexy demon (hot)"), get_trait("neither"), get_trait("androgynous"),
                          get_trait("fish man (man of fishes)"), get_trait("femboy (hot)")])


def get_all_characters():
    classes = inspect.getmembers(sys.modules[__name__], lambda member: inspect.isclass(member) and member.__module__ == __name__)
    return [c[1] for c in classes]


def auto_create_init_character(name, classe, stat, trait):
    name = '"' + name + '", '
    classe = '"' + classe + '", '
    stat = str(stat) + ", "
    trait = ['get_trait("' + t + '"), ' for t in trait]
    _ = "["
    for s in trait:
        _ += s
    trait = _[:-2] + "]"
    return name + classe + stat + trait
