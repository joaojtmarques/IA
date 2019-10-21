import math
import pickle
import time

  
class SearchProblem:

  def __init__(self, goal, model, auxheur = []):
    self._queue = []
    self._solution = []
    self._model = model
    self._goal = goal 
    pass

  def search(self, init, limitexp = 2000, limitdepth = 10, tickets = [math.inf,math.inf,math.inf]):
    
    current_node = init[0];
    
    while(current_node != _goal[0]):
  
      for child in _model[current_node]: 
        node = station(self, child)
        node.setDistance(self, _goal[0], auxheur = [])
        _queue.add(node)
      
      _queue.sort(station.getDistance(self)) 
      print (_queue)
        
    return []

  
class station: 
  def __init__(self, child):
    self._transport = child[0]
    self._number = child[1]
    self._distance = 0
    
  def __init__(self, child, parent):
    self._transport = child[0]
    self._number = child[1]
    self._distance = 0
    self._parent = parent
        
  def setDistance(self, goal, auxheur = []):
    self._distance = math.sqrt((auxheur[_number][0]- auxheur[goal][0])**2 +(auxheur[_number][1]- auxheur[goal][1])**2)
    
  def getDistance(self):
    return _distance
    
    
    
# 0 - taxi
# 1 - autocarro
# 2 - metro