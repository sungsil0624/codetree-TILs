import sys

n = int(sys.stdin.readline().strip())

word = {}

for _ in range(n):
    input_word = sys.stdin.readline().strip()

    word[input_word] = 0

for _ in range(n - 1):
    parity_word = sys.stdin.readline().strip()

    if parity_word in word.keys():
        word[parity_word] += 1

for k, v in word.items():
    if v == 0:
        print(k)