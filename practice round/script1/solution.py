# We need 'sys' for fast input, which is important for large test cases.
import sys

def solve():
    """
    This function solves one test case for Chef Alfredo's problem.
    """
    
    # --- Fast Input Section (Improved) ---
    try:
        # Check if the line for N is empty before reading
        line_n = sys.stdin.readline()
        if not line_n.strip():
            return None, None
        N = int(line_n)
        
        # Read lines for A and B
        line_a = sys.stdin.readline()
        line_b = sys.stdin.readline()
        
        # Handle case where file ends unexpectedly
        if not line_a or not line_b:
            return None, None

        A = list(map(int, line_a.split()))
        B = list(map(int, line_b.split()))

    except (IOError, ValueError):
        # This handles errors if a line cannot be converted to a number
        return None, None

    # --- New and Correct Plan ---

    # Step 1: The impossible check
    for i in range(N):
        if A[i] > B[i]:
            return -1, []

    # Step 2: Get organized
    sources_at_temp = [[] for _ in range(N + 2)]
    for i in range(N):
        dish_number = i + 1
        current_temp = A[i]
        sources_at_temp[current_temp].append(dish_number)

    dishes_that_need_temp = [[] for _ in range(N + 2)]
    for i in range(N):
        if A[i] < B[i]:
            dish_number = i + 1
            target_temp = B[i]
            dishes_that_need_temp[target_temp].append(dish_number)

    operations = []

    # Step 3: The "Chain Reaction"
    for temp in range(1, N + 1):
        for dish_to_heat in dishes_that_need_temp[temp]:
            if not sources_at_temp[temp]:
                return -1, []
            
            source_dish = sources_at_temp[temp][0]
            operations.append((source_dish, dish_to_heat))

        # After a dish is heated, it can become a source for other dishes at the same temperature.
        for heated_dish in dishes_that_need_temp[temp]:
            sources_at_temp[temp].append(heated_dish)
            
    return len(operations), operations

# === MAIN PROGRAM (The Manager) ===

# --- File Handling Setup ---
# Input file ka naam
input_filename = 'input.txt'
# Output file ka naam
output_filename = 'output.txt'

# Redirect standard input and output to files
try:
    sys.stdin = open(input_filename, 'r')
    sys.stdout = open(output_filename, 'w')
except FileNotFoundError:
    # This error will print to your console if input.txt is missing
    sys.stdout = sys.__stdout__ # Restore console output
    print(f"Error: Make sure '{input_filename}' is in the same folder as the script.")
    exit()

# Read the number of test cases
try:
    line = sys.stdin.readline()
    # Check if the file is empty or the line is blank
    if line and line.strip():
        T = int(line.strip())
    else:
        T = 0
except (IOError, ValueError):
    T = 0

# Loop 'T' times for each test case.
for i in range(1, T + 1):
    result = solve()
    
    # If solve() returns None, it means the end of the file was reached.
    if result is None or result[0] is None:
        break 
    
    k, ops = result
    
    # Print the result in the required format.
    if k == -1:
        print(f"Case #{i}: -1")
    else:
        print(f"Case #{i}: {k}")
        for op_pair in ops:
            print(f"{op_pair[0]} {op_pair[1]}")

# Files ko aakhir mein band karna ek achi practice hai
sys.stdout.close()
sys.stdin.close()
