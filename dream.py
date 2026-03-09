import inspect

class player:
    def __init__(self, homeStatus="Has a Home"):
        self.homeStatus = homeStatus
    def die(self):
        frame = inspect.currentframe().f_back
        keys_to_delete = [name for name, val in frame.f_locals.items() if val is self]
        
        for name in keys_to_delete:
            del frame.f_locals[name]

dream = player("homeless")

if dream.homeStatus == "homeless":
    print("oh no")
    dream.die()
else:
    print("yay dream has a home")
