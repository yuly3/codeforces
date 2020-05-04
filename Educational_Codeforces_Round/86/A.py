import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    x, y = map(int, rl().split())
    if x < y:
        x, y = y, x
    a, b = map(int, rl().split())
    
    if 2 * a <= b:
        ans = a * (x + y)
    else:
        ans = a * (x - y) + b * y
    print(ans)


if __name__ == '__main__':
    t = int(rl())
    for _ in range(t):
        solve()
