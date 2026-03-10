import inspect
import random as r

class player:
    def __init__(self, status="has a Home", hp=20):
        self.status = status
        self.hp = hp
    def attack(self, other):
        if not isinstance(other, player): return
        other.hp -= r.randint(1, 4)
        if other.hp < 1:
            other.die()
    def die(self):
        frame = inspect.currentframe().f_back.f_back
        keys_to_delete = [name for name, val in frame.f_locals.items() if val is self]
        
        for name in keys_to_delete:
            del frame.f_locals[name]
            print(f"{name} died lmao")

dream = player("homeless")
sapnap = player("homeful")

if dream.status == "homeless":
    print("dream will now steal sapnaps home")
    dream.attack(sapnap)
    print(f"sapnap now has {sapnap.hp} hp")
    sapnap.attack(dream)
    print(f"dream now has {dream.hp} hp")
    if sapnap.hp < dream.hp: print("dream kicked sapnap out of his own home"); dream.status = "homeful"; sapnap.status = "homeless"
    else: print("dream's ahh gets beaten by sapnap, who keeps his home")
else:
    print("yay dream has a home")
