######################################################
# Developed by Alborz Geramiard Oct 30th 2012 at MIT #
######################################################
from Policy import *
class eGreedy(Policy):
    epsilon         = None
    old_epsilon     = None 
    def __init__(self,representation,epsilon = .1):
        self.epsilon = epsilon
        super(eGreedy,self).__init__(representation)
    def pi(self,s):
        coin = random.rand()
        if coin < self.epsilon:
            A = self.representation.domain.possibleActions(s)
            return randSet(A)
        else:
            bestA = self.representation.bestActions(s)
            if len(bestA) > 1:
                return randSet(bestA)
            else:
                return bestA[0]
    def turnOffExploration(self):
        self.old_epsilon = self.epsilon 
        self.epsilon = 0
    def turnOnExploration(self):
        self.epsilon = self.old_epsilon
         
        
        
        