import sys

def solve(n, arr):
    """
    Solves a single test case and returns the list of operations.
    It no longer prints directly.
    """
    # === 1. Correct Partitioning of array A ===
    permutations_info = []
    start_idx = 0
    
    while start_idx < n:
        longest_k = -1
        seen = set()
        max_val_in_segment = 0
        r = arr[start_idx] - 1
        
        for k in range(1, n - start_idx + 1):
            current_val = arr[start_idx + k - 1]
            idx_in_p = k - 1

            if current_val in seen or current_val > (n - start_idx):
                break
            
            seen.add(current_val)
            max_val_in_segment = max(max_val_in_segment, current_val)
            
            if max_val_in_segment == k:
                expected_val = ((idx_in_p + r) % k) + 1
                if current_val == expected_val:
                    longest_k = k
                else:
                    break
        
        k = longest_k
        permutation = arr[start_idx : start_idx + k]
        r = permutation[0] - 1
        permutations_info.append({'k': k, 'r': r})
        start_idx += k

    m = len(permutations_info)
    if m == 0:
        return []

    # === 2. Calculate the total rotations (t_i) for each permutation ===
    t = [0] * m
    t[m-1] = permutations_info[m-1]['r']
    
    for i in range(m - 2, -1, -1):
        k_i = permutations_info[i]['k']
        r_i = permutations_info[i]['r']
        t_next = t[i+1]
        
        current_t = r_i
        while current_t < t_next:
            current_t += k_i
        t[i] = current_t

    # === 3. Generate and return the final list of operations ===
    ops = []
    for i in range(m - 1):
        k_i = permutations_info[i]['k']
        ops.append(f"1 {k_i}")
        
        num_rots = t[i] - t[i+1]
        ops.extend(["2"] * num_rots)
            
    k_last = permutations_info[m-1]['k']
    ops.append(f"1 {k_last}")
    
    num_rots_last = t[m-1]
    ops.extend(["2"] * num_rots_last)
        
    return ops


def main():
    """
    Main function to handle file I/O and test cases.
    All printing is now handled here for consistent formatting.
    """
    try:
        sys.stdin = open('input.txt', 'r')
        sys.stdout = open('output.txt', 'w')
    except FileNotFoundError:
        pass

    try:
        num_test_cases = int(sys.stdin.readline())
    except (IOError, ValueError):
        num_test_cases = 0

    for i in range(1, num_test_cases + 1):
        try:
            n = int(sys.stdin.readline())
            arr = list(map(int, sys.stdin.readline().split()))
        except (IOError, ValueError):
            continue

        # Get the list of operations from the solver
        operations = solve(n, arr)
        
        # Print the output in the exact required format
        sys.stdout.write(f"Case #{i}: {len(operations)}\n")
        for op in operations:
            sys.stdout.write(f"{op}\n")

if __name__ == "__main__":
    main()