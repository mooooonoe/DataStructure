# ListStack
class ListStack:
	def __init__(self):
		self.__stack = []

	def push(self, x):
		self.__stack.append(x)

	def pop(self):
		return self.__stack.pop()

	def top(self):
		if self.isEmpty():
			return None
		else:
			return self.__stack[-1]

	def isEmpty(self) -> bool:
		return not bool(self.__stack)

	def popAll(self):
		self.__stack.clear() 

	def printStack(self):
		print("Stack from top:", end = ' ')
		for i in range(len(self.__stack)-1, -1, -1):
			print(self.__stack[i], end = ' ')
		print()
		
    
def checkStr(s):
    stack = ListStack()
    found_dollar = False

    for i in range(len(s)):
        if s[i] == '$':
            found_dollar = True
            continue 

        if not found_dollar:
            stack.push(s[i])
        else:
            if stack.isEmpty():
                return False
            if s[i] != stack.pop():
                return False
    
    return stack.isEmpty()