class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        holder = deque()
        temp = []
        r = 0
        counter = 1
        i = 0

        if len(stones) == 1:
            return stones[0]

        for ch in stones:
            stones[i] = -1
            i += 1
            print(f"\nLOOP: {counter}   {stones}")
            print(f"  {ch}")
            counter+=1
            

            if len(holder) == 0:
                holder.append(ch)
                print(f"  holder: {holder}")
            
            elif ch >= holder[-1]:
                holder.append(ch)
                print(f"  holder: {holder}")
            
            elif ch <= holder[0]:
                holder.appendleft(ch)
                print(f"  holder: {holder}")
            
            elif ch > holder[0] and ch < holder[-1]:
                print(f"  {holder[0]} < ({ch}) < {holder[-1]}")
                while ch > holder[0]:
                    temp.append(holder.popleft())
                    print(f"  holder: {holder}   temp: {temp}")
                holder.appendleft(ch)
                print(f"  holder: {holder}")
                print(f"  temp: {temp}")
                while temp:
                    holder.appendleft(temp.pop())
                    print(f"  holder: {holder}   temp: {temp}")

        counter = 1
        print("\n\nSECOND LOOP")
        while len(holder) > 1:

            print(f"LOOP: {counter}")
            counter+=1

            if holder[-1] == holder[-2]:
                holder.pop()
                holder.pop()
                if len(holder) == 0:
                    return 0

            else:
                if len(holder) == 2:
                    return holder[1] - holder[0]

                holder[-2] = holder[-1] - holder[-2]
                holder.pop()

                if holder[-1] < holder[-2]:
                    temp = []
                    while holder[-1] > holder[0]:
                        temp.append(holder.popleft())
                    holder.appendleft(holder.pop())
                    while len(temp) > 0:
                        holder.appendleft(temp.pop())
                


            print(holder)

        if len(holder) == 0:
            return 0
            
        return holder[0]



