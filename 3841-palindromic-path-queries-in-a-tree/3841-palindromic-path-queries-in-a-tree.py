
class SegmentTree:
    def __init__(self, arr):
        self.n = 1
        while self.n < len(arr):
            self.n <<= 1

        self.seg = [0] * (2 * self.n)

        for i, val in enumerate(arr):
            self.seg[self.n + i] = val

        for i in range(self.n - 1, 0, -1):
            self.seg[i] = self.seg[2 * i] ^ self.seg[2 * i + 1]

    def update(self, idx, val):
        p = idx + self.n
        self.seg[p] = val
        p >>= 1

        while p:
            self.seg[p] = self.seg[2 * p] ^ self.seg[2 * p + 1]
            p >>= 1

    def query(self, l, r):
        ans = 0
        l += self.n
        r += self.n

        while l <= r:
            if l & 1:
                ans ^= self.seg[l]
                l += 1

            if not (r & 1):
                ans ^= self.seg[r]
                r -= 1

            l >>= 1
            r >>= 1

        return ans


class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n

        # Iterative DFS
        order = []
        stack = [0]

        while stack:
            u = stack.pop()
            order.append(u)

            for v in graph[u]:
                if v == parent[u]:
                    continue

                parent[v] = u
                depth[v] = depth[u] + 1
                stack.append(v)

        # Calculate subtree sizes and heavy children
        for u in reversed(order):
            largest = 0

            for v in graph[u]:
                if parent[v] == u:
                    size[u] += size[v]

                    if size[v] > largest:
                        largest = size[v]
                        heavy[u] = v

        # Iterative Heavy-Light Decomposition
        head = [0] * n
        pos = [0] * n
        current = 0
        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()

            while u != -1:
                head[u] = h
                pos[u] = current
                current += 1

                for v in graph[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        # Character bitmasks
        base = [0] * n

        for i, ch in enumerate(s):
            base[pos[i]] = 1 << (ord(ch) - ord('a'))

        seg = SegmentTree(base)

        def path_xor(u, v):
            ans = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                ans ^= seg.query(pos[head[u]], pos[u])
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            ans ^= seg.query(pos[u], pos[v])
            return ans

        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                seg.update(
                    pos[u],
                    1 << (ord(c) - ord('a'))
                )

            else:
                u = int(parts[1])
                v = int(parts[2])

                mask = path_xor(u, v)
                answer.append(
                    mask == 0 or (mask & (mask - 1)) == 0
                )

        return answer
