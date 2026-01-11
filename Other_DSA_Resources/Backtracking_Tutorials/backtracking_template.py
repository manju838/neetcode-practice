def is_valid_state(state):
    # check if it is a valid solution
    return True

def get_candidates(state):
    # List of candidates used to construct the next state
    return []

def search(state, solutions):
    if is_valid_state(state):
        solutions.append(state.copy())
        # return

    for candidate in get_candidates(state):
        state.add(candidate)
        search(state, solutions)
        state.remove(candidate)

def solve():
    solutions = []
    state = set()
    search(state, solutions)
    return solutions




#######################################
"""
Backtracking is all about giving a solution or a set of solutions that satisfy some constraints.

Key Takeaways:
1. A fn to define if state is valid based on constraints.
2. A fn to feed states to the is_valid_state function.
3. A fn to run the outer loop enclose both the above fns. and save the state if valid
4. A main fn that completely isolates the above 3 fns. 
"""

def is_valid_state(state):
    # check if it is a valid solution
    return True

