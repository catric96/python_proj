#Part A
def DFS(node, goal, path, superLst):
  if node not in superLst:
    superLst = superLst + [node]
    path = path + [node]
  if node == goal:
    return path
  for child in graph[node]:
    if child not in superLst:
      newPath = DFS(child, goal, path, superLst)
      if newPath != None:
          return newPath
  return None

def DFSFewestNodes(node, goal, path, superLst):
  if node not in superLst or superLst[node] > len(path):
    superLst[node] = len(path)
    path = path + [node]
  if node == goal:
    return path
  best = None
  for child in graph[node]:
    if child not in superLst or superLst[child] > len(path):
      newPath = DFSFewestNodes(child, goal, path, superLst)
      if newPath != None:
        if best == None or len(newPath) < len(best):
          best = newPath
  return best

def DFSfindAll(node, goal, paths):
  paths = paths + [node]
  total = []
  if node == goal:
    total = total + [paths]
    return total
  for nodex in graph[node]:
    if nodex not in paths :
      newPath = DFSfindAll(nodex, goal, paths)
      if newPath != None:
          for child in newPath:
            total = total + [child]
  return total     

def DFSLeastMileage(node, goal, paths):
  path = None
  mileage = 0
  for nodex in DFSfindAll(node, goal, paths):
    value = pathDist(nodex)
    if path == None or pathDist(path) > value:
      path = nodex
      mileage = pathDist(path)
  return path, mileage

def pathDist(path):
  total = 0
  cityNum = 0
  for cityNum in range(1, len(path)):
    g = graphX[path[cityNum]]
    tubSet = g[2:]
    for tub in tubSet:
      if tub[0] == path[cityNum-1]:
         print(total)
         total += tub[1]
  return total

def BFS1(node, goal):
  Q = [[node, [node]]]
  while Q:
    nodex = Q.pop(0)
    if nodex[0] == goal:
      return nodex[1]
    for child in graph[nodex[0]]:
      Q.append([child, nodex[1]+[child]])
  return Q

def BFS2(node, goal):
  Q = [('A', [])]
  best = []
  while Q:
    n, path = Q.pop(0)
    newPath = path + [n]
    if n == goal:
      if not best or pathdist(newPath) < pathDist(best):
         best = newPath
    for child in graph[n][2:]:
      if child[0] not in newPath:
        Q.append((child[0], newPath))
  return best
  
def BFS3(node, goal):
  Q = [[node, [node]]]
  while Q:
    nodex = Q.pop(0)
    if nodex[0] == goal:
      return nodex[1]
    for child in graph[nodex[0]]:
      Q.append([child, nodex[1]+[child]])
  return Q

  
def main():
  print('DFS')
  print ('\nA. ANY PATH:', DFS('A', 'B', [], []))
  print ('\nB. LEAST CITIES PATH:', DFSFewestNodes('A', 'B', [], {}))
  print ('\nC. ALL PATHS TO GOAL:')
  count = 0
  for path in DFSfindAll('A', 'B', []):
    print ('-->', count, path)
    count += 1
  #path, mileage = DFSLeastMileage('A', 'B', [])
  #print ('\nD. LEAST MILEAGE PATH: ', path, '. Path is ', mileage, ' miles.', sep = '')
  print()
  node = 'A'
  goal = 'B'
  print ('BFS')
  print ('\nA. Least node path.... from ', node, 'to', goal, '=', BFS1(node, goal))
  path = BFS2(node, goal)
  print('\nB. Least distance path from', node, 'to', goal, '=', path, 'Dist =', pathDist(path))
  #print('\nC. All paths ......... from', node, 'to', goal, '=')
  #for path in enumerate(BFS3(node, goal)):
  #  print ('-->', path[0], '. ', path[1], sep = '')
  
graphX= {'A':[('Z', 75), ('T', 118), ('S', 140)],
	 'Z':[('A', 75), ('O', 71)],
	 'T':[('A', 118), ('L', 111)],
	 'L':[('T', 111), ('M', 70)],
	 'M':[('L', 70), ('D', 75)],
	 'D':[('M', 75), ('C', 120)],
	 'C':[('D', 120), ('R', 146), ('P', 138)],
	 'R':[('C', 146), ('P', 97), ('S', 80)],
	 'S':[('R', 80), ('F', 99), ('O', 151), ('A', 140)],
	 'O':[('S', 151), ('Z', 71)],
	 'P':[('C', 138), ('R', 98), ('B', 101)],
	 'F':[('S', 99), ('B', 211)],
	 'B':[('P', 101), ('F', 211), ('G', 90), ('U', 85)],
	 'G':[('B', 90)],
	 'U':[('B', 85), ('H', 98), ('V', 142)],
	 'H':[('U', 75), ('E', 86)],
	 'E':[('H', 75)],
	 'V':[('U', 142), ('I', 92)],
	 'I':[('V', 92), ('N', 87)],
	 'N':[('I', 87)],}

graph = {'A':['Z', 'T', 'S'],
         'Z':['A', 'O'],
         'T':['A', 'L'],
         'L':['T', 'M'],
         'M':['L', 'D'],
         'D':['M', 'C'],
         'C':['D', 'R', 'P'],
         'R':['C', 'P', 'S'],
         'S':['R', 'F', 'O', 'A'],
         'O':['S', 'Z'],
         'P':['C', 'R', 'B'],
         'F':['S', 'B'],
         }

if __name__ == '__main__':
  main()
