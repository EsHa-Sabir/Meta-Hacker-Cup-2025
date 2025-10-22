import sys

def solve():
    """
    Reads one test case from input, solves it using the two-pointer simulation,
    and returns the result string.
    """
    try:
        line1 = sys.stdin.readline()
        if not line1: return ""
        N = int(line1.strip())
        S = sys.stdin.readline().strip()
    except (IOError, ValueError):
        return ""

    alice_turns = 0
    bob_turns = 0
    left = 0
    right = N - 1

    while left <= right:
        # Alice's Turn: Find the leftmost 'A'
        found_A = False
        # We search from the current 'left' pointer
        for i in range(left, right + 1):
            if S[i] == 'A':
                alice_turns += 1
                left = i + 1  # The new game starts after the eaten 'A'
                found_A = True
                break
        
        # If Alice couldn't find an 'A', her game is over.
        if not found_A:
            break

        # Bob's Turn: Find the rightmost 'B'
        found_B = False
        # We search from the current 'right' pointer
        for i in range(right, left - 1, -1):
            if S[i] == 'B':
                bob_turns += 1
                right = i - 1 # The new game ends before the eaten 'B'
                found_B = True
                break
        
        # If Bob couldn't find a 'B', his game is over.
        if not found_B:
            break
            
    if alice_turns > bob_turns:
        return "Alice"
    else:
        return "Bob"

def main():
    """
    Main function to handle multiple test cases from files.
    """
    # Redirect standard input and output to files
    try:
        sys.stdin = open('input.txt', 'r')
        sys.stdout = open('output.txt', 'w')
    except IOError:
        print("Error: input.txt not found or cannot write to output.txt")
        return

    try:
        # Read the number of test cases
        num_test_cases_line = sys.stdin.readline()
        if not num_test_cases_line:
            num_test_cases = 0
        else:
            num_test_cases = int(num_test_cases_line.strip())
    except (IOError, ValueError):
        num_test_cases = 0

    for i in range(1, num_test_cases + 1):
        result = solve()
        if result:
            sys.stdout.write(f"Case #{i}: {result}\n")

if __name__ == "__main__":
    main()
