import math 

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        x = self.getParameter("x")
        y = self.getParameter("y")
        
        amountToTurn =  math.atan2(y,x)
        amountToWalk = math.sqrt(x*x+y*y)
        
        motionProxy = ALProxy ("ALMotion")
        motionProxy.walkTo(0,0,amountToTurn)
        motionProxy.walkTo(amountToWalk,0,0)
        
                
                

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
