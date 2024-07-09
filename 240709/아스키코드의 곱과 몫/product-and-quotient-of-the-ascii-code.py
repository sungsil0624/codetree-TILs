import sys

a,b = sys.stdin.readline().strip().split()

ascii_code1 = ord(a)
ascii_code2 = ord(b)

print(ascii_code1 * ascii_code2, end = " ")

if ascii_code1 > ascii_code2:
    print(ascii_code1 % ascii_code2)
else:
    print(ascii_code2 % ascii_code1)