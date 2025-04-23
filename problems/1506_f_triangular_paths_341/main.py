#!/usr/bin/env python3

#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
from collections import deque, Counter, defaultdict
from heapq import heapify, heappush, heappop

def solve(Y, X, N):
	points = list(zip(Y, X))
	points.sort()
	res = 0
	y1 = x1 = 1
	for y2, x2 in points:
		if y1 - x1 == y2 - x2:
			if (y1 + x1) % 2 == 0:
				res += y2 - y1
		else:
			y3 = y2 - y1 + 1
			x3 = x2 - x1 + 1
			if (y1 + x1) % 2 == 0:
				res += (y3 - x3) // 2
			else:
				res += (y3 - x3 + 1) // 2
		y1, x1 = y2, x2
	return res


def main():
	for _ in range(inInt()):
		N = inInt()
		Y = inLst()
		X = inLst()
		outInt(solve(Y, X, N))



# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

############ ---- Input Functions ---- ############
# Integer inputs
inInt = lambda: int(input())
# List inputs
inLst = lambda: list(map(int,input().split()))
# String input (transforms into list of chars)
inStr = lambda: list(input())
# Space separated integer variable inputs
inVar = lambda: map(int,input().split())

########### ---- Output Functions ---- ############
# Print integer
outInt = lambda n: sys.stdout.write(str(n) + "\n")
# Print integer list
outLst = lambda lst: sys.stdout.write(" ".join(map(str,lst)) + "\n")
# Print string
outStr = lambda s: sys.stdout.write("".join(s) + "\n")

# endregion

if __name__ == "__main__":
    main()
