import socket
import argparse
from collections import defaultdict

##############################################################
# Graph code
##############################################################

# https://www.geeksforgeeks.org/strongly-connected-components/

class Graph:

  def __init__(self, vertices):
    self.V = vertices # No. of vertices
    self.graph = defaultdict(list) # default dictionary to store graph
  
  # function to add an edge to graph
  def add_edge(self, u, v):
    self.graph[u].append(v)
  
  # A function used by DFS
  def dfs_util(self, v, visited):
    # Mark the current node as visited and print it
    visited[v] = True
    sscs = [v]
    # Recur for all the vertices adjacent to this vertex
    for i in self.graph[v]:
      if visited[i] == False:
        more = self.dfs_util(i, visited)
        sscs.extend(more)
    return sscs
  
  def fill_order(self, v, visited, stack):
    # Mark the current node as visited
    visited[v] = True
    # Recur for all the vertices adjacent to this vertex
    for i in self.graph[v]:
      if visited[i] == False:
        self.fill_order(i, visited, stack)
    stack = stack.append(v)
  
  # Function that returns the reverse (or transpose) of  the graph
  def get_transpose(self):
    g = Graph(self.V)
    # Recur for all the vertices adjacent to this vertex
    for i in self.graph:
      for j in self.graph[i]:
        g.add_edge(j, i)
    return g
  
  # The main function that finds all strongly connected component
  def get_sccs(self):
    stack = []
    sscs = []
    # Mark all the vertices as not visited (For first DFS)
    visited = [False] * self.V
    # Fill vertices in stack according to their finishing times
    for i in range(self.V):
      if visited[i] == False:
        self.fill_order(i, visited, stack)
    # Create a reversed graph
    transpose = self.get_transpose()
    # Mark all the vertices as not visited (For second DFS)
    visited = [False] * self.V
    # Now process all vertices in order defined by Stack
    while stack:
      i = stack.pop()
      if visited[i] == False:
        sscs.append(transpose.dfs_util(i, visited))
    return sscs
  
  def __str__(self):
    return list(self.graph.items()).__str__()


##############################################################
# Socket code
##############################################################

EDGES = []


def parse_data(data):
  msg = data.decode()
  split_msg = msg.split(' ')
  func = split_msg[0]
  params = []
  if len(split_msg) > 1:
    params.extend(split_msg[1:])
  return func, ' '.join(params)


def set_edges(_, edges):
  global EDGES
  EDGES = []
  edges = edges.split()
  for edge in edges:
    start, end = edge.split(',')
    EDGES.append([int(start), int(end)])


def solve(conn, state):
  graph = Graph()
  [last_state, beacons_reading, emm_edges, thresh_str] = state.split(' ')
  


def run_server(ip, port, buffer_size):
  funcs = {'solve':solve, 'set-edges':set_edges}
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((ip, port))
  s.listen(1)
  print('Listening to {}:{} with buffer size {}'.format(ip, port, buffer_size))
  conn, addr = s.accept()
  print('Connected to:', addr)
  while 1:
    data = conn.recv(buffer_size)
    func, params = parse_data(data)
    if func == 'exit':
      break
    if func not in funcs.keys():
      print('Function {} not defined'.format(func))
    else:
      res = funcs[func](conn, params)
  conn.close()


if __name__ == '__main__':
  # Construct the argument parser and parse command line arguments
  ap = argparse.ArgumentParser()
  ap.add_argument('-i', '--ip', type=str, default='0.0.0.0', help='IP address of the device | DEFAULT: 0.0.0.0')
  ap.add_argument('-p', '--port', type=int, default=5000, help='Ephemeral port number of the server (1024 to 65535) | DEFAULT: 5000')
  ap.add_argument('-b', '--buffer-size', type=int, default=2**10, help='Message Buffer size | DEFAULT: 2^10')
  args = vars(ap.parse_args())
  run_server(**args)