import sys
import collections

# Input ko 'input.txt' se parhne aur Output ko 'output.txt' mein likhne ke liye setup
try:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
except FileNotFoundError:
    pass # Agar file na ho to error na de

def solve():
    """
    Ek single test case ko hal karne ka function.
    """
    try:
        R, C, S = map(int, input().split())
    except (IOError, ValueError):
        return

    grid = [input() for _ in range(R)]

    # --- Step 1: Faasla Calculate Karna (Corrected Method) ---
    
    dist = [[-1] * C for _ in range(R)]
    q = collections.deque()

    # Sirf '#' (objects) ko shuruaati khatra (hazard) maano
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '#':
                dist[r][c] = 0
                q.append((r, c))

    # Pehla BFS: Sirf '#' se faasla nikalo
    while q:
        r, c = q.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

    # Ab har cell ke liye, deewar se faasla bhi check karo aur minimum lo
    for r in range(R):
        for c in range(C):
            # Deewar se faasla (yeh ahem correction hai)
            wall_dist = min(r, c, R - 1 - r, C - 1 - c) + 1
            
            # Agar cell tak '#' se nahi pohnch paaye thay
            if dist[r][c] == -1:
                dist[r][c] = wall_dist
            # Agar pohnch gaye thay to minimum lo
            else:
                dist[r][c] = min(dist[r][c], wall_dist)

    # --- Step 2: Safe Islands Dhoondna (Yeh hissa pehle jaisa hi hai) ---
    
    # Asal formal rule hai: faasla >= S + 1
    # Isay hum dist > S likh sakte hain, jo ke same hai
    safe_dist_condition = S + 1

    visited = [[False] * C for _ in range(R)]
    max_size = 0

    for r in range(R):
        for c in range(C):
            # Condition: Agar cell ka faasla zaroorat se zyada/barabar hai aur visited nahi
            if dist[r][c] >= safe_dist_condition and not visited[r][c]:
                current_size = 0
                stack = [(r, c)]
                visited[r][c] = True

                while stack:
                    curr_r, curr_c = stack.pop()
                    current_size += 1
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = curr_r + dr, curr_c + dc
                        if 0 <= nr < R and 0 <= nc < C and dist[nr][nc] >= safe_dist_condition and not visited[nr][nc]:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                
                max_size = max(max_size, current_size)

    return max_size

# --- Main Program ---
T_str = input()
if not T_str:
    # Handle empty input file
    T = 0
else:
    T = int(T_str)


for i in range(1, T + 1):
    result = solve()
    if result is not None:
      print(f"Case #{i}: {result}")