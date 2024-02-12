from Scripts.BaseWindow import bg, Window
from Scripts.CharacterScripts import stats, classes, check_subclass
from Scripts.AllTraits import traits
from tkinter import *
from tkinter import ttk


class CreationWindow(Window):
    def __init__(self, manager):
        super().__init__(manager, "Character Creation", "530x630")

        # creating name entry
        self.namelabel = Label(self.window, text="Name : ", font=("Helvetica", 10), bg=bg, width=10)
        self.namebox = Entry(self.window, textvariable=StringVar(), font=("Helvetica", 10), width=30)

        self.namelabel.grid(column=1, row=0, pady=10)
        self.namebox.grid(column=2, row=0, pady=10)

        # creating class entry
        self.classlabel = Label(self.window, text="Class : ", font=("Helvetica", 10), bg=bg, width=10)
        self.classvar = StringVar()
        self.classvar.set("choose a class")
        self.classbox = ttk.Combobox(self.window, textvariable=self.classvar, state="readonly", width=30)
        self.classbox["values"] = [c for c in classes]

        self.classlabel.grid(column=1, row=1, pady=10)
        self.classbox.grid(column=2, row=1, pady=10)

        # creating subclass entry
        self.subclasslabel = Label(self.window, text="Sub-class : ", font=("Helvetica", 10), bg=bg, width=10)
        self.subclassvar = StringVar()
        self.subclassbox = ttk.Combobox(self.window, textvariable=self.subclassvar, state="readonly", width=30)
        self.updatesubclass()
        self.classbox.bind('<<ComboboxSelected>>', self.updatesubclass)

        self.subclasslabel.grid(column=1, row=2, pady=10)
        self.subclassbox.grid(column=2, row=2, pady=10)

        # creating stats entry
        self.sliders = []
        for i in range(6):
            temp = Slider(self.window, stats[i], 8, 0, 20, self.updatesliders)
            self.sliders.append(temp)
            temp.grid(0, i + 1, 10)

        self.costlabel = Label(self.window, text="27 stat points left", font=("Helvetica", 9), bg=bg)
        self.costlabel.grid(column=0, row=7, pady=20)
        self.updatesliders()

        # creating traits entry
        self.traitlabel = Label(self.window, text="Traits : ", font=("Helvetica", 10), bg=bg)
        self.traitlabel.grid(column=1, row=3, pady=10)
        self.traitboxes = []
        for i in range(5):
            cbbox = ttk.Combobox(self.window, textvariable=StringVar(), state="readonly", width=30)
            cbbox.set("choose trait")
            cbbox["values"] = []
            cbbox.bind('<<ComboboxSelected>>', self.updatetraits)
            self.traitboxes.append(cbbox)
            cbbox.grid(column=2, row=i + 3, pady=10)
        self.updatetraits()

        # creating a create button
        self.createbutton = Button(self.window, text="Create Character", command=self.manager.character_creation)
        self.createbutton.grid(column=0, row=8, columnspan=3, pady=20)

    def getstatsweight(self):
        ans = 0
        for s in self.sliders:
            ans += s.get() - 8
        return ans

    def updatesliders(self):
        weight = self.getstatsweight()
        if 27 - weight >= 0:
            self.costlabel.config(text=str(27 - weight) + " stat points left")
        else:
            self.costlabel.config(text="no more stat points left")

    def updatesubclass(self, event=None):
        clas = self.classvar.get()
        if clas in classes:
            self.subclassvar.set("choose subclass")
            self.subclassbox["values"] = classes[clas]
        else:
            self.subclassvar.set("select class first")
            self.subclassbox["values"] = []

    def updatetraits(self, event=None):  #holy shit this function took me like an hour to make, wtf
        _traits = [box.get() for box in self.traitboxes]
        for box in self.traitboxes:
            allcurrenttraits = self.get_traits_classes()
            if box.get() != "choose trait":
                allcurrenttraits.remove(traits[box.get()])
            values = []
            for t in traits:
                if box.get() in traits and traits[t] != None:
                    values.append(traits[t].name)
                elif t not in _traits and traits[t] != None and t in traits:
                    if traits[t].compatible_with_traits(allcurrenttraits):
                        values.append(traits[t].name)
            box["values"] = values

    def get_traits_classes(self):
        return [traits[box.get()] for box in self.traitboxes if box.get() in traits]

    def get_all(self):
        _name = self.namebox.get()
        if _name == "":
            print("name error")
            return False
        _subclass = self.subclassbox.get()
        if _subclass not in classes and not check_subclass(_subclass):
            print("subclass error")
            return False
        _stats = [s.get() for s in self.sliders]
        if 27 - self.getstatsweight() < 0:
            print("no stat points left")
            return False
        _traits = [b.get() for b in self.traitboxes if b.get() in traits]

        return _name, _subclass, _stats, _traits



class Slider:
    def __init__(self, window, name, basenbr=0, mini=0, maxi=20, update=None):
        self.var = basenbr
        self.min = mini
        self.max = maxi
        self.updatefunc = update

        self.box = Frame(window, bg=bg)
        self.namelabel = Label(self.box, text=name, font=("Helvetica", 12), bg=bg)
        self.lowerbutton = Button(self.box, text="-", command=self.lower, width=5)
        self.increasebutton = Button(self.box, text="+", command=self.increase, width=5)
        self.visuallabel = Label(self.box, text=str(self.var), bg=bg, width=5)

        self.namelabel.grid(column=0, row=0, columnspan=3)
        self.lowerbutton.grid(column=0, row=2, rowspan=2)
        self.increasebutton.grid(column=2, row=2, rowspan=2)
        self.visuallabel.grid(column=1, row=2, rowspan=2)

    def increase(self):
        if self.var < self.max:
            self.var += 1
        self.visuallabel.config(text=str(self.var))
        if type(self.updatefunc) != None:
            self.updatefunc()

    def lower(self):
        if self.var > self.min:
            self.var -= 1
        self.visuallabel.config(text=str(self.var))
        if type(self.updatefunc) != None:
            self.updatefunc()

    def grid(self, column, row, pady=0, padx=0):
        self.box.grid(column=column, row=row, pady=pady, padx=padx)

    def get(self):
        return self.var
