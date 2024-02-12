import inspect
import sys


class Action:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def on_use(self, user, target):
        pass

    def __repr__(self):
        return self.name


class Move(Action):
    def __init__(self, x=1, y=0):
        super().__init__("move", "move your character by " + str(x) + " horizontaly, then " + str(y) + " verticaly")

    def on_use(self, user, target):
        pass


class Attack(Action):
    def __init__(self):
        super().__init__("attack", "slap the shit out of someone")

    def on_use(self, user, target):
        if user.roll("1d20", strength=True, mean="touch")[0] > target.armorclass:
            print(user.name + " hit " + target.name)
            target.damage(user.roll(user.attackpower, strength=True, mean="damage")[0])
        else:
            print(user.name + " attack's failed")


class Charm(Action):
    def __init__(self):
        super().__init__("charm", 'Example : "Girl are you from California ? Cause your the only miss whose I sippie"')

    def on_use(self, user, target):
        bonus = not user.gender == target.gender or user.gender == target.gender and target.gay
        if user.roll("1d20", charisma=bonus, mean="charm")[0] > target.stats["wisdom"]:
            print(user.name + " seduced " + target.name + " !")
            target.love.append(user)
        else:
            print(user.name + " wasn't sexxy enuff for " + target.name + " (sadge)")


class CharmGay(Action):
    def __init__(self):
        super().__init__("charm (gay)", '"Why is everyone so hot ?" said the bi, "Global Warming" said the ace')

    def on_use(self, user, target):
        print(user.name + " used " + self.name + " on " + target.name)
        bonus = 0
        if target.gay:
            bonus += 1
        if target.gender == user.gender or "2" in [target.gender, user.gender]:
            bonus += 2
        if user.roll("1d20", charisma=True, mean="charm", bonus=bonus)[0] > target.stats["wisdom"]:
            print(user.name + " seduced " + target.name + " (gayly) !")
            target.love.append(user)
        else:
            print(user.name + " wasn't sexy enuff for " + target.name + " (litteraly how ??)")


class Charm2(Action):
    def __init__(self):
        super().__init__("charm (2)", '"If Charm is so good then why is there no Charm 2 ?" Guess what bitch !?')

    def on_use(self, user, target):
        print(user.name + " used " + self.name + " on " + target.name)
        if user.roll("1d20", charisma=True, mean="charm")[0] + 3 > target.stats["charisma"]:
            print(user.name + " (greatly) seduced " + target.name + " !")
            target.love.append(user)
        else:
            print(user.name + " wasn't sexy enuff for " + target.name + " (are you ace or somethin ???)")


class PotemkinBuster(Action):
    def __init__(self):
        super().__init__("potemkin buster", "POTEMKIN BASUTAAAA")

    def on_use(self, user, target):
        print(user.name + " used " + self.name + " on " + target.name)
        if user.roll("1d20", dexterity=True, mean="touch")[0] > target.armorclass:
            print(user.name + " grabbed " + target.name)
            target.damage(user.roll(user.attackpower, strength=True, mean="potemkin buster")[0])
        else:
            print(user.name + " didn't manage to grab " + target.name + " (sadge)")


def get_all_actions():
    classes = inspect.getmembers(sys.modules[__name__], lambda member: inspect.isclass(member) and member.__module__ == __name__)
    return [a[1] for a in classes if a[1] != Action]


def get_action(name):
    for a in get_all_actions():
        if a().name == name:
            return a()
    return False
