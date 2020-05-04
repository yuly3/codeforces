import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    n, k = map(int, rl().split())
    b = set(map(int, rl().split()))
    
    if k < len(b):
        print(-1)
        return
    
    print(n * k)
    for _ in range(n):
        print(' '.join(map(str, b)), end=' ')
        print(' '.join(['1' for _ in range(k - len(b))]), end=' ')
    print('')


if __name__ == '__main__':
    t = int(rl())
    for _ in range(t):
        solve()
