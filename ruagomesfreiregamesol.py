import math
import pickle
import time
  
class SearchProblem:

  def __init__(self, goal, model, auxheur = []):
    self._queue = []
    self._solution = []
    self._model = model
    self._goal = goal
    self._auxheur = auxheur
    
  def search(self, init, limitexp = 2000, limitdepth = 10, tickets = [math.inf,math.inf,math.inf]):
    
    current_node = init[0]
    
    while(current_node != self._goal[0]):
  
      for child in self._model[int(current_node)]: 
        node = Station(child, current_node)
        node.setDistance(self._goal[0], self._auxheur)
        self._queue.append(node)
      
      self._queue.sort(key=lambda x: x._distance, reverse=False)
      current_node = self._queue.pop(0).getNumber()
      print (int(current_node))
      
    for x in self._queue:
      x.printNumber()
      x.printDistance()
        
    return []

  
class Station: 
    
  def __init__(self, child, parent):
    self._transport = child[0]
    self._number = child[1]
    self._distance = 0
    self._parent = parent
        
  def setDistance(self, goal, auxheur):
    self._distance = math.sqrt((auxheur[self._number-1][0]- auxheur[goal-1][0])**2 +(auxheur[self._number-1][1]- auxheur[goal-1][1])**2)
    
  def getDistance(self):
    return self._distance
  
  def getNumber(self):
        return self._number
  
  def printNumber(self):
    print ("filho - ", self._number)
    
  def printDistance(self):
        print ("distance - ", self._distance)
  
    
    
    
# 0 - taxi
# 1 - autocarro
# 2 - metro