import sys
import bisect

def solve():
    """
    Solves a single test case.
    """
    try:
        N, Q, L = map(int, sys.stdin.readline().split())
        X = list(map(int, sys.stdin.readline().split()))
    except (IOError, ValueError):
        return # Handle empty lines at the end of file

    # Store initial positions with 1-based indexing for convenience
    initial_X = {i + 1: X[i] for i in range(N)}

    # Keep a sorted list of all wall positions
    walls = [1, L]
    
    total_ans = 0

    for _ in range(Q):
        line = sys.stdin.readline().split()
        op_type = int(line[0])

        if op_type == 1:
            # Type 1: Add a new wall
            x = int(line[1])
            bisect.insort(walls, x)
        
        elif op_type == 2:
            # Type 2: Run a simulation query
            r, s = int(line[1]), int(line[2])
            
            # 1. Find the segment [W_L, W_R] containing robot r
            Xr = initial_X[r]
            # Find the index of the first wall to the right of Xr
            wall_idx = bisect.bisect_right(walls, Xr)
            W_L = walls[wall_idx - 1]
            W_R = walls[wall_idx]
            D = float(W_R - W_L)

            best_k = 0
            max_t_last = -1.0
            
            # 2. Iterate through all possible robots k to find candidates
            for k in range(1, N + 1):
                # Condition: k must have a higher index
                if k <= r:
                    continue

                Xk = initial_X[k]
                
                # Condition: k must be in the same segment as r
                if not (W_L < Xk < W_R):
                    continue
                
                # 3. Calculate first collision time (t0)
                t0 = (Xr + Xk - 2 * W_L) / 2.0

                # Condition: A collision must be possible at or before time s
                if t0 > s:
                    continue
                
                # 4. Calculate the last collision time before or at s
                if D == 0:
                    t_last = t0
                else:
                    # m is the number of full periods (D) elapsed between t0 and s
                    m = (s - t0) // D
                    t_last = t0 + m * D

                # 5. Keep track of the robot from the latest collision event
                if t_last > max_t_last:
                    max_t_last = t_last
                    best_k = k
            
            total_ans += best_k

    return total_ans

def main():
    """
    Main function to handle multiple test cases.
    Reads from 'input.txt' and writes to 'output.txt'.
    """
    # Redirect standard I/O to files
    try:
        sys.stdin = open('input.txt', 'r')
        sys.stdout = open('output.txt', 'w')
    except FileNotFoundError:
        print("input.txt not found, reading from standard input.")

    # Read the number of test cases
    try:
        num_test_cases = int(sys.stdin.readline())
    except (IOError, ValueError):
        num_test_cases = 0

    for i in range(1, num_test_cases + 1):
        result = solve()
        print(f"Case #{i}: {result}")

if __name__ == "__main__":
    main()