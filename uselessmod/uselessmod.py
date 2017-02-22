class UselessClass():
    def __init__(self):
        #make a property
        self.value = "blerg"

    #Here's a useless method
    def beep(self):
        return "beep" if self.value == "blerg" else "nobeep4u"

