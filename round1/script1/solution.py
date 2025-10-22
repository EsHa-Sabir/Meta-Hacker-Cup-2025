import sys

def solve():
    """
    Reads the platform heights for a single test case,
    calculates the minimum ladder height, and returns it.
    """
    try:
        # Read the number of platforms
        N = int(sys.stdin.readline())
        # If there are no platforms or only one, no ladder is needed.
        if N <= 1:
            # Still need to read the platform heights line to advance the input stream
            if N == 1:
                sys.stdin.readline()
            return 0
        
        # Read the platform heights and convert them to a list of integers
        heights = list(map(int, sys.stdin.readline().split()))
        
        max_difference = 0
        # Iterate through adjacent platforms to find the maximum height difference
        for i in range(N - 1):
            # Calculate the absolute difference in height between platform i and i+1
            difference = abs(heights[i+1] - heights[i])
            # Keep track of the maximum difference found so far
            if difference > max_difference:
                max_difference = difference
                
        return max_difference

    except (IOError, ValueError) as e:
        # Handle potential errors during file reading or data conversion
        print(f"An error occurred: {e}", file=sys.stderr)
        return None

def main():
    """
    Main function to handle file I/O, loop through test cases,
    and write the results to the output file.
    """
    try:
        # Redirect standard input to read from 'input.txt'
        sys.stdin = open('input.txt', 'r')
        # Redirect standard output to write to 'output.txt'
        sys.stdout = open('output.txt', 'w')

        # Read the total number of test cases
        num_test_cases = int(sys.stdin.readline())

        for i in range(1, num_test_cases + 1):
            result = solve()
            if result is not None:
                # Print the result in the required format
                print(f"Case #{i}: {result}")

    except FileNotFoundError:
        print("Error: input.txt not found.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
