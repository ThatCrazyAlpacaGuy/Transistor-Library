class transistor:
    #sets the state to zero by default
    state = 0

    #constructer


    #sets the state
    def setstate(self, newstate):
        if newstate == 1 : self.state = 1
        else: self.state = 0

    #gets the state
    def getstate(self, asstring):
        if asstring == True:
            return str(self.state)
        else:
            return self.state

    #sets the output
    def out(self, trans):
        if self.state == 1: trans.setstate(1)
        else: trans.setstate(0)
    
    #checks if on
    def ifon(self):
        if self.state == 1: return True
        else: return False    
    def invert(self):
        if self.state == 1:
            self.state = 0
        else:
            self.state = 1


