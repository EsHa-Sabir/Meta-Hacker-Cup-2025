import sys


def solve():
   
    N, A, B = map(int, sys.stdin.readline().split())

    
    p1 = -1
    for i in range(A, 0, -1):
        if B % i == 0:
            p1 = i
            break
            
  
    p2 = B // p1

   
    multipliers = []

 
    multipliers.append(p1)
    for _ in range(N - 1):
        multipliers.append(1)


    multipliers.append(p2)
    for _ in range(N - 1):
        multipliers.append(1)
   
    return " ".join(map(str, multipliers))


try:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
except FileNotFoundError:

    pass


try:
    T = int(sys.stdin.readline())
except (IOError, ValueError):
    T = 0


for i in range(1, T + 1):
    result = solve()
  
    sys.stdout.write(f"Case #{i}: {result}\n")