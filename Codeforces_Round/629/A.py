import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    t = int(rl())
    ans = []
    for _ in range(t):
        a, b = map(int, rl().split())
        ans.append(b - a % b if a % b != 0 else 0)
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
