import sys

# Graph problems mein gehri recursion ke liye limit badhana zaroori ho sakta hai.
sys.setrecursionlimit(400005)

def find_tour(u, adj, ptrs, visited_edges, tour_edges):
    """
    Hierholzer's algorithm par adhaarit, yeh function recursively Eulerian tour dhoondhta hai.
    """
    while ptrs[u] < len(adj[u]):
        v, edge_index = adj[u][ptrs[u]]
        ptrs[u] += 1
        if not visited_edges[edge_index]:
            visited_edges[edge_index] = True
            find_tour(v, adj, ptrs, visited_edges, tour_edges)
            # Jab recursion se wapas aate hain, tab edge ko tour mein add karte hain.
            tour_edges.append(edge_index)

def solve(case_num, f_in, f_out):
    """
    Har ek test case ko solve karta hai.
    """
    try:
        line = f_in.readline()
        if not line: return
        N, M = map(int, line.split())
    except (IOError, ValueError):
        return

    adj = [[] for _ in range(N + 1)]
    degrees = [0] * (N + 1)
    edges = []

    for i in range(M):
        u, v = map(int, f_in.readline().split())
        adj[u].append((v, i))
        adj[v].append((u, i))
        degrees[u] += 1
        degrees[v] += 1
        edges.append((u, v))

    # Jin nodes ki activities odd number mein hain, unhe store karte hain.
    is_odd_degree = [False] * (N + 1)
    odd_nodes = []
    for i in range(1, N + 1):
        if degrees[i] % 2 != 0:
            odd_nodes.append(i)
            is_odd_degree[i] = True

    # Odd-degree nodes ko jodkar "dummy" edges add karte hain.
    edge_count = M
    for i in range(0, len(odd_nodes), 2):
        u, v = odd_nodes[i], odd_nodes[i + 1]
        adj[u].append((v, edge_count))
        adj[v].append((u, edge_count))
        edge_count += 1
        
    assignments = [''] * M
    visited_edges = [False] * edge_count
    ptrs = [0] * (N + 1)

    # Tour shuru karne ke liye nodes ki priority set karte hain.
    # Odd-degree wale nodes pehle aayenge.
    tour_starters = odd_nodes + [i for i in range(1, N + 1) if not is_odd_degree[i]]

    # Graph ke har component mein Eulerian circuit dhoondhte hain.
    for i in tour_starters:
        if ptrs[i] < len(adj[i]): # Check karte hain ki node pehle se traverse to nahi hua.
            tour_edges = []
            find_tour(i, adj, ptrs, visited_edges, tour_edges)
            
            # Tour ke edges ko alternately color (assign) karte hain.
            color = 1
            for edge_index in tour_edges:
                if edge_index < M:  # Sirf original edges ko assign karte hain.
                    assignments[edge_index] = str(color)
                color = 3 - color # 1 aur 2 ke beech mein toggle.

    # Assignments ke aadhar par final cost calculate karte hain.
    day1_degrees = [0] * (N + 1)
    day2_degrees = [0] * (N + 1)
    cost = 0

    for i in range(M):
        u, v = edges[i]
        if assignments[i] == '1':
            day1_degrees[u] += 1
            day1_degrees[v] += 1
        else:
            day2_degrees[u] += 1
            day2_degrees[v] += 1

    for i in range(1, N + 1):
        cost += day1_degrees[i]**2 + day2_degrees[i]**2

    # Final result format ke mutabik print karte hain.
    f_out.write(f"Case #{case_num}: {cost} {''.join(assignments)}\n")

def main():
    """
    File I/O handle karne aur sabhi test cases ko run karne ke liye main function.
    """
    try:
        with open('input.txt', 'r') as f_in, open('output.txt', 'w') as f_out:
            line = f_in.readline()
            if line:
                T = int(line)
                for i in range(1, T + 1):
                    solve(i, f_in, f_out)
    except FileNotFoundError:
        print("Error: 'plan_out_validation_input.txt' file nahi mili.")

if __name__ == "__main__":
    main()