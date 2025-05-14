from library import readint, readstr, DSU

# Secret Passwords: union letters appearing in same string
n = readint()
dsu = DSU(26)
present = [False] * 26
for _ in range(n):
    # unique characters in the password
    letters = set(readstr())
    if not letters:
        continue
    # pick a representative
    rep = ord(next(iter(letters))) - 97
    present[rep] = True
    for c in letters:
        idx = ord(c) - 97
        present[idx] = True
        dsu.union(rep, idx)
# count connected components among present letters
roots = {dsu.find(i) for i, v in enumerate(present) if v}
print(len(roots))
