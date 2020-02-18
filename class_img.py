
#parameterized constructor
class dancer:
    #attributes of the object (the dancer)
    name = ""
    country = ""
    style = ""

    def __init__(self, n, c, s):
        self.name = n
        self.country = c
        self.style = s

    
    def intro(self):
        print(f"I am {self.name} from {self.country} and my main dance style is {self.style}")

obj1 = dancer("kyoka", "japan", "Hip Hop")
obj1.intro()


