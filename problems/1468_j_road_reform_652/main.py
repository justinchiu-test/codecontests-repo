#!/usr/bin/env python3

from collections import defaultdict
from math import ceil, sqrt, floor
from heapq import heappush,heappop
import sys

inf = float("inf")

class DisjointSet:
	def __init__(self, n):
		self.n = n
		self.par = [-1] * n
		self.nc = n

	def findParent(self, i):
		if self.par[i] == -1:
			return i #no parent yet
		else:
			var = self.findParent(self.par[i])
			self.par[i] = var
			return var

	def union(self, a, b):
		aPar = self.findParent(a)
		bPar = self.findParent(b)
		if aPar != bPar:
			self.par[aPar] = bPar
			self.nc -= 1

	def numComponents(self):
		return self.nc

def primMSTFaster(adj, source=0):
	edgesUsed = set()
	fringe = list()
	start = (0, source, None) # dist, node, parent
	heappush(fringe, start)
	mstSet = set()
	key = defaultdict(lambda: None)
	key[source] = 0
	while len(fringe) > 0:
		curTup = heappop(fringe)

		curCost = curTup[0]
		cur = curTup[1]
		curParent = curTup[2]

		if cur in mstSet:
			continue

		mstSet.add(cur)

		if curParent is not None:
			edgesUsed.add((curParent, cur, curCost))

		for neighborTup in adj[cur]:
			neighbor = neighborTup[0]
			cost = neighborTup[1]
			if (cost != -1) and (neighbor not in mstSet) and (key[neighbor] is None or key[neighbor] > cost):
				key[neighbor] = cost
				heappush(fringe, (cost, neighbor, cur))
	return edgesUsed, key

'''def primMST(adj, source=0):
	edgesUsed = set()
	fringe = list()
	start = (0, source, None) # dist, node, parent
	heappush(fringe, start)
	mstSet = set()
	key = defaultdict(lambda: None)
	key[source] = 0
	parent = defaultdict(lambda: None)
	while len(fringe) > 0:
		curTup = heappop(fringe)

		curCost = curTup[0]
		cur = curTup[1]
		curParent = curTup[2]

		if cur in mstSet:
			continue

		mstSet.add(cur)

		if curParent is not None:
			edgesUsed.add((curParent, cur, cost))
			parent[cur] = curParent

		for neighbor in adj[cur]:
			cost = adj[cur][neighbor]
			if (neighbor not in mstSet) and (key[neighbor] is None or key[neighbor] > cost):
				key[neighbor] = cost
				heappush(fringe, (cost, neighbor, cur))
	return edgesUsed, key, parent'''



t = int(input())
res = list()
for dsskfljl in range(t):
	splitted = [int(amit) for amit in sys.stdin.readline().split(" ")]
	n = splitted[0]
	m = splitted[1]
	k = splitted[2]
	ds = DisjointSet(n)
	edges = list()
	minDelta = inf
	minEdge = None
	for i in range(m):
		edge = [int(amit) for amit in sys.stdin.readline().split(" ")]
		if edge[2] <= k:
			ds.union(edge[0]-1, edge[1]-1)
		edges.append((edge[0], edge[1], edge[2]))
		if abs(edge[2] - k) < minDelta:
			minDelta = abs(edge[2] - k)
			minEdge = edge

	if ds.numComponents() == 1:
		# connected case, find edge with min |si - k| and make a spanning tree with this edge
		totalCost = abs(minEdge[2] - k)
		res.append(str(totalCost))
	else:
		# unconnected case, must add other edges
		#adj = defaultdict(lambda: dict())
		adj = list()
		for i in range(n):
			adj.append(set())

		for edge in edges:
			s = edge[0] - 1
			t = edge[1] -1
			cost = max(0, edge[2] - k)
			adj[s].add((t, cost))
			adj[t].add((s, cost))

		mst = primMSTFaster(adj, 0)
		edgesUsed = mst[0]
		#print (edgesUsed)
		totalCost = 0
		for edge in edgesUsed:
			#print (edge)
			cost = edge[2]
			totalCost += cost
		res.append(str(totalCost))

sys.stdout.write("\n".join(res))
