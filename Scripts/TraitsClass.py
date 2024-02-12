class Trait:
    def __init__(self, name, owner, types, bantype):
        self.name = name
        self.owner = None
        self.type = types
        self.bannedtypes = bantype
        if owner != None:
            self.pickup(owner)

    def pickup(self, target):
        self.owner = target
        if not self.compatible_with_char(self.owner):
            del self
            return False
        else:
            self.owner.traits.append(self)
            self.on_pickup()
            return True

    def on_pickup(self):
        pass

    def on_action(self):
        pass

    def compatible_with_char(self, character):
        for t in character.traits:  #check all the types the target already has
            for i in t.type:  #check all the trait's types
                if i in self.bannedtypes:  #we check if he has one of the banned type (we don't want that)
                    return False
        return True

    def compatible_with_traits(self, traits):
        for t in traits:
            for i in t.type:  #check all the trait's types
                if i in self.bannedtypes:  #we check if he has one of the banned type (we don't want that)
                    return False
        return True


    def __repr__(self):
        return self.name


class Test1(Trait):
    def __init__(self, owner=None):
        super().__init__("good trait", owner, ["good"], ["evil"])

    def on_pickup(self):
        Test2(self.owner)


class Test2(Trait):
    def __init__(self, owner=None):
        super().__init__("evil trait", owner, ["evil"], ["good"])
