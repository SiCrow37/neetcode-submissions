class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.f = deque()

    def get(self, key: int) -> int:
        if key in self.d:
            holder = []
            while self.f and self.f[0] != key:
                holder.append(self.f.popleft())
            self.f.append(self.f.popleft())
            while len(holder) > 0:
                self.f.appendleft(holder.pop())
            
            return self.d[key]

        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        self.d[key] = value
        if key not in self.f:
            self.f.append(key)
        else:
            holder = []
            while self.f and self.f[0] != key:
                holder.append(self.f.popleft())
            self.f.append(self.f.popleft())
            while len(holder) > 0:
                self.f.appendleft(holder.pop())

        least = 1000

        if len(self.d) > self.capacity:
           
            del self.d[self.f[0]] 
            self.f.popleft()
        
        return


        