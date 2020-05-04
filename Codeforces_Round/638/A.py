import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    t = int(rl())
    pow_of_2 = [0]
    for exp in range(1, 31):
        pow_of_2.append(2 ** exp)
    
    ans = []
    for _ in range(t):
        n = int(rl())
        sm = pow_of_2[n]
        for i in range(1, n // 2):
            sm += pow_of_2[i]
        for i in range(n // 2, n):
            sm -= pow_of_2[i]
        ans.append(sm)
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
