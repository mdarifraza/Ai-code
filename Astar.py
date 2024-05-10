import heapq
class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.heuristic = self.calculate_heuristic()
        self.total_cost = self.path_cost + self.heuristic
    def calculate_heuristic(self):
        """Calculate the heuristic using the Manhattan distance."""
        goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        heuristic = 0
        for i, value in enumerate(self.state):
            if value != 0:
                goal_index = goal_state.index(value)
                current_row, current_col = i // 3, i % 3
                goal_row, goal_col = goal_index // 3, goal_index % 3
                heuristic += abs(current_row - goal_row) + abs(current_col - goal_col)
        return heuristic
    def __lt__(self, other):
        return self.total_cost < other.total_cost
def get_possible_actions(state):
    """Return the list of actions that can be executed in the given state."""
    actions = []
    zero_index = state.index(0)
    if zero_index % 3 > 0:  # Can move left
        actions.append('left')
    if zero_index % 3 < 2:  # Can move right
        actions.append('right')
    if zero_index // 3 > 0:  # Can move up
        actions.append('up')
    if zero_index // 3 < 2:  # Can move down
        actions.append('down')
    return actions
def get_result(state, action):
    """Return the resulting state from taking action in the given state."""
    new_state = list(state)
    zero_index = state.index(0)
    if action == 'left':
        new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]
    elif action == 'right':
        new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]
    elif action == 'up':
        new_state[zero_index], new_state[zero_index - 3] = new_state[zero_index - 3], new_state[zero_index]
    elif action == 'down':
        new_state[zero_index], new_state[zero_index + 3] = new_state[zero_index + 3], new_state[zero_index]
    return tuple(new_state)
def a_star_search(start, goal):
    """Perform the A* search algorithm."""
    frontier = []
    heapq.heappush(frontier, Node(start))
    explored = set()
    while frontier:
        current_node = heapq.heappop(frontier)
        if current_node.state == goal:
            return reconstruct_path(current_node)
        explored.add(current_node.state)
        for action in get_possible_actions(current_node.state):
            child_state = get_result(current_node.state, action)
            child_node = Node(child_state, current_node, action, current_node.path_cost + 1)
            if child_state not in explored and child_node not in frontier:
                heapq.heappush(frontier, child_node)
    return None
def reconstruct_path(node):
    """Reconstruct the path from start to goal."""
    actions = []
    while node.parent is not None:
        actions.append(node.action)
        node = node.parent
    return actions[::-1]
# Define the start and goal states
start_state = (1, 2, 3, 4, 5, 6, 0, 7, 8)
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
# Perform A* search
path = a_star_search(start_state, goal_state)
# Print the path
print("Start State :", start_state)
print("Goal State :", goal_state)
print("Path to solve the 8-puzzle:")
print("Count of Moves " , len(path))
print(path)
