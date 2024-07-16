import sys

n = int(sys.stdin.readline().strip())

word = {}

for _ in range(n):
    input_word = sys.stdin.readline().strip()

    if input_word in word.keys():
        word[input_word] += 1
    else:
        word[input_word] = 0

check_word = {}

for _ in range(n - 1):
    input_word2 = sys.stdin.readline().strip()

    if input_word2 in check_word.keys():
        check_word[input_word2] += 1
    else:
        check_word[input_word2] = 0

for k, v in word.items():
    if k not in check_word.keys():
        print(k)
    elif k in check_word.keys() and v != check_word[k]:
        print(k)