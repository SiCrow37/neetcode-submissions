class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # i counts the number of iterations the while loop runs
        # i resets upon student and sandwich match
        # i compares to len(students) so that once i is greater than the len(students) it knows to stop and return the len(students) who cant eat
        i = 0

        l = len(students)

        # j iterates through students
        j = 0

        # s used to store re-qued student
        s = 0

        students = deque(students)
        sandwiches = deque(sandwiches)

        while i < l:
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                i = 0
                l -= 1
            else:
                s = students.popleft()
                students.append(s)
                i += 1
        
        return l


