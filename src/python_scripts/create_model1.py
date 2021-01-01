from scipy.io import savemat

edges = [[4, 3],[4, 3],[3, 2],[3, 1],[2, 0],[2, 0],[1, 2],[1, 2],[0, 1],[0, 4],[0, 1],[0, 4],[1, 4],[1, 3],[1, 4],[2, 4]]
edges = [[x+1, y+1] for [x, y] in edges]
# Sort edges
edges.sort(key=lambda x: '{},{}'.format(x[0], x[1]))

# Create initial state
initial_state = [1] * len(edges)

if __name__ == '__main__':
  savemat('data/MODEL1.mat', {'EDGES': edges, 'x0FSM':initial_state})