import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    t = rl().rstrip()
    if t.find('0') == -1:
        print(t)
    elif t.find('1') == -1:
        print(t)
    else:
        if t[0] == '0':
            ans = ''
            for i in range(2 * len(t)):
                if i % 2 == 0:
                    ans += '0'
                else:
                    ans += '1'
        else:
            ans = ''
            for i in range(2 * len(t)):
                if i % 2 == 0:
                    ans += '1'
                else:
                    ans += '0'
        print(ans)


if __name__ == '__main__':
    T = int(rl())
    for _ in range(T):
        solve()
