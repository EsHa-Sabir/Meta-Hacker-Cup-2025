import sys
from collections import defaultdict

def solve():
    """
    Solves a single test case.
    """
    try:
        N_str = sys.stdin.readline()
        if not N_str: return False
        N = int(N_str)
        A = list(map(int, sys.stdin.readline().split()))
    except (IOError, ValueError):
        return False

   
    prefix_xor = [0] * (N + 1)
    for i in range(N):
        prefix_xor[i+1] = prefix_xor[i] ^ A[i]

    total_lengths_sum = N * (N + 1) * (N + 2) // 6


    counts = defaultdict(int)
    for px_val in prefix_xor:
        counts[px_val] += 1

  
    total_reduction = 0
    for val in counts:
        c = counts[val]
        if c >= 2:
          
            pairs_reduction = c * (c - 1) // 2
            total_reduction += pairs_reduction
        if c >= 3:
         
            triplets_reduction = c * (c - 1) * (c - 2) // 6
            total_reduction += triplets_reduction
            
    
    final_cost = total_lengths_sum - total_reduction
    
    return final_cost

def main():
    """
    Main function to handle multiple test cases and file I/O.
    """
   
    try:
        sys.stdin = open('input.txt', 'r')
        sys.stdout = open('output.txt', 'w')
    except FileNotFoundError:
        print("Error: input.txt not found. Please create it with the sample input.")
        return

    try:
        T_str = sys.stdin.readline()
        if not T_str:
             T = 0
        else:
             T = int(T_str)
    except (IOError, ValueError):
        T = 0

    for i in range(1, T + 1):
        result = solve()
        if result is not False:
            print(f"Case #{i}: {result}")
        else:
            break
            
  
    sys.stdin.close()
    sys.stdout.close()

if __name__ == "__main__":
    main()