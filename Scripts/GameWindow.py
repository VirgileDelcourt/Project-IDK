from Scripts.BaseWindow import Window, bg
from Scripts.AllActions import *
from Scripts.CharacterScripts import Character
from tkinter import *
from tkinter import ttk


class GameWindow(Window):
    def __init__(self, manager):
        super().__init__(manager, "Project IDK", "1080x720")
        self.combatmanager = manager.combatmanager
        self.combatmanager.updatemethod = self.update

        self.visualbox = Frame(self.window, bg=bg)
        self.UIbox = Frame(self.window, bg=bg)

        # columns setup
        self.UIbox.columnconfigure(0, weight=1)
        self.UIbox.columnconfigure(1, weight=2)
        self.UIbox.columnconfigure(2, weight=1)

        # creation of ui
        self.combobox = ttk.Combobox(self.UIbox, textvariable=StringVar(), state="readonly", width=50)
        self.combobox.bind('<<ComboboxSelected>>', self.updateact)
        self.targetbox = ttk.Combobox(self.UIbox, textvariable=StringVar(), state="readonly", width=20)
        self.desclabel = Label(self.UIbox, text="choose action", font=("Helvetica", 13), bg=bg)
        self.confirmbutton = Button(self.UIbox, text="Confirm", command=self.confirm)

        self.combobox.grid(column=1, row=12, pady=20)
        self.targetbox.grid(column=2, row=12, pady=20)
        self.desclabel.grid(column=1, row=13, pady=10)
        self.confirmbutton.grid(column=1, row=14, pady=10)

        self.buttonmap = []
        for y in range(3, 0, -1):
            self.buttonmap.append([])
            for x in range(5):
                butoon = Label(self.visualbox, text="buttno :)", width=20, height=10, bg=bg)
                self.buttonmap[-1].append(butoon)
                butoon.grid(column=x, row=y)
                butoon.bind("<Button-1>", lambda _: print("mwahahaha"))

        # packing frames
        self.visualbox.pack()
        self.UIbox.pack(side="bottom", fill="both", expand=False)

        self.update()
        self.reset_act()

    def reset_act(self):
        self.combobox.set("choose action")
        self.targetbox.set("choose target")

    def updateact(self, event=None):
        if len(self.combatmanager.stack) <= 0:
            return
        self.combobox["values"] = self.combatmanager.stack[0].getaction()
        act = get_action(self.combobox.get())
        if act:
            self.desclabel.config(text=act.desc)
        targets = [e.name for e in self.combatmanager.entities if e != self.combatmanager.stack[0]]
        self.targetbox["values"] = targets

    def updatemap(self):
        map = self.combatmanager.map
        for y in range(3):
            for x in range(5):
                button = self.buttonmap[y][x]
                character = map[y][x]
                button.bind("<Button-1>", lambda _: print("mwahahaha"))
                if issubclass(type(character), Character):
                    button.config(text=character.name, bg=character.skin)
                    print(character.name)
                    button.bind("<Button-1>", lambda _, mes=character.name: print(mes))

    def update(self):
        self.updateact()
        self.updatemap()

    def confirm(self, event=None):
        action = get_action(self.combobox.get())
        target = self.combatmanager.get_entity(self.targetbox.get())
        if action and target:
            actor = self.combatmanager.stack.pop(0)
            action.on_use(actor, target)
            self.reset_act()
            self.updateact()
        else:
            print(action)
            print(target)
        self.combatmanager.turn()

    def updatecombatmanager(self, cbmanager):
        self.combatmanager = cbmanager
        self.combatmanager.updatemethod = self.update
