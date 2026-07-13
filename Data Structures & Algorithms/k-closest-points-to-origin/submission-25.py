class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # math.sqrt(num)
        # to square: num ** 2    or    pow(num, 2)

        candidates = deque()
        i = 0

        # length of candidates
        l = 0

        for p in points:
            d = math.sqrt(((p[0] - 0) ** 2) + ((p[1] - 0) ** 2))
            holder = []

            if l == 0:
                candidates.append((d, i))
                l += 1

            elif l < k:
                if d > candidates[-1][0]:
                    candidates.append((d, i))
                else:
                    while len(candidates) > 0 and d > candidates[0][0]:
                        holder.append(candidates.popleft())
                    candidates.appendleft((d, i))
                    l += 1
                    while len(holder) > 0:
                        candidates.appendleft(holder.pop())

            elif l == k:
                if d < candidates[-1][0]:
                    candidates.pop()
                    l -= 1
                    if l == 0:
                        candidates.append((d, i))
                        l += 1
                    else:
                        while d > candidates[0][0]:
                            holder.append(candidates.popleft())
                        candidates.appendleft((d, i))
                        l += 1
                        while len(holder) > 0:
                            candidates.appendleft(holder.pop())

            i += 1

        while len(candidates) > k:
            candidates.pop()

        holder = []
        for item in candidates:
            holder.append(points[item[1]])
            
        return holder
