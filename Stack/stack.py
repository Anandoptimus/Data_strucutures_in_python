from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        self.container.pop()

    def isEmpty(self):
        return len(self.container) == 0

    def peek(self):
        return self.container[-1]

    def size(self):
        return len(self.container)

    def reverse_string(self,val):
        for i in val:
            self.push(i)
        sel = ''
        for i in range(len(val)):
            sel += self.peek()
            self.pop()
        return sel


def is_match(ch1, ch2):
    match_dict = {
        ']': '[',
        '}': '{',
        ')': '('
    }
    return match_dict[ch1] == ch2


def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch == '(' or ch == '{' or ch == '[':
            stack.push(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if stack.size() == 0:
                return False
            if not is_match(ch, stack.pop()):
                return False

    return stack.size() == 0


if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    stack = Stack()
    a = stack.reverse_string("We will conquere COVID-19")
    print(a)
    # print(a+1)
