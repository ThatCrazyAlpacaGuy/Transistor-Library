class transistor:
    
    statebool = False

    #constructer
    def __init__(self, state):
        if state >= 1:
            self.statebool = True
        else:
            self.statebool = False
    
    #getting the state
    def getstate(self):
        if self.statebool == True:
            return 1
        else:
            return  0
    
    #setting the state
    def setstate(self, state):
        if state >= 1:
            self.statebool == True 
        else:
            self.statebool == False

    #seting the output
    def out(self, transistor):
        if self.statebool == True:
            transistor.setstate(1)
        else:
            transistor.setstate(0)
    
    #if on bool
    def ifon(self):
        return self.statebool

    




