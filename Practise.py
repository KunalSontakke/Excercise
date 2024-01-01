int = 1234
rev = 0
while int > 0:
    dig = int % 10
    rev = rev * 10 + dig
    int = int // 10
print(rev)
