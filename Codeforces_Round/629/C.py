import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    t = int(rl())
    ans = []
    for _ in range(t):
        n = int(rl())
        digits = input()
        a, b = '', ''
        for i in range(n):
            if digits[i] == '1':
                a += '1' + '0' * (n - i - 1)
                b += '0' + digits[i + 1:]
                break
            else:
                a += str(int(digits[i]) // 2)
                b += str(int(digits[i]) // 2)
        ans.append(a)
        ans.append(b)
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
