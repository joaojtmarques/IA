import math
import pickle
import time
from itertools import product

  
class SearchProblem:

  def __init__(self, goal, model, auxheur = []):
    self._queue = []
    self._solution = []
    self._model = model
    self._goal = goal
    self._auxheur = auxheur
    self._queueSize = 0
    self._nOfAgents = 0
    self._limitexp = 0
    ##
    ## to implement
    ## 
    pass

  def search(self, init, limitexp = 2000, limitdepth = 10, tickets = [math.inf,math.inf,math.inf]):
    self._limitexp = limitexp
    self.initialProblem(init)
    self._queueSize = self.getQueueSize()
    self._nOfAgents = len(init)
    possibilities = []

    if self.isOptimalSolution(self.getPossibilityNumber(self._queue[0])):
      return [[], self._queue[0]]

    exitWhile = 0
    while (exitWhile == 0):
      sucessors = []
      for i in range(self._nOfAgents):
        agentSucessors = []
        agentSucessors = self.getSucessors(self._queue[0][i], self._limitexp).copy()
        if self._limitexp == 0:
          return None
        sucessors.append(agentSucessors)
    
      self._queue.pop(0)
      possibilities = self.generatePossiblePaths(sucessors).copy()
      #for el in possibilities:
        #print("element: ", el[0]._number, ", ", el[1]._number, el[2]._number,)
      a = []
      for element in possibilities:
        #print("element", self.getPossibilityNumber(element))
        a = self.getPossibilityNumber(element)
        if self.isPossibleCombination(a):
          if self.isOptimalSolution(a):
            #solucao encontrada, fazer funcao
            if self.enoughTickets(element, tickets):
              solution_found = list(element)
              exitWhile = 1
              break
        else:
          possibilities.remove(element)
        
      if exitWhile != 1:
        self._queue.extend(possibilities)
     # for x in self._queue[0]:
      #  print(x._number)

    print(solution_found)
    #aux = list(solution_found)
    while solution_found[0]._parent != None:
      self._solution.append(self.printAux(solution_found))
      print(self._solution)
      for i in range(len(solution_found)):
        print(i)
        solution_found[i] = solution_found[i]._parent
    
    current_position_number = []
    for x in solution_found:
      current_position_number.append(x._number)

    self._solution.append([[], current_position_number])
    self._solution.reverse()

    print(self._solution)

    ##
    ## to implement
    ##
    return self._solution
  

  def enoughTickets(self, possibility, tickets):
    element = list(possibility)
    tick = tickets.copy()
    print(tickets)
    while element[0]._parent != None:
      for i in range(len(element)):
        if (tick[element[i]._transport] == 0):
          return False
        else:
          tick[element[i]._transport] -= 1
      for i in range(len(element)):
        element[i] = element[i]._parent
    return True

  
  def initialProblem(self, init):
    initialStations = []
    i = 0
    for x in init:
      newStation = Station([-1, x], None, i)
      initialStations.append(newStation)
      i += 1
    self._queue.append(initialStations)


  def getQueueSize(self):
    return len(self._queue)

  def getSucessors(self, station, limitexp):
    sucessors = []
    #print(station._number)
    #print("parent", station._parent._number)
    if self._limitexp == 0:
      return 0
    self._limitexp -=1
    for child in self._model[station._number]:
      newStation = Station(child, station, station._agent)
      newStation.setDistance(self._goal[station._agent], self._auxheur)

      sucessors.append(newStation)
    #sucessors.sort(key=lambda x: x._distance, reverse=False) 
    return sucessors
    

  def generatePossiblePaths(self, sucessors):
    return list(product(*sucessors))


  def isOptimalSolution(self, positionSet):
    return (positionSet == self._goal)

  def getPossibilityNumber(self, possibility):
    lst = []
    for x in possibility:
      lst.append(x._number)
    return lst
  
  def isPossibleCombination(self, possibility):
    for i in range(0, len(possibility)):
      for j in range(1, len(possibility)):
        if possibility[i] == possibility[j] and i != j:
          return False
    return True  

  def printAux(self, current_position):
    aux = []
    auxTransport = []
    auxStations = []
    for x in current_position:
      auxTransport.append(x._transport)
      auxStations.append(x._number)
    aux.append(auxTransport)
    aux.append(auxStations)
    return aux

class Station:

  def __init__(self, child, parent, agent):
    self._transport = child[0]
    self._number = child[1]
    self._parent = parent
    self._distance = 0
    self._agent = agent

  def setDistance(self, goal, auxheur):
    self._distance = math.sqrt((auxheur[self._number-1][0]- auxheur[goal-1][0])**2 +(auxheur[self._number-1][1]- auxheur[goal-1][1])**2)