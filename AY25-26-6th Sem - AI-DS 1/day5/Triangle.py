word="DLITHE"
n=len(word)
for i in range(0, n):
    print(" " * (n - i) + "".join(word[x] for x in range(0, i + 1)))