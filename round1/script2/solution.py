import sys

def can_solve(h, N, heights):
    """
    Checks if a ladder of height 'h' is sufficient to visit all platforms.
    This function implements the "islands" logic in O(N) time.
    """
    if N == 0:
        return True
        
    i = 0
    while i < N:
       
        min_height_in_island = heights[i]
        
      
        j = i
        while j + 1 < N and abs(heights[j+1] - heights[j]) <= h:
            j += 1
            min_height_in_island = min(min_height_in_island, heights[j])
            
    
        if min_height_in_island > h:
      
            return False
   
        i = j + 1
        
   
    return True

def solve_case():
    """
    Solves a single test case using binary search on the answer.
    """
    try:
        N = int(sys.stdin.readline())
        if N == 0:
            return 0
        
        A = list(map(int, sys.stdin.readline().split()))
        
        # Binary search for the minimum possible ladder height 'h'.
        # The lowest possible answer is 0.
        # The highest possible answer is the height of the tallest platform.
        low = 0
        high = 10**9 + 7 # A safe upper bound based on constraints
        ans = high
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if can_solve(mid, N, A):
                # If 'mid' is a possible height, it's a potential answer.
                # Let's try to find an even smaller height.
                ans = mid
                high = mid - 1
            else:
                # If 'mid' is not enough, we need a taller ladder.
                low = mid + 1
                
        return ans

    except (IOError, ValueError):
        return None

def main():
    """
    Main function to handle file I/O and test cases.
    """
    try:
        sys.stdin = open('input.txt', 'r')
        sys.stdout = open('output.txt', 'w')
        
        num_test_cases = int(sys.stdin.readline())
        for i in range(1, num_test_cases + 1):
            result = solve_case()
            if result is not None:
                print(f"Case #{i}: {result}")
                
    except FileNotFoundError:
        print("Error: input.txt not found.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()