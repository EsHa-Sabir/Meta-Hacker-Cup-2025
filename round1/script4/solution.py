import sys



MOD = 10**9 + 7


def modInverse(n):
    return pow(n, MOD - 2, MOD)


def combinations(n, k):
    if k < 0:
        return 0
    if k == 0:
        return 1
    
  
    n %= MOD
    

    numerator = 1
    for i in range(k):
        numerator = (numerator * (n - i + MOD)) % MOD
 
    denominator = 1
    for i in range(1, k + 1):
        denominator = (denominator * i) % MOD
        
    return (numerator * modInverse(denominator)) % MOD


def get_prime_factorization(num):
    factors = {}
    d = 2
    temp = num
    while d * d <= temp:
        while temp % d == 0:
            factors[d] = factors.get(d, 0) + 1
            temp //= d
        d += 1
    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1
    return factors


def count_ways_for_num(factorization, N):
    total_ways = 1
    
    for p, exponent in factorization.items():
        ways_for_prime = combinations(exponent + N - 1, exponent)
        total_ways = (total_ways * ways_for_prime) % MOD
    return total_ways


total_count = 0


def solve_recursive(prime_factors, index, current_divisor, current_factors_p1, N, A, B_factors):
    global total_count


    if index == len(prime_factors):
       
        if current_divisor > A:
            return

        
        p1 = current_divisor
        
       
        ways_p1 = count_ways_for_num(current_factors_p1, N)
  
        factors_p2 = {}
        for p, exp in B_factors.items():
            exp_p1 = current_factors_p1.get(p, 0)
            if exp - exp_p1 > 0:
                factors_p2[p] = exp - exp_p1
        
      
        ways_p2 = count_ways_for_num(factors_p2, N)
        
   
        term = (ways_p1 * ways_p2) % MOD
        total_count = (total_count + term) % MOD
        return


    p, exp_in_B = prime_factors[index]
    
    temp_divisor = 1
    for exp_in_p1 in range(exp_in_B + 1):
      
        if exp_in_p1 > 0:
            current_factors_p1[p] = exp_in_p1
        
        solve_recursive(prime_factors, index + 1, current_divisor * temp_divisor, current_factors_p1, N, A, B_factors)
        
        
        if exp_in_p1 > 0:
            del current_factors_p1[p]
            
        temp_divisor *= p


def solve():
    global total_count
    N, A, B = map(int, sys.stdin.readline().split())

    B_factors = get_prime_factorization(B)
    prime_factors_list = list(B_factors.items())
    
    total_count = 0
    solve_recursive(prime_factors_list, 0, 1, {}, N, A, B_factors)
    
    return total_count


# --- Main script ---
try:
    sys.stdin = open('input.txt', 'r')
except FileNotFoundError:
    print("input.txt not found, using standard input.")
    pass

try:
    sys.stdout = open('output.txt', 'w')
except IOError:
    print("Could not open output.txt for writing.")
    pass

try:
    T = int(sys.stdin.readline())
except (IOError, ValueError):
    T = 0

for i in range(1, T + 1):
    result = solve()
    sys.stdout.write(f"Case #{i}: {result}\n")


if sys.stdout.name != '<stdout>':
    sys.stdout.close()