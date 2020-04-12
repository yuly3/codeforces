import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    t = int(rl())
    for _ in range(t):
        n = int(rl())
        a = list(map(int, rl().split()))
        flg = False
        for i in range(n - 2):
            if a[i] in a[i + 2:]:
                flg = True
                break
        print('YES' if flg else 'NO')


if __name__ == '__main__':
    solve()
