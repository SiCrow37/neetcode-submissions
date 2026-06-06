class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        seen = {}
        count = 0

        for e in emails:
            i = 0
            curr = ""
            domain = ""
            local = ""

            if e[0] == '@':
                print("e[0] == @")
                continue
            if e.count('@') != 1:
                print(f"more than 1 @ symbol in {e}")
                continue
            if any(ch != ch.lower() and not ch.isalpha() and ch != '+' and ch != '@' and ch != '.' for ch in e):
                print(f"Invalid character in {e}, skipping to next email")
                continue
                
            read = True
            while e[i] != '@':
                print(f"\ni = {i}")

                ch = e[i]
                print(f"ch = {ch}")

                if ch.isalpha() and read:
                    local += ch
                    print(f"local = {local}")
                elif ch == '.':
                    print(". skipped")
                    i += 1
                    continue
                elif ch == '+':
                    read = False
                    print("read switched to FALSE")
                i += 1
            
            curr += local + '@'
            print(f"curr = {curr}")

            match = re.search(r"@(.*)", e)

            if match:
                domain = match.group(1)
                print(f"domain = {domain}")
                
            if domain[-3:] != ".io" and domain[-4:] != ".com":
                print(f"{e} doesnt end in .com or .io")
                continue

            else:
                curr += domain
                if curr in seen:
                    continue
                else:
                    seen[curr] = 1
                    count += 1
                    print(f"{e} accepted: count = {count}")
        return count


                
                



