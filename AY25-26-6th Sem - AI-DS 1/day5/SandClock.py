word = "DLITHE"
n = len(word)
for i in range(n, 0, -1):
    print(" " * (n - i) + " ".join(word[x] for x in range(0, i)))
for i in range(2,n+1):
    print(" " * (n - i) + " ".join(word[x] for x in range(0, i)))
