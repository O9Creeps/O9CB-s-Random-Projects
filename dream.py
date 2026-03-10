import inspect
import random as r

Empty = object()


maxstacks = {
    "_default": 64,
    "sword": 1,
    "range": 1,
    "tool": 1,
    "armor": 1,
    "boat": 1,
    "Empty": 1
}

class player:
    def __init__(self, status="unknown", hp=20):
        self.status = status
        self.hp = hp
        # self.inventory = inventory if inventory is not None else [[Empty, 1]]
        caller_frame = inspect.currentframe().f_back
        info = inspect.getframeinfo(caller_frame)
        line = info.code_context[0].strip()
        if "=" in line:
            self.name = line.split("=")[0].strip()
        else:
            self.name = "Unknown"
        print(f"{self.name} joined the game.")
    def check(self):
        """
        if type(self.inventory) != list:
            self.inventory = [[Empty, 1]]
            print(f"{self.name}'s inventory has been reset.")
        """
        pass
    def attack(self, other):
        self.check()
        if not isinstance(other, player): return
        other.hp -= r.randint(1, 4)
        if other.hp < 1:
            other.die(self)
    def die(self, killer):
        frame = inspect.currentframe().f_back
        keys_to_delete = [nam for nam, val in frame.f_locals.items() if val is self]
        
        for ki in keys_to_delete:
            del frame.f_locals[ki]
            if type(killer) == player: print(f"{killer.name} killed {ki}.")
            else: print(f"{ki} died.")

dream = player("homeless", 12)
sapnap = player("homeful")

if dream.status == "homeless":
    print("dream will now steal sapnaps home")
    dream.attack(sapnap)
    print(f"sapnap now has {sapnap.hp} hp")
    sapnap.attack(dream)
    print(f"dream now has {dream.hp} hp")
    if sapnap.hp < dream.hp: print("dream kicked sapnap out of his own home"); dream.status = "homeful"; sapnap.status = "homeless"
    else: print("dream's ahh gets beaten by sapnap, who keeps his home")
    sapnap.die(dream)
else:
    print("yay dream has a home")
    print("conflict avoided")